def send(name="Luciano", to_email=None):
     assert to_email != None
     msg = format_msg(name)

     #send the message
     try:
          send_mail(text=msg, to_emails=[to_email],html=None)
          send = True
     except:
          send = False

     return send


if __name__ == "__main__":
     from send_mail import send_mail
     from format_msg import *
     from read_xlsx import read
     df = read("usuarios.xlsx")
     to_emails = df["Email"]
     subject = "Só um teste"
     from_email = 'LACJ code <lucicardona630@gmail.com>'
     text = format_msg()

     try:
          send_mail(text, subject, from_email, to_emails)
          send = True
     except:
          send = False
     finally:
          print(send)
