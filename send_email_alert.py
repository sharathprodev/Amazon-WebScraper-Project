# sending yourself an email when a price hits below a certain level you can try it out

def send_mail():
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('sharathprodev@gmail.com','xxxxxxxxxxxxxx')
    
    subject = "The Item you want is below $xx! Now is your chance to buy!"
    body = "Sharath, This is the moment we have been waiting for. Link here: url"
   
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'sharathprodev@gmail.com',
        msg
     
    )