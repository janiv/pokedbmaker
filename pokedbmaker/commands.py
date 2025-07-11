import click
from pokedex_creator import *


@click.command()
@click.option('--dbname', prompt='Enter database name, program will create a new one if it does not exist', help="Check your spelling")
@click.option('--gen', prompt='Enter pokemon Generation 1-6', help='Enter number from 1-6 to choose a generation of pokemon')
def command_create_dex(dbname,gen):
    print("This is the test function")
    print(f"You want to use database: {dbname}.db")
    print(f"You want to generate a pokedex for Generation {gen}")

@click.command()
@click.option('--')
@click.option('--dexnum', prompt='Enter pokedex id of pokemon to look up', help='Gen 1 ranges from 1-151, Gen 2 ranges from 1-251')
def command_lookup_by_dex_id(gen, dexnum):
    print(f"Looking up {dexnum} in {gen} dex")