import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "franciscoalberto.bautista.fp@iescampanillas.com"
    password = "pjxr mnnt gfmo nmzv"

    receiver = "franciscoalberto.bautista.fp@iescampanillas.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)