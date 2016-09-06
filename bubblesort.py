from datetime import datetime
import random
def bubbleSort(listvar):
	timeStart = datetime.now()
	print listvar
	crawlLimit = len(listvar)-1
	print 'crawlLimit = '+str(crawlLimit)
	idx = 0
	while crawlLimit != 0:
		while idx < crawlLimit:
			if listvar[idx] > listvar[idx+1]:
				listvar[idx], listvar[idx+1] = listvar[idx+1], listvar[idx]
				#print listvar
				idx += 1
			else:
				#print listvar
				idx += 1
		crawlLimit -= 1
		idx = 0
		print str(idx)+' '+str(crawlLimit)
	timeEnd = datetime.now()
	print listvar
	print timeEnd-timeStart

def sorter(listvar):
	timeStart = datetime.now()
	print timeStart
	print listvar
	crawlLimit = len(listvar)-1
	idx = 0
	while crawlLimit != 0:
		while idx < crawlLimit:
			if listvar[idx]>listvar[crawlLimit]:
				listvar[idx],listvar[crawlLimit]=listvar[crawlLimit],listvar[idx]
				idx += 1
			else:
				idx += 1
		crawlLimit -= 1
		idx = 0
	timeEnd = datetime.now()
	print timeEnd
	print listvar
	print timeEnd-timeStart

def generate100():
	idx = 0
	mylist = []
	while idx < 100:
		mylist.append(random.randrange(10001))
		idx += 1
	return mylist

def generate10():
	idx = 0
	mylist = []
	while idx < 10:
		mylist.append(random.randrange(101))
		idx += 1
	return mylist

def generate(amount):
	idx = 0
	mylist = []
	while idx < amount:
		mylist.append(random.randrange(10001))
		idx += 1
	return mylist


