import tkinter as tk
from tkinter import font
import smtplib
from email.mime.text import MIMEText


class sendMail(tk.Tk):
    '''
    Classe associé à l'interface de gestion des mailinglist
    '''

    def __init__(self, mail):
        super().__init__()
        self.fontTitle = font.Font(family='Helvetica', size=28)
        self.fontCommun = font.Font(family='Helvetica', size=15)

        self._mail = mail

        self._testmail = tk.StringVar()

        self.geometry("600x350")

        self.mailTest = tk.Label(self, text="Mail d'essai : ", font=self.fontCommun, justify='center')
        self.mailTest.place(x=70, y=50)

        self.mailTestInput = tk.Entry(self, font=self.fontCommun, textvariable=self._testmail)
        self.mailTestInput.place(x=270, y=50)

        self.mailTestButton = tk.Button(self, text="Envoyer un mail", font=self.fontCommun, command=lambda: self.sendMailTest())
        self.mailTestButton.place(x=200, y=150)

        self.SendButton = tk.Button(self, text="Envoyer à toute la mailinglist", font=self.fontCommun, command=lambda: self.sendMail())
        self.SendButton.place(x=150, y=300)


    def sendMailTest(self):
        s = smtplib.SMTP('smtp.gmail.com')
        s.set_debuglevel(1)
        msg = MIMEText("""body""")
        sender = 'quentin.mailtest2@gmail.com'
        recipients = [self._testmail.get()]
        msg['Subject'] = self._mail['object']
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        s.sendmail(sender, recipients, msg.as_string())

    def sendMail(self):
        s = smtplib.SMTP('smtp.gmail.com')
        s.set_debuglevel(1)
        msg = MIMEText("""body""")
        sender = 'quentin.mailtest2@gmail.com'
        recipients = [self._mail['mailinglist']]
        msg['Subject'] = self._mail['object']
        msg['From'] = sender
        msg['To'] = ", ".join(recipients)
        s.sendmail(sender, recipients, msg.as_string())
