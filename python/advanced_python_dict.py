import csv
import collections
import re

def dict_q6():
	with open('python/faculty.csv') as file:
		reader = csv.reader(file, delimiter=',')
		next(reader, None)
		degrees = []
		titles = []
		emails = []
		profs = {}
		prof_title = 'Professor'
		for line in reader:
			key = line[0].split(' ')[-1]
			value = [line[1].strip(), line[2][:(line[2].find(prof_title) + len(prof_title))], line[3]]
			profs[key] = value
		
	return profs

def dict_q7():
	with open('python/faculty.csv') as file:
		reader = csv.reader(file, delimiter=',')
		next(reader, None)
		degrees = []
		titles = []
		emails = []
		profs = {}
		prof_title = 'Professor'
		for line in reader:
			name = line[0].split(' ')
			key = (' '.join(name[:-1]), name[-1])
			value = [line[1].strip(), line[2][:(line[2].find(prof_title) + len(prof_title))], line[3]]
			profs[key] = value
		
	return profs


def dict_q8():
	profs_dict = dict_q7()
	profs_ordered = collections.OrderedDict(sorted(profs_dict.items(), key=lambda t: t[0][1]))
	return profs_ordered