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
email_from = "akshaykc749@gmail.com"


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
email_list = ["anand@cyber-resource.com",
"anandm@vbeyond.com",
"anand.s@vdartinc.com",
"anand@codetech-inc.com",
"anand@reveilletechnologies.com",
"anandg@select-jarvis.com",
"ANANTH.GEJJI@experis.com",
"ananth@ebasetek.com",
"anantha@aroghia.com",
"ananu@vsoftconsulting.com",
"Andrea@i2usystems.com",
"andrew.g@tek-connexion.com",
"Andrew.Hunt@gvdsystem.com",
"andy@ms-info-tech.com",
"andy@americanunit.com",
"andy@kosheritgroup.com",
"ani@scelint.com",
"aniket.sharma@prismitcorp.com",
"aniket@akaasa.com",
"aniket@veracity-us.com",
"aniketsharma@sivisoft.com",
"anil@itvisiongroup.com",
"anil.pal@idctechnologies.com",
"anil.kumar@axiomglobal.com",
"anil.kumar@compunnel.com",
"anil.s@idctechnologies.com",
"anil.s@unicomtec.com",
"anil@quantumincs.com",
"anil@satyass.com",
"anil@sophusinfo.com",
"anilkumar@krgtech.com",
"Animesh.dey@nityo.com",
"anand@cyber-resource.com",
"anandm@vbeyond.com",
"anand.s@vdartinc.com",
"anand@codetech-inc.com",
"anand@reveilletechnologies.com",
"anandg@select-jarvis.com",
"ANANTH.GEJJI@experis.com",
"ananth@ebasetek.com",
"anantha@aroghia.com",
"ananu@vsoftconsulting.com",
"Andrea@i2usystems.com",
"andrew.g@tek-connexion.com",
"Andrew.Hunt@gvdsystem.com",
"andy@ms-info-tech.com",
"andy@americanunit.com",
"andy@kosheritgroup.com",
"ani@scelint.com",
"aniket.sharma@prismitcorp.com",
"aniket@akaasa.com",
"aniket@veracity-us.com",
"aniketsharma@sivisoft.com",
"anil@itvisiongroup.com",
"anil.pal@idctechnologies.com",
"anil.kumar@axiomglobal.com",
"anil.kumar@compunnel.com",
"anil.s@idctechnologies.com",
"anil.s@unicomtec.com",
"anil@quantumincs.com",
"anil@satyass.com",
"anil@sophusinfo.com",
"anilkumar@krgtech.com",
"Animesh.dey@nityo.com",
]

# Run the function with the updated email_list


pswd = "kzlgvmfzuggayfhd" 

# name the email subject
subject = "Job Inquiry for Full Stack Developer/ Java Developer/ Front end Developer Position"



# Define the email function (dont call it email!)
def send_emails(email_list, email_from, pswd):
    
    for person in email_list:
        try:


        # Make the body of the email
            body = f"""
Hello,

I hope this email finds you well. My name is Akshay Kumar.

With a 10+ background in the software industry, Throughout my career, I have demonstrated proficiency in Full Stack Development. I have attached my resume for your review. Please feel free to reach out to me if you require any additional information or if you would like to schedule an interview. I am available at 5395859198 or akshaykc749@gmail.com.

Thank you for considering my application. I look forward to the opportunity to discuss how my skills and experiences align with the needs. 

Work Authorization: GC, Looking for C2C roles.

Sincerely,
Akshay Kumar
+1 539 585 9198
akshaykc749@gmail.com
        """

        # make a MIME object to define parts of the email
            msg = MIMEMultipart()
            msg['From'] = email_from
            msg['To'] = person
            msg['Subject'] = subject

        # Attach the body of the message
            msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
            filename = "AkshayKumarChemuri_FSJD.docx"

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