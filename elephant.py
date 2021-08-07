#!/usr/bin/env python

import os
import click
import requests
import datetime
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

    # this is a test

    # get the time in utc timestamp and make it an int not a float
    current_time = datetime.datetime.now().timestamp()
    current_time = int(current_time)

    # we are choosing intervals
    start_time = current_time - 3000

    # turn them into a string
    start = str(start_time)
    end = str(current_time)

    response = requests.get(('https://api.whale-alert.io/v1/transactions?api_key='+API_KEY+'&start='+start+'&end='+end+'&currency=btc&min_value='+str(ammount)))
    json_r = response.json()
    print(json_r)








if __name__ == "__main__":
    main()













import requests
import datetime
import tweepy
import config

def getTransactions():
    # get the time in utc timestamp and make it an int not a float
    ends = datetime.datetime.utcnow().timestamp()
    ends = int(ends)

    # take the valid start and end time
    starts = ends - 26000
    end = starts + 3600

    # turn them into a string
    start = str(starts)
    end = str(end)

    # get api from blockchain
    response = requests.get(('https://api.whale-alert.io/v1/transactions?api_key='+config.BLOCKCHAIN+'&min_value=1000000&start='+start+'&end='+end+'&cursor=2bc7e46-2bc7e46-5c66c0a7'))
    json_r = response.json()

    # get how many transaction within that certain time frame
    count = json_r["count"]
    
    # if the count is not zero then get the transactions
    if(count != 0):
        transactions = json_r['transactions']
        
        for key in transactions:
            if key['amount_usd'] >= 10000000:
                if key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'exchange':
                    if key['from']['owner'] == key['to']['owner']:
                        twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered on #' + key['from']['owner'].title())
                    else:
                        twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'unknown':
                    twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to ' + key['to']['owner_type'])
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'exchange':
                    twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'unknown':
                    twitter("🔺 " +str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to ' + key['to']['owner_type'])
            else:
                if key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'exchange':
                    if key['from']['owner'] == key['to']['owner']:
                        twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered on #' + key['from']['owner'].title())
                    else:
                        twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'exchange' and key['to']['owner_type'] == 'unknown':
                    twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from #' + key['from']['owner'].title() + ' to ' + key['to']['owner_type'])
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'exchange':
                    twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to #' + key['to']['owner'].title())
                elif key['from']['owner_type'] == 'unknown' and key['to']['owner_type'] == 'unknown':
                    twitter(str(int(key['amount']))+' #'+key['symbol'].upper() +' (' + str(int(key['amount_usd'])) + ' USD) Was transfered from ' + key['from']['owner_type'] + ' to ' + key['to']['owner_type'])

def twitter(post):
    # all the keys we need for our twitter bot
    CONSUMER_KEY = config.CONSUMERKEY
    CONSUMER_SECRET = config.CONSUMERSECRET
    ACCESS_KEY = config.ACCESSKEY
    ACCESS_SECRET = config.ACCESSSECRET

    # talk to twitter
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    api.update_status(post)
