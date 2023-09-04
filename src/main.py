#! /usr/bin/env python3

import requests

_URL_ = 'http://example.com/the/example/path/messages'
API_KEY = 'Vmdhb1NzdUd0YUFKQnhwQmNVUnRVSUtOUUtjQmlDa1Q'
# password = "this-is()hard_pass"

def main():
	h = {
		'APIKEY', _API_KEY_
	}

	r = requests.get(_URL_, headers=h)

	if r.status_code == 200:
		print(r.text)

	else:
		print('API down!')

if __main__ == '__main__':
	main()
