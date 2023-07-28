import unittest
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# Import the function you want to test
from emailSending import send_emails

class TestEmailSendingFunction(unittest.TestCase):
    # Replace the values with your own test email and password
    test_email_from = "youremail@gmail.com"
    test_pswd = "your password"

    # Define the email list
    email_list = [	
        "youremail@gmail.com","youremail@gmail.com","youremail@gmail.com","youremail@gmail.com"	
    ]

    def test_email_sending(self):
        # Run the email sending function with the test email and password
        try:
            send_emails(self.email_list, self.test_email_from, self.test_pswd)
        except smtplib.SMTPException as e:
            self.fail(f"Failed to send email. Error: {str(e)}")

    def test_invalid_email_list(self):
        # Test the function with an empty email list
        empty_email_list = []
        with self.assertRaises(smtplib.SMTPRecipientsRefused):
            send_emails(empty_email_list, self.test_email_from, self.test_pswd)

        # Test the function with an email list containing an invalid email address
        invalid_email_list = ["invalid_email", "test@example.com"]
        with self.assertRaises(smtplib.SMTPRecipientsRefused):
            send_emails(invalid_email_list, self.test_email_from, self.test_pswd)

    def test_attachment_existence(self):
        # Test if the function successfully attaches the resume file
        for person in self.email_list:
            try:
                # Make sure the attachment is included in the email
                send_emails(self.email_list, self.test_email_from, self.test_pswd)
                self.assertTrue("attachment" in send_emails(self.email_list, self.test_email_from, self.test_pswd))

                # Make sure the attachment is of the correct file type (PDF)
                self.assertTrue(".pdf" in send_emails(self.email_list, self.test_email_from, self.test_pswd))
            except Exception as e:
                self.fail(f"Failed to send email to {person}. Error: {str(e)}")

if __name__ == "__main__":
    unittest.main()
