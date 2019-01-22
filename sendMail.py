import tkinter as tk
from tkinter import font
import mail1
import tkinter.ttk as ttk
from tkinter import filedialog, simpledialog
import csv
from bs4 import BeautifulSoup
import requests, re
from email_validator import validate_email, EmailNotValidError


class sendMail(tk.Tk):
    '''
    Classe associé à l'interface de gestion des mailinglist
    '''

    def __init__(self, mail):
        super().__init__()
        self.fontTitle = font.Font(family='Helvetica', size=28)
        self.fontCommun = font.Font(family='Helvetica', size=15)

        self._mail = mail


        self.geometry("600x350")

        self.mailTest = tk.Label(self, text="Mail d'essai : ", font=self.fontCommun, justify='center')
        self.mailTest.place(x=70, y=50)

        self.mailTestInput = tk.Entry(self, font=self.fontCommun)
        self.mailTestInput.place(x=270, y=50)

        self.mailTestButton = tk.Button(self, text="Envoyer un mail", font=self.fontCommun, command=lambda: self.sendMailTest())
        self.mailTestButton.place(x=200, y=150)

        self.SendButton = tk.Button(self, text="Envoyer à toute la mailinglist", font=self.fontCommun, command=lambda: self.sendMail())
        self.SendButton.place(x=150, y=300)


    def sendMailTest(self):
        print(self._mail['mailinglist'])
        pass

    def sendMail(self):
        pass