#!/usr/bin/python


#scraping this page: https://www.bitcoinblockhalf.com/  to get some information about bitcoin


from bs4 import BeautifulSoup
import requests
page_link ='https://www.bitcoinblockhalf.com/'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")

####################################################################################

#a faster way to scrape:
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

print (list(bitcoinInCirculation)[0].get_text() + list(bitcoinInCirculation)[1].get_text())
print (list(bitcoinToBeProduced)[0].get_text() + list(bitcoinToBeProduced)[1].get_text())
print (list(percentageOfBitcoinMined)[0].get_text() + list(percentageOfBitcoinMined)[1].get_text())
print (list(bitcoinLeftToMine)[0].get_text() + list(bitcoinLeftToMine)[1].get_text())
