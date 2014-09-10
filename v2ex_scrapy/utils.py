import requests
from settings import DB

def topic_max():

	return requests.get('http://v2ex.com/api/topics/latest.json').json()[0]['id']

def maxid_local(collection):

	return DB[collection].find().sort("_id", -1).limit(1)[0]['_id']

if __name__ == '__main__':
	
	print(topic_max())
	print(maxid_local('member'))
