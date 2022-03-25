from datetime import datetime

def format_msg(name = "Luciano"):
     data = datetime.now().strftime("%m/%d/%Y, %H horas, %M minutos e %S segundos")
     file = open("templates/email_text.txt", "r")
     my_msg = file.read().format(nome=name, data = data)

     return my_msg

if __name__ == "__main__":
     format_msg()
