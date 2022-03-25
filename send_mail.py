import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from templates import Template

# env variables
username = 'lucicardona630@gmail.com'
passwd = 'w7xtcg1a2b'

class Emailer():
     to_emails = []
     context={}
     subject = ''
     from_email = 'LACJ code <lucicardona630@gmail.com>'
     has_html = False
     template_html=None
     template_name=None
     
     def __init__(self, subject, template_name=None, context=None,
                  template_html=None, to_emails=None):
          if template_name == None and template_html == None:
               raise Exception("You must set a template")
          assert isinstance(to_emails,list)
          self.to_emails = to_emails
          self.subject=subject
          if template_html != None:
               self.has_html = True
               self.template_html = template_html
          self.template_name = template_name
          self.context = context

     def format_msg(self):
          msg = MIMEMultipart('alternative')
          msg['From'] = self.from_email
          msg['To'] = ", ".join(self.to_emails)
          msg['Subject'] = self.subject

          if self.template_name != None:
               tmpl_str = Template(template_name=self.template_name, context=self.context)
               txt_part = MIMEText(tmpl_str.render(), 'plain')
               msg.attach(txt_part)

          if self.template_html != None:
               tmpl_str = Template(template_name=self.template_html, context=self.context)
               
               html_part = MIMEText(tmpl_str.render(), 'html')
               msg.attach(html_part)

          msg_str = msg.as_string()
          return msg_str
     def send_mail(self):
          msg_str = self.format_msg()
          did_send=False
          with smtplib.SMTP(host='smtp.gmail.com', port = 587) as server:
               server.ehlo()
               server.starttls()
               server.login(username, passwd)
               try:
                    server.sendmail(self.from_email, self.to_emails, msg_str)
                    did_send=True
               except:
                    did_send=False

          return did_send

if __name__ == "__main__":
     import datetime
     time = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
     to_emails = ["lucicardona630@gmail.com"]

     e = Emailer(subject="Test", context={"nome":"Luciano", "data":time},
                 template_name="email_text.txt",
                 to_emails=to_emails,template_html="email_html.html")

     print(e.send_mail())
     
