import click
from pokedex_creator import *

@click.group()
def cli():
    click.echo(f"This is a click group to handle creating a pokemon database")


@click.command()
@click.option('--dbname', 
              prompt='Enter database name, program will create a new one if it does not exist',
              type=click.STRING,
              help="Check your spelling")
@click.option('--gen', prompt='Enter pokemon Generation 1-6', help='Enter number from 1-6 to choose a generation of pokemon')
def command_create_dex(dbname,gen):
    print("This is the test function")
    print(f"You want to use database: {dbname}.db")
    print(f"You want to generate a pokedex for Generation {gen}")

@click.command()
@click.option('--gen', prompt='Enter pokedex gen', help='Enter a number 1-6')
@click.option('--dexnum', prompt='Enter pokedex id of pokemon to look up', help='Gen 1 ranges from 1-151, Gen 2 ranges from 1-251')
def command_lookup_by_dex_id(gen, dexnum):
    print(f"Looking up {dexnum} in {gen} dex")


@click.command()
@click.option('--game', prompt="Enter game name", type=click.STRING, help='Use pokedmaker games for list of games')
@click.option('--dbname', prompt="Enter dbname", type=click.STRING, help="Check spelling")
@click.option('--gen', prompt="Enter gen as number between 1-6", type=click.INT, help="Enter a number")
def command_create_routes_list(dbname, gen, game):
    print(f"Creating {game} routes list using {gen} dex and db: {dbname}")

cli.add_command(command_create_dex)
cli.add_command(command_lookup_by_dex_id)
cli.add_command(command_create_routes_list)