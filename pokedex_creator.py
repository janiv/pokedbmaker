import requests
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


def makePokedex():
    return 0


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


def stripEvoIdFromURL(url: str) -> int:
    parts = url.split("/")
    id = parts[-2]
    return int(id)
