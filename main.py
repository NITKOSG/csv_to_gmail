import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

import config

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
	mail = SendMail() 
	mail.sendMessage(config.GMAIL_USERNAME, 'abhishekg785@gmail.com', "NITK_OSG","hii this is a testing mail :)")
	

