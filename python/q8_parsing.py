# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
def smallest_gd_team():
	import csv
	with open('python/football.csv') as csvfile:
		fbreader = csv.reader(csvfile, delimiter=',')
		next(fbreader, None)
		gd_sorted = sorted(fbreader, key=lambda row: abs(int(row[5])-int(row[6])))
		print(gd_sorted[0][0])
