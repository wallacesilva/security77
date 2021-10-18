import sys

import click

from security77.passgen import generate_random_password

# Required python 3.8+
if sys.version_info[0] < 3 and sys.version_info[1] < 8:
    raise Exception("Python 3.8+ required, sorry")

@click.group()
def cli():
    pass

@cli.command("passgen")
def cli_passgen():
    click.echo("Password Generated: " + generate_random_password())