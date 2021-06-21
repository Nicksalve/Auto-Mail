#type this command in your teminal 'pip install secure-smtplib'
#go to your google account, go to security and turn on 'Less secure app access'
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('your email ID','Password')
server.sendmail('recivers email ID',
                'recivers email ID',
                input(“type your message”)
               )
