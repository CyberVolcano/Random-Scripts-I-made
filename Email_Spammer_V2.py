#Basic Contact Info
import smtplib
total_session = 0
users=[]
fromaddr=input('Sender:')
message=input('Message:')
password=input('Password:')
recent_users=[]

#add recipients

def contacts():
	users.append(input("Receiver:"))
	adduser = input("Would you like to add another recipient? 1 = yes , 2 = no ")
	if int(adduser) == 1:
		print('List of current recipients:' + str(users))
		contacts()
	else:
		print(users)

contacts()

#inputs from user

numberofemails=input("How many emails would you like to be sent? ")

print("Please wait...")

a=int(numberofemails)+1

#Recipients

#email sending loop

#entering server
server=smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(fromaddr, password)

#emailsending loop
for currentuser in users:
	for email_to_user in range(1,a):
		server.sendmail(fromaddr, currentuser, message)
		print (str(email_to_user) + ' email sent to ' + currentuser)
		total_session=total_session+1

#quit server
server.quit()

#add_users to recent

for currentuser in users:
	recent_users.append(currentuser)

#Email send results

print ('Total emails sent this session:' + str(total_session))
