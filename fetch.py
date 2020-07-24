import requests
import urllib.parse
import webbrowser

import pprint

pp = pprint.PrettyPrinter(indent=2)

# @TODO: get this from user input
USER = input('Enter GitHub Username: ')
ENDPOINT = f"https://api.github.com/users/{USER}/repos?sort=pushed"

response = requests.get(ENDPOINT)
result = response.json()[0]

print(result['url'])
webbrowser.open(result['svn_url'])
