import smbplit
from email.message import EmailMessage
from pathlib import Path
# Email account credentials
EMAIL_ADDRESS = "your_email@example.com"
EMAIL_PASSWORD ="your password"

# File paths
RECIPIENT_FILE = "text.txt"
ATTACHMENT_PATH = "your_attachment.pdf"

def load_emails(filename):
    """load email addresses from a text file"""
    with open(filename, 'r') as file:
     return [line.strip() for line in file if line.strip]

def send_email(to_address):
    """send an email with an attachment to a single address"""
    msg =EmailMessage()
    msg['from'] =  EMAIL_ADDRESS
    msg['to'] = to_address
    msg['subject'] = "this is a test"

     #email content
    msg.set_content("""
    Hello "this is a test
    """)
    
    
    #add a file attachment
    with open(ATTACHMENT_PATH, 'rib') as attachment_file:
        file data = attachment_file.read()
        file_name =Path(ATTACHMENT_PATH).name
        msg.add_attachment(file_data, maintype='application', subtype='pdf',file):
        
    
    #send email
    try:
         with smtplib.SMTP_SSL ('smtp.exemple.com' ,465) as smtp
              smtp.send_message(msg)
              print(f"email sent to {to_address}")
         except Exception as e:
            print(f"Failed to send email to {to_address}: {e}")
            
            
     if __name__=="__main__":
          addresses =load_emails("text.txt")
          for email in addresses:
          send_email(email)