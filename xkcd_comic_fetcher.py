import waveassist
waveassist.init()
import requests

response = requests.get('https://xkcd.com/info.0.json')
response.raise_for_status()
comic_data = response.json()

waveassist.store_data('comic_data', comic_data)