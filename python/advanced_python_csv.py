from python import advanced_python_regex
import csv

degrees, titles, emails, emails_count = advanced_python_regex.read_faculty_csv()

with open('python/emails.csv', 'w') as file:
	writer = csv.writer(file)
	for email in emails:
		writer.writerow([email])
