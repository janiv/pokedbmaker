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
3. Store these tables in either sqlite, or postgres.
4. Create a script that fixes some of the weird things that the PokeAPI will
   give as values. For example Magnemite is not a steel type until Gen 2.
