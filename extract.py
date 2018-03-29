#@author: KevinMendieta
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

def buildParams(id, start, finish):
	"""
	Build parameters for connection.
	Args:
		id: id parameter.
		start: the start date parameter.
		finish: the finish date parameter.
	Returns:
		a tuple with the parameters inside.
	"""
	return (
		("id", id),
		("start", start),
		("finish", finish)
	)

def getResponse(url, params):
	"""
	Get the response for the request to the Web Service.
	Args:
		url: URL for request.
		param: params for the Web Service consume.
	Return:
		The text of the response ()
	"""
	return requests.get(url, params = params).text

def main():
	"""
	main function
	"""
	global id, start, finish, url
	print(getResponse(url, buildParams(id, start, finish))


main()
