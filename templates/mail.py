# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
# 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
# sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("alecross89@gmail.com")
to_email = Email("alecross89@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)