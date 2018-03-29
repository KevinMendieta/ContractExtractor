#author: KevinMendieta
#libraries
from datetime import date
import requests
import math

#connection parameters
url = "http://34.209.24.195/facturas"
id = "4e25ce61-e6e2-457a-89f7-116404990967"
#consts
start = "2017-01-01"
finish = "2017-12-31"
calls = 0

def main():
	global id, start, finish, url
	params = (
		("id", id),
		("start", start),
		("finish", finish)
	)
	print(requests.get(url, params = params).text)


main()
