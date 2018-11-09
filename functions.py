#!/usr/bin/python

#testing Plaintext query api found at : https://www.blockchain.com/api/q


import requests

print("the following is an important list of thing to know about Bitcoin:")
print ""


print ("Hash of the latest block")
r = requests.get("https://blockchain.info/q/latesthash")
print (r.text)

print ("Current block reward in BTC :")
r = requests.get("https://blockchain.info/q/bcperblock")
print (float(r.text)/100000000)

print ("Total Bitcoins in circulation (delayed by up to 1 hour]): ")
r = requests.get("https://blockchain.info/q/totalbc")
print (float(r.text)/100000000)

print("Probability of finding a valid block each hash attempt")
r = requests.get("https://blockchain.info/q/probability")
print (r.text)
