#!/usr/bin/python


#scraping this page: https://www.bitcoinblockhalf.com/  to get some information about bitcoin



from bs4 import BeautifulSoup
import requests
page_link ='https://www.bitcoinblockhalf.com/'
# fetch the content from url
page_response = requests.get(page_link, timeout=5)
# parse html
page_content = BeautifulSoup(page_response.content, "html.parser")


info = page_content.find_all('table', attrs={'class':'table table-striped'})

print(info)
