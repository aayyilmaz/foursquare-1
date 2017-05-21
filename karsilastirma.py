#Returns a list of recommended venues near the current location.

import requests
import time
import csv

start_time = time.time()

client_id = "1LWQP2V0J1UHPUFTA3XNMW4XTIKTGYJDPJLBAKKRUPNMOVSQ"
client_secret = "23FOSJGN3YRYDAKFMOWFISUFP5G5GATNQWEHX100RLNNB5UO"
limit="50"
ll="41.042497,29.000636"
def_price="999"
v='20170430'

URL = "https://api.foursquare.com/v2/venues/explore?"
param = {'ll':ll, 'client_id': client_id, 'client_secret': client_secret, 'v': v, 'limit': limit}
print(param)
rg = requests.get(URL, params=param)  # auth=('user', 'pass')
print("rg:",rg)
rj=rg.json()
print("rj:",rj)