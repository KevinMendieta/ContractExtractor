#@author: KevinMendieta
#libraries
from datetime import date, timedelta
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
		The text of the response (string)
	"""
	return requests.get(url, params = params).text

def sliceDate(start, finish):
	"""
	Calculate the mid date from two dates.
	Args:
		start: the first date.
		finish: the second date.
	Return:
		The middle date from two dates in python datetime.
	"""
	start = [int(x) for x in start.split("-")]
	finish = [int(x) for x in finish.split("-")]
	start = date(start[0], start[1], start[2])
	finish =  date(finish[0], finish[1], finish[2])
	return (start + (finish - start) / 2)

def extractContracts(start, finish):
	"""
	Extract the contracts from two dates, in case that the number of contracts became greater
	than 100 the dates get sliced by the middle, and re-calculate the contracts with the new
	dates.
	Args:
		start: the first date.
		finish: the second date.
	Return:
		The total of contracts between two dates.
	Global:
		url: The url to consume the web service.
		id: The id for consume the web service.
		calls: Number of calls for solve the problem.
	"""
	global url, id, calls
	data = getResponse(url, buildParams(id, start, finish))
	calls += 1
	if (data == '"Hay mÃ¡s de 100 resultados"'):
		middle = sliceDate(start, finish)
		middleBack = str(middle - timedelta(days = 1))
		middle = str(middle)
		return int(extractContracts(start, middleBack)) + int(extractContracts(middle, finish))
	else:
		return int(data)

def main():
	"""
	main function
	"""
	global start, finish, calls
	contracts = extractContracts(start, finish)
	print("Calculated: " + str(contracts) + " contracts from " + start + " to " + finish + " in: " + str(calls) + " call/s.")


main()
