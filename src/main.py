#! /usr/bin/env python3

import requests

_URL_ = 'http://example.com/the/example/path/messages'
_API_KEY_ = 'Vmdhb1NzdUd0YUFKQnhwQmNVUnRVSUtOUUtjQmlDa1Q'


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
