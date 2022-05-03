# https://rl.se/com/wxajax2.py?what=genhist&maptime=2015-03-29%2015:15
import requests

r = requests.get("https://rl.se/com/wxajax2.py?what=genhist&maptime=2015-03-29%2015:15")
print(r.status_code)