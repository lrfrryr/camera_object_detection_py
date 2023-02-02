import smtplib
from email.message import EmailMessage
import imghdr

PASSWORD = "fdfohpsgcqadocyp"
SENDER = "pythonlara23@gmail.com"
RECEIVER = "pythonlara23@gmail.com"


def send_email(image_to_send):
    print("Send email function started")
    with open(image_to_send, "rb") as file:
        image_content = file.read()

    email_message = EmailMessage()
    email_message["Subject"] = "Unidentified object appeared on camera!"
    email_message.set_content("Hey, you may wanna check this out.")
    email_message.add_attachment(image_content, maintype="image", subtype=imghdr.what(None, image_content))

    # create email server to send email
    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("send email function ended")


if __name__ == "__main__":
    send_email(image_to_send="images/19.png")


