#!/usr/bin/python

import requests

print "using coindesk.com/api to get bitcoin api (updated every 1 min)"
print ""
r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print("1 BTC = " + r.json()['bpi']['USD']['rate'] + " USD")
