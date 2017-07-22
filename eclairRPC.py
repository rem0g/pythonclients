import requests
import json
import argparse

#Adjust when needed
url = "http://localhost:8081"

parser = argparse.ArgumentParser(description='Dumb RPC caller to Eclair.')
parser.add_argument('cmds', metavar='Usage: help / getinfo / and more...', nargs='+', help='Type help to get list of commands')
headers = {'content-type': 'application/json'}

args = parser.parse_args()
out = []
for x in args.cmds[1:]:
	if x.isdigit():
	   out.append(int(x))
	else:
	   out.append(x)

payload = {
    "method": args.cmds[0],
    "params": out,
    "jsonrpc": "2.0",
    "id": 0,
}

print(requests.post(url, data=json.dumps(payload), headers=headers).json())
