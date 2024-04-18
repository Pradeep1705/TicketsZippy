from routes import app
import schedule
import time
from models.users_data import *
from models.tickets_data import *
# from datetime import datetime, timedelta
import datetime
from email.message import EmailMessage
import smtplib
import ssl
from dotenv import load_dotenv
import os

load_dotenv()
email_adress = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


def send_email(email, subject, message):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = email_adress
    msg['To'] = str(email)
    msg.set_content(message)

    print("inside send email", msg)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(email_adress, password)
        server.send_message(msg)

def daily_reminder():
    with app.app_context():
        users= User.query.all()
 
        for user in users:
            username = user.UserName
            email = user.Email
            log_in = loggedIn.query.filter_by(userName = user.UserName).one()
            cur_date = datetime.datetime.now().strftime('%Y-%m-%d')
            current_date = datetime.datetime.strptime(cur_date,'%Y-%m-%d').date()
            
            if datetime.datetime.now().day==11:
                monthly_report()
                continue  

            time_stamp = log_in.time
            dt_object = datetime.datetime.fromtimestamp(time_stamp) 
            date = dt_object.date()
            print(date)
            print(current_date)
            print(type(date))
            print(type(current_date))
            print(bool(date!=current_date), user.UserName)
            if date != current_date:
                body=f"Hello {username},\n\nThis is a friendly reminder that you haven't booked any ticket(s) within the last 24 hours.\n\nPlease visit out application.\n\nThank you,\nThe Ticketing Team"
                send_email(email,"Daily Reminder",body)
                print("mail sent")         
            
                       
            

def monthly_report():
    with app.app_context():
        users = User.query.all()
        cur = datetime.datetime.now()
        print('inside monthly report')
        for user in users:
            username = user.UserName
            email = user.Email
            ticket = Ticket.query.filter_by(userName = user.UserName ).all()
            
            ticket_booked = 0
            length = len(ticket)
            print(type(length))
            for i in range(len(ticket)):    
                ticket_booked +=1
                
                
            body=f"Hello {username},\n\nThis is your monthly report that you have booked  ticket(s) for {ticket_booked} movies in the last month.\n\nPlease review your recent bookings.\n\nThank you,\nThe Ticketing Team"
            send_email(email,"Daily Reminder",body)
            print("mail sent")

def Scheduled():

    schedule.every().day.at("20:40").do(daily_reminder)

    while True:
        schedule.run_pending()
        time.sleep(2)