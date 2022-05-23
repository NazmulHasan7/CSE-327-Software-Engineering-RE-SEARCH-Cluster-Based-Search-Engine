import smtplib
import os

def send(mail):
    gmail_user = os.environ.get('email')
    gmail_password = os.environ.get('mail_pass')

    sent_from = gmail_user
    to = [mail]
    subject = 'Cluster ready'
    body = 'your recent added url is ready for search'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as ex:
        print("Something went wrong….", ex)


# import smtplib
# import os


# email = os.environ.get('email')
# password = os.environ.get('mail_pass')
# print(password)
# # print(email)
# with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login(email, password)
#     subject= 'cluster is ready'
#     body= 'you can search now'
#     msg = f'Subject: {subject}: \n\n{body}'

#     smtp.sendmail(email, 'hasan104710@gmail.com', msg)
