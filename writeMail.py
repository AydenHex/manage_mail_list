import tkinter as tk
from tkinter import font
import sendMail
import tkinter.ttk as ttk
from tkinter import filedialog, simpledialog
import csv
from bs4 import BeautifulSoup
import requests, re
from email_validator import validate_email, EmailNotValidError


class writeMail(tk.Tk):
    '''
    Classe associé à l'interface de gestion des mailinglist
    '''

    def __init__(self, thismailist, parent):
        super().__init__()
        self.fontTitle = font.Font(family='Helvetica', size=28)
        self.fontCommun = font.Font(family='Helvetica', size=15)

        self._parent = parent
        self._listmail = thismailist
        self._mail = {
            'sender': tk.StringVar(),
            'object': tk.StringVar(),
            'mail': tk.StringVar(),
            'mailinglist': self._listmail
        }


        self.geometry("600x700")

        self.sender = tk.Label(self, text="Expéditeur :", font=self.fontCommun, justify='center')
        self.sender.place(x=100, y=50)

        self.senderInput = tk.Entry(self, textvariable=self._mail['sender'], font=self.fontCommun)
        self.senderInput.place(x=300, y=40)

        self.object = tk.Label(self, text="Objet :", font=self.fontCommun, justify='center')
        self.object.place(x=100, y=100)

        self.objectInput = tk.Entry(self, textvariable=self._mail['object'], font=self.fontCommun)
        self.objectInput.place(x=300, y=90)

        self.mailEdit = tk.Text(self)
        self.mailEdit.place(x=60, y=170, width=500)

        self.NextButton = tk.Button(self, text="Suite", font=self.fontCommun, command=lambda: self.next())
        self.NextButton.place(x=500, y=600)

        self.backButton = tk.Button(self, text="Retour", font=self.fontCommun, command=lambda: self.back())
        self.backButton.place(x=40, y=600)

    def next(self):
        self._mail['mail'] = self.mailEdit.get("1.0", "end-1c")
        self.withdraw()
        mySendMail = sendMail.sendMail(self._mail)
        mySendMail.mainloop()

    def back(self):
        self._parent.deiconify()
        self.destroy()

