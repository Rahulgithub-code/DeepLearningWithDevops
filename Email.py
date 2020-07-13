import smtplib
sender="rahulkr.demo@gmail.com"
race="rahulkr.mits@gmail.com"
#password=input("Enter password :")
password="9905350054"
msg="Accuracy reached above 90%"
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.starttls()
mail.login(sender,password)
print("access granted")
mail.sendmail(sender,race,msg)
print("everything is okay")
mail.close()
