# Pokemon Database Maker
I needed a way to create Pokemon databases for a personal project I have been 
working on. I have already made a similar project in the past but it is 
extremely messy. The original was called Pokemon Database Helper and created a
Postgres database that I then used to create janiv.github.io. Because I was 
such a noob I made a bunch of nooby mistakes that I want to clean up with this 
version.

All data will come from PokeAPI. We will need to fix a few things because 
PokeAPI does have a few things that long time players will recognize to be 
wrong. 

## Basic features
1. Create any single generation pokedex with the following columns: id, name,
   type_1, type_2, evo_id.
2. Create encounter tables for all routes in a pokemon game.
3. Store these tables in sqlite.
4. Create a script that fixes some of the weird things that the PokeAPI will
   give as values. For example Magnemite is not a steel type until Gen 2.

## Commands
1. pokedbmaker dex {gen} {dbname-optional}. Where {gen} is a number 1-6. For example:
   pokedbmaker dex 1
   Creates a Pokemon.db with a table called gen_1_dex. It pull the information from
   the Pokeapi website and applies fixes listed in fixes.txt. If you provide a
   different dbname it will create or update that db instead.
2. pokedbmaker encounters {gamename} {dbname-optional} : Creates the game 
   specific routes tables inside either the default db or a user specified one.
   Tables will be named gamename_routename. Because some games are multi-region
   the table names are in the form of "blue_kanto_route_1". Requires a valid
   gamename. To see column names check tables-info.
3. pokedbmaker gamenames : lists all acceptable game names.
4. pokedbmaker custom_routes_from_csv {game_name} {dbname-optional}
