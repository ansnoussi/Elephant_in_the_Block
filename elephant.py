#!/usr/bin/env python

import os
import click
import requests
import datetime
import time
from dotenv import load_dotenv

load_dotenv()







@click.command()
@click.option('--verbose', '-v', is_flag=True, help="Print more output.")
@click.option('--ammount', default=1000000, help='Ammount in $ to listen for (default 1000000).')
def main(verbose,ammount):
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


    while(True):
        # get the current timestamp
        current_time = datetime.datetime.now().timestamp()
        current_time = int(current_time)

        # we are choosing intervals of 15s so we dont surpass the api limit
        # start_time = current_time - 15
        start_time = current_time - 15

        # turn them into a string
        start = str(start_time)
        end = str(current_time)

        response = requests.get(('https://api.whale-alert.io/v1/transactions?api_key='+API_KEY+'&start='+start+'&end='+end+'&currency=btc&min_value='+str(ammount)))
        json_r = response.json()
        count = json_r["count"]

        # if the count is not zero then get the transactions
        if(count != 0):
            transactions = json_r['transactions']
            
            for key in transactions:
                if key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'exchange':
                    if key['from']['owner'] == key['to']['owner']:
                        logOutput("🐘 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered on #' + key['from']['owner'].title())
                    else:
                        logOutput("🐘 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'unknown':
                    logOutput("🐘 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to ' + key['to']['owner_type'])
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'exchange':
                    logOutput("🐘 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'unknown':
                    logOutput("🐘 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to ' + key['to']['owner_type'])


        time.sleep(15)



def logOutput(post):
    print(post)





if __name__ == "__main__":
    main()