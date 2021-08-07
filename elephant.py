#!/usr/bin/env python

import os
import click
from dotenv import load_dotenv

load_dotenv()







@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Print more output.")
def main(verbose):
    """
    Get alerted each time a transaction is made on the Bitcoin blockchain that surpasses 1 Million Dollars.
    """
    API_KEY = os.getenv('API_KEY')

    click.secho("              ___.-~\"~-._   __....__" , fg = 'blue')
    click.secho("            .'    `    \ ~\"~        ``-.", fg = 'blue')
    click.secho("           /` _      )  `\              `\ ", fg = 'blue')
    click.secho("          /`  a)    /     |               `\ ", fg = 'blue')
    click.secho("         :`        /      |                 \ ", fg = 'blue')
    click.secho("    <`-._|`  .-.  (      /   .            `;\\\          _.-~\"~-.", fg = 'blue')
    click.secho("     `-. `--'_.'-.;\___/'   .      .       | \\\       ;`a)   )  `\ ", fg = 'blue')
    click.secho("  _     /:--`     |        /     /        .'  \\\     /      /    |~=-=--.", fg = 'blue')
    click.secho(" (\"\   /`/        |       '     '         /    ;`'._/ ,;_  |    /        \".", fg = 'blue')
    click.secho(" `\\\'\_/`/         .\     /`~`=-.:        /     ``.,__/ ` `| `\"~`           \ ", fg = 'blue')
    click.secho("   `._.'          /`\    |      `\      /(            .--'   /      /      |\ ", fg = 'blue')
    click.secho("                 /  /\   |        `Y   /  \          /  ____/\     |      / `\" ", fg = 'blue')
    click.secho("                J  /  Y  |         |  /`\  \        /__/  |  |`-...-\    |", fg = 'blue')
    click.secho("               /  |   |  |         |  |  |  |       '\"\"   |  |      |`\  |", fg = 'blue')
    click.secho("              \"---\"  /___|        /___|  /__|             /__|     /__/__|", fg = 'blue')
    click.secho("                     '\"\"\"         '\"\"\"  '\"\"\"              '\"\"\"    '\"\"\"'\"\"         ", fg = 'blue')
    click.secho(" _____ _         _           _      _        _   _          _____ _         _   " , bg='blue', fg='white')
    click.secho("|   __| |___ ___| |_ ___ ___| |_   |_|___   | |_| |_ ___   | __  | |___ ___| |_ ", bg='blue', fg='white')
    click.secho("|   __| | -_| . |   | .'|   |  _|  | |   |  |  _|   | -_|  | __ -| | . |  _| '_|", bg='blue', fg='white')
    click.secho("|_____|_|___|  _|_|_|__,|_|_|_|    |_|_|_|  |_| |_|_|___|  |_____|_|___|___|_,_|", bg='blue', fg='white')
    click.secho("            |_|                                                                 ", bg='blue', fg='white')
    click.secho("                                V 0.001",  fg='white')
    click.secho
    click.secho
    click.secho(f"Listening for Elephants {'in verbose mode' if verbose else ''} ..." , fg = 'white')









if __name__ == "__main__":
    main()