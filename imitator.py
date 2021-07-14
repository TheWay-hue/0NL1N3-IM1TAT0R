import requests
import random
import time
sitesList = []
print('''
[ 0NL1N3 IMITATOR ]
    by C.A.S\n''')
with open('sites.txt','r') as handle:
	sites = handle.readlines()
	for x in sites:
		site = x.rstrip()
		sitesList.append(site)
try:
	while True:
		random.shuffle(sitesList)
		for site in sitesList:
			try:
				x = random.randint(0, 11)
				time.sleep(x)
				req = requests.get(f'http://{site}')
				if req.status_code == 200:
					print('\033[4m\033[32m{}\033[0m'.format(f'Status => {req} | Site => {site} | Timeout: {x} Message => OK'))
				elif req.status_code == 429:
					print('\033[4m\033[33m{}\033[0m'.format(f'Status => {req} | Site => {site} | Timeout: {x} Message => Rate Limit'))
				elif req.status_code == 403:
					print('\033[4m\033[33m{}\033[0m'.format(f'Status => {req} | Site => {site} | Timeout: {x} Message => Automation detected'))
				elif req.status_code == 503:
					print('\033[4m\033[36m{}\033[0m'.format(f'Status => {req} | Site => {site} | Timeout: {x} Message => Site not available yet'))
			except requests.exceptions.ConnectionError:
				print("\033[4m\033[31m{}\033[0m" .format(f'Status => <Response [???]> | Site => {site} | Timeout: {x} Message: Access error'))
except KeyboardInterrupt:
	print('\033[4m\033[35m{}\033[0m'.format('\nGoodby!'))