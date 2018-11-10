#!/usr/bin/python

import click
import requests
from bs4 import BeautifulSoup


@click.command()

def main():
    click.secho("              ___.-~\"~-._   __....__" , fg = 'blue')
    click.secho("            .'    `    \ ~\"~        ``-.", fg = 'blue')
    click.secho("           /` _      )  `\              `\ ", fg = 'blue')
    click.secho("          /`  a)    /     |               `\ ", fg = 'blue')
    click.secho("         :`        /      |                 \ ", fg = 'blue')
    click.secho("    <`-._|`  .-.  (      /   .            `;\\          _.-~\"~-.", fg = 'blue')
    click.secho("     `-. `--'_.'-.;\___/'   .      .       | \\       ;`a)   )  `\ ", fg = 'blue')
    click.secho("  _     /:--`     |        /     /        .'  \\     /      /    |~=-=--.", fg = 'blue')
    click.secho(" (\"\   /`/        |       '     '         /    ;`'._/ ,;_  |    /        \".", fg = 'blue')
    click.secho(" `\'\_/`/         .\     /`~`=-.:        /     ``.,__/ ` `| `\"~`           \ ", fg = 'blue')
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


    click.secho("fetching Bitcoin price from coindesk.com ..." , fg = 'white')
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    price = r.json()['bpi']['USD']['rate']
    click.secho("1 BTC = " + price + " USD", fg = 'red')
    bitcoinBlockHalf()

def bitcoinBlockHalf():
    click.secho("scraping information from bitcoinblockhalf.com ..." , fg = 'white')

    page_link ='https://www.bitcoinblockhalf.com/'
    # fetch the content from url
    page_response = requests.get(page_link, timeout=5)
    # parse html
    page_content = BeautifulSoup(page_response.content, "html.parser")

    ####################################################################################

    #a faster way to scrape the table:
    #info_table = page_content.find_all('table', attrs={'class':'table table-striped'})

    ####################################################################################


    #another more complicated way but more organized
    html_content = list(page_content.children)[4]
    body_content = list(html_content.children)[3]
    container_content = list(body_content.children)[1]
    table_content = list(container_content.children)[9]

    #the content I'm more interested in:
    bitcoinInCirculation = list(table_content.children)[1]
    bitcoinToBeProduced = list(table_content.children)[3]
    percentageOfBitcoinMined = list(table_content.children)[5]
    bitcoinLeftToMine = list(table_content.children)[7]

    click.secho (list(bitcoinInCirculation)[0].get_text() + list(bitcoinInCirculation)[1].get_text(), fg = 'red')
    click.secho (list(bitcoinToBeProduced)[0].get_text() + list(bitcoinToBeProduced)[1].get_text(), fg = 'red')
    click.secho (list(percentageOfBitcoinMined)[0].get_text() + list(percentageOfBitcoinMined)[1].get_text(), fg = 'red')
    click.secho (list(bitcoinLeftToMine)[0].get_text() + list(bitcoinLeftToMine)[1].get_text(), fg = 'red')



if __name__ == "__main__":
    main()
