#type in terminal 'pip install secure-smtplib'
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ayush.tech100@gmail.com','ayush.techsavy')
server.sendmail('ayush.tech100@gmail.com',
               'ayush.tech100@gmail.com',
               input(“type your message”)
               )
