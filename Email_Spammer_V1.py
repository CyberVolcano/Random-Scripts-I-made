#Basic Contact Info
import smtplib
users=[]
fromaddr=input('Sender:')
toaddr=input('Receiver:')
message=input('Message:')
password=input('Password:')

#add recipients
#non existant in V1

#inputs from user

numberofemails=input("How many emails would you like to be sent? ")

print("Please wait...")

a=int(numberofemails)+1

#Recipients



#email sending loop

for emailsent in range(1,a):
    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddr, message)
    server.quit()
    print (str(emailsent) + ' email sent to ' + toaddr)


#Email send results
total=str(emailsent)
print ('Total emails sent:' + total)
