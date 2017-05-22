import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import sys

import config

import csv_reader

class SendMail():
	def __init__(self):
		print 'this is a basic cons'
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.server.starttls()
		try:
			self.server.login(config.GMAIL_USERNAME, config.GMAIL_PASSWORD)
		except:
			print """ 
				Error occurred!
				print 'Following may be the possible reasons'
				print '1. Wrong credentials'
				print '2. Enable less secure apps in your gmail settings 
			"""

	def sendMessage(self, sender_email, receiver_email, message_subject, message_body):
		sender_address = sender_email
		receiver_address = receiver_email
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = message_subject

		message_body = message_body
		message.attach(MIMEText(message_body, 'plain'))
		message_str = message.as_string()
		self.server.sendmail(sender_email, receiver_email, message_str)
		self.server.quit()



if __name__ == '__main__':
	message_subject = "NITK-Open Source Group"
	message_body = """
	I hope you people are doing well ! It's a right time to get started :)
	All of you are invited tomorrow at 8pm on the slack channel for our first discussion.
	Tomorrow we will be discussing the time suitable for all of us and some basic concepts and requirements.

	Slack channel : https://nitk-osg.slack.com
	Github : https://github.com/NITKOSG/

	Note ( Very Important!) : I have not sent the mails to you all manually :P i have created a python script to do so :)
	Link : https://github.com/NITKOSG/csv_to_gmail
	Do have a look !

	Invite your friends too if you want.

	I will be available today also on the slack channel upto 10 pm , so you are invited today itself :)
	"""
	csv_file_name = sys.argv[1]
	csv_reader_obj = csv_reader.CSV_READER_FOR_SLACK()
	user_email_list = csv_reader_obj.read_csv(csv_file_name)
	for email in user_email_list:
		mail = SendMail() 
		print 'sending mail to ' + email 
		mail.sendMessage(config.GMAIL_USERNAME, email, "NITK-OSG", message_body)
	

