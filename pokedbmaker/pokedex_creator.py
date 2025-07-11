import requests
import sqlite3
# We want to create a set of pokedex tables with the following columns:
# id    name    type_1  type_2  evo_id
# We want to be able to save these in either an sqlite db (default)
# Or we save them to a postgres db


GENERATION_ID_RANGES = {
    1: [1, 151],
    2: [1, 251],
    3: [1, 386],
    4: [1, 493],
    5: [1, 649],
    6: [1, 721]
}


def makePokedex(database_name: str, pokedex_name: str, pokedex_gen: int):
    con = sqlite3.connect(database_name)
    cur = con.cursor()

    # Please don't SQL inject yourself. Do drugs with friends instead!
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS " +
                    noSQLInjects(pokedex_name) +
                    "(id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL, " +
                    "type_1 TEXT NOT NULL, type_2 TEXT, evo_id INTEGER);")
    except sqlite3.Error as error:
        print(error)
    cur.close()
    con.commit()


def insertIntoPokedex(database_name: str, pokedex_name: str, pokedex_gen: int):
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    curr_id = GENERATION_ID_RANGES[pokedex_gen][0]
    end = GENERATION_ID_RANGES[pokedex_gen][1]
    while (curr_id <= end):
        poke_dict = getPokemonById(curr_id)
        query = generateSQLForPokedexInsert(pokedex_name, poke_dict)
        try:
            cur.execute(f"{query[0]}", query[1])
            print(f"Succesfully inserted {poke_dict["name"]}")
        except sqlite3.Error as error:
            print(f"Failed to insert {poke_dict["name"]} due to {error}.")
        curr_id += 1
    con.commit()
    cur.close()

    con.close()


def generateSQLForPokedexInsert(pokedex_name: str, poke_info: dict):
    if len(poke_info['types']) > 1:
        query = "INSERT INTO " + noSQLInjects(pokedex_name) + \
                " (id, name, type_1, type_2, evo_id) values (?,?,?,?,?);"
        values = (poke_info["id"], poke_info["name"], poke_info["types"][0],
                  poke_info["types"][1], poke_info["evo_id"],)
    else:
        query = "INSERT INTO " + noSQLInjects(pokedex_name) + \
            " (id, name, type_1, evo_id) values (?,?,?,?);"
        values = (poke_info["id"], poke_info["name"], poke_info["types"][0],
                  poke_info["evo_id"],)
    return query, values

def getPokemonById(id: int) -> dict:
    res = {}
    res["id"] = id
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(base_url + str(id))
    data = response.json()

    # Get name
    res["name"] = data["name"]

    # Get types
    data_types = data["types"]
    types = []
    if (len(data_types) > 1):
        type_1 = data_types[0]["type"]["name"]
        type_2 = data_types[1]["type"]["name"]
        types.append(type_1)
        types.append(type_2)
    else:
        type_1 = data_types[0]["type"]["name"]
        types.append(type_1)
    res["types"] = types

    # Get evo_id
    base_species_url = "https://pokeapi.co/api/v2/pokemon-species/"
    species_response = requests.get(base_species_url + str(id))
    species_data = species_response.json()
    evo_id_url = species_data["evolution_chain"]["url"]
    res["evo_id"] = stripEvoIdFromURL(evo_id_url)
    return res


def getPokemonFromDBById(id: int, pokedex_name: str,
                         database_name: str) -> str:
    con = sqlite3.connect(database_name)
    cur = con.cursor()
    query = "SELECT * FROM " + noSQLInjects(pokedex_name) + \
        " WHERE id = " + noSQLInjects(str(id)) + ";"
    print(query)
    try:
        cur.execute(query)
        con.commit()
        row = cur.fetchone()
        print(f"Row: {row}")
        cur.close()
    except sqlite3.Error as error:
        print(error)
        return "Something went wrong"
    finally:
        if con:
            con.close()
            print("Closed sqlite connection")
    return row


def stripEvoIdFromURL(url: str) -> int:
    parts = url.split("/")
    id = parts[-2]
    return int(id)


def noSQLInjects(phrase: str) -> str:
    return ''.join(chr for chr in phrase if chr.isalnum())

