import smtplib
import time
for i in range(3):
    time.sleep(.5)
# range=how many times / sleep=is in how long before sends another
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    server.login("hacker.dungy@gmail.com", "dungyM0217!")
    server.sendmail("dungy_hacker@gmail.com",
                    "erick_m-17@hotmail.com",
                    "YOURE ACCOUNT IS BEING HACKED\n""HAHAHAHAHA\n""GOOD GAME")
    server.quit()

# made by dungy