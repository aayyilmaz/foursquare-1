import foursquare
import requests

# Construct the client object
client = foursquare.Foursquare(client_id='1LWQP2V0J1UHPUFTA3XNMW4XTIKTGYJDPJLBAKKRUPNMOVSQ',
                               client_secret='23FOSJGN3YRYDAKFMOWFISUFP5G5GATNQWEHX100RLNNB5UO', version='20170520')


v=client.venues.explore(params={'ll':"41.042497,29.000636"})
jv=client.venues.explore(params={'ll':"41.042497,29.000636"}).json()
print(jv)

print("hata kodu:", rg.raise_for_status(), rg.status_code)
