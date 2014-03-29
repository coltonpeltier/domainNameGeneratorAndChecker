import urllib2
import json
import random
import time
import sys

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
if (sys.platform == "win32"):
	text_file = open("dictionary.txt","r")
else:
	text_file = open("/usr/share/dict/words","r")
words = text_file.read().split('\n')
while True:
	max = len(words)
	first = random.randint(0,max)
	second = random.randint(0,max)
	domainname = words[first].replace("'","")+words[second].replace("'","")
	print "Checking if " + domainname + " extensions are already registered:"
	rawJsonResults = domainr_search_json(domainname)
	dotComTaken = is_com_taken(rawJsonResults)
	dotOrgTaken = is_org_taken(rawJsonResults)
	dotNetTaken = is_net_taken(rawJsonResults)
	print "    .com:" + str(dotComTaken)
	print "    .net:" + str(dotNetTaken)
	print "    .org:" + str(dotOrgTaken)
	print " "
	time.sleep(15)
