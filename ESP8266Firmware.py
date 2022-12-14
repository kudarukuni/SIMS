import time
import serial
import smtplib

TO = 'krukuni@gmail.com'
GMAIL_USER = 'simsdata123@gmail.com'
GMAIL_PASS = 'simsdata$$321'
SUBJECT = 'Smart Inventory Management System Alert'
TEXT1 = 'Barcode Scan Alert !! To see more details go to http://www.sdts.com'
  
ser = serial.Serial('COM10', 115200)

def send_email():
    print("Sending Email")

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(GMAIL_USER, GMAIL_PASS)

    header = 'To:' + TO + '\n' + 'From: ' + GMAIL_USER
    header = header + '\n' + 'Subject:' + SUBJECT + '\n'

    print(header)

    msg = header + '\n' + TEXT1 + ' \n\n'

    smtpserver.sendmail(GMAIL_USER, TO, msg)
    smtpserver.close()
    
while True:
    message = ser.readline()
    string_n = message.decode()
    string = string_n.rstrip()
    print(string)
    
    if string:
        send_email()
    time.sleep(0.5)
