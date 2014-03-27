import urllib2
import json
import random
import time

def domainr_search_json(domainname):
	requesturl = 'http://www.domai.nr/api/json/search?q='
	requesturl += domainname
	request = urllib2.Request(requesturl)
	request.add_header('User-Agent', 'domainr.py/0.1')
	opener = urllib2.build_opener()
	response = opener.open(request).read()
	objs = json.loads(response)
	return objs

def is_com_taken(domainr_json):
	return domainr_json['results'][0]['availability'] == 'taken'

def is_net_taken(domainr_json):
	return domainr_json['results'][1]['availability'] == 'taken'

def is_org_taken(domainr_json):
	return domainr_json['results'][2]['availability'] == 'taken'
text_file = open("/usr/share/dict/words","r")
words = text_file.read().split('\n')
while True:
	max = len(words)
	first = random.randint(0,max)
	second = random.randint(0,max)
	domainname = words[first]+words[second]
	print "Checking domain " + domainname + ".com" 
	test = domainr_search_json(domainname)
	answer = is_com_taken(test)
	print "Taken: " + str(answer)
	time.sleep(15)
