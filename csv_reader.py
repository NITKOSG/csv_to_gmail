import csv
import sys

# this one is for slack ! however it can be customized
class CSV_READER_FOR_SLACK:

	def __init__(self):
		print 'this is a simple csv reader'

	def read_csv(self, name):
		email_arr = []
		email_index = 1 #email index in each row of the csv file
		rownum = 0 # check for the current row
		with open(name, 'rb') as f:
			reader = csv.reader(f)
			for row in reader:
				if rownum == 0: # for header
					header = row
				else:
					email = row[email_index]  # for slack, the row[1] gives the email in the row array of csv file
					email_arr.append(email)
				rownum = rownum + 1
		return email_arr


#works fine! yay!
if __name__ == '__main__':
	csv_file_name = sys.argv[1]
	obj = CSV_READER_FOR_SLACK()
	user_email_arr = obj.read_csv(csv_file_name)
	print user_email_arr