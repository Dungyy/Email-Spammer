import smtplib
import time
for i in range(20):
    time.sleep(.5)
# range=how many times / sleep=is in how long before sends another
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login("#enter your email", "#enter your password")
    server.sendmail("#enter your email",
                    "#enter the email your sending too",
                    "#enter the message you wanna send")
    server.quit()

# made by dungy