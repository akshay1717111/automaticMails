
#install python before you run this code

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

#enter your email address
email_from = "youremail@gmail.com"

# Set up the email lists
email_list = [	
"emaillist@gmaill.com",	
"typeypuremails@overhere.com"
"enteremail@gmail.com"	
]
pswd = "your password" 
#here password is not your email password it is generated using google setting
#below steps to enable app password in gmail account
#go to the google account setting next go to security tab
#after that enable 2-step Verification  and make sure to on it.
# after in the search bar please enter app password
#create a custom name to and click on generate then you can see password as abcd abcd abcd abcd
#enter this password in the pswd variable.

# name the email subject
subject = "subject line"



# Define the email function (dont call it email!)
def send_emails(email_list):

    for person in email_list:
        try:


        # Make the body of the email
            body = f"""
Hello,

Type your body over here
        """

        # make a MIME object to define parts of the email
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg['Subject'] = subject

        # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
            filename = "Resume.pdf"

        # Open the file in python as a binary
            attachment= open(filename, 'rb')  # r for read and b for binary

        # Encode as base 64
            attachment_package = MIMEBase('application', 'octet-stream')
            attachment_package.set_payload((attachment).read())
            encoders.encode_base64(attachment_package)
            attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
            msg.attach(attachment_package)

        # Cast as string
            text = msg.as_string()

            # Connect with the server
            print("Connecting to server...")
            TIE_server = smtplib.SMTP(smtp_server, smtp_port)
            TIE_server.starttls()
            TIE_server.login(email_from, pswd)
            print("Successfully connected to server")
            print()

            # Send emails to "person" as list is iterated
            print(f"Sending email to: {person}...")
            TIE_server.sendmail(email_from, person, text)
            print(f"Email sent to: {person}")
            print()

            # Close the connection
            TIE_server.quit()

        except Exception as e:
            print(f"Failed to send email to {person}. Error: {str(e)}")
            print()

# Run the function
send_emails(email_list)




        




