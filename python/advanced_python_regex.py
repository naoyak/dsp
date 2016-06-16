import csv
import collections
import re

def read_faculty_csv():
	with open('python/faculty.csv') as file:
		reader = csv.reader(file, delimiter=',')
		next(reader, None)
		degrees = []
		titles = []
		emails = []
		prof_title = 'Professor'
		for line in reader:
			degrees.extend(line[1].split())
			titles.append(line[2][:(line[2].find(prof_title) + len(prof_title))])
			emails.append(line[3])
		degrees = [x.replace('.', '') for x in degrees]
		degree_counts = collections.Counter(degrees)
		title_counts = collections.Counter(titles)
		email_domains = set([re.search('@.*', email).group()[1:] for email in emails])
	return degree_counts, title_counts, emails, email_domains

read_faculty_csv()