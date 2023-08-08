import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Setup port number and server name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

# Set up the email lists
email_from = ""


# Define the function to read emails from .xlsx file
# def read_emails_from_excel(file_path):
#     try:
#         # Read the .xlsx file into a pandas DataFrame
#         df = pd.read_excel(file_path, engine='openpyxl')

#         # Assuming the emails are in a column named 'Email'
#         email_list = df['Email'].tolist()

#         # Remove any NaN values (if any) from the list
#         email_list = [email for email in email_list if pd.notnull(email)]

#         return email_list

#     except Exception as e:
#         print(f"Failed to read emails from the .xlsx file. Error: {str(e)}")
#         return []

# # ... Rest of your code ...

# # Path to the .xlsx file containing the emails
# xlsx_file_path = "file.xlsx"

# Read emails from the .xlsx file
email_list = [""]

# Run the function with the updated email_list


pswd = "" 

# name the email subject
subject = ""



# Define the email function (dont call it email!)
def send_emails(email_list, email_from, pswd):
    
    for person in email_list:
        try:


        # Make the body of the email
            body = f"""

        """

        # make a MIME object to define parts of the email
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg['Subject'] = subject

        # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
            filename = ""

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
            TIE_server = smtplib.SMTP(smtp_server, smtp_port, timeout=60)
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
send_emails(email_list, email_from, pswd)