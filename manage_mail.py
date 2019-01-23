import csv
import requests
import re

import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import simpledialog

from bs4 import BeautifulSoup
from email_validator import validate_email
from email_validator import EmailNotValidError

import writeMail


class manageMail(tk.Tk):

    def __init__(self, thismailist, parent):
        super().__init__()
        self.fontTitle = font.Font(family='Helvetica', size=28)
        self.fontCommun = font.Font(family='Helvetica', size=15)

        self._parent = parent
        self._listmail = thismailist

        self.geometry("500x600")

        self.dedupeButton = tk.Button(self, text="Dédoublouner", font=self.fontCommun, command=lambda: self.dedupe())
        self.dedupeButton.place(x=45, y=50)

        self.AvailableButton = tk.Button(self, text="Test de la Mailist", font=self.fontCommun, command=lambda: self.validityMail())
        self.AvailableButton.place(x=280, y=50)

        self.CSVButton = tk.Button(self, text="CSV", font=self.fontCommun, command=lambda: self.loadCsv())
        self.CSVButton.place(x=85, y=110)

        self.LinkButton = tk.Button(self, text="URL", font=self.fontCommun, command=lambda: self.crawlMail())
        self.LinkButton.place(x=330, y=110)

        self.deleteButton = tk.Button(self, text="Delete not valide mail", font=self.fontCommun, command=lambda: self.deleteNotValide())
        self.deleteButton.place(x=330, y=110)

        self.nextButton = tk.Button(self, text="Suite", font=self.fontCommun, command=lambda: self.next())
        self.nextButton.place(x=400, y=500)

        self.backButton = tk.Button(self, text="Retour", font=self.fontCommun, command=lambda: self.back())
        self.backButton.place(x=40, y=500)

        self.tv = ttk.Treeview(self)
        self.tv['columns'] = ('validity')
        self.tv.heading("#0", text='Email')
        self.tv.column("#0", width=300)
        self.tv.heading('validity', text='Validité')
        self.tv.column('validity', anchor='center', width=100)

        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.vsb.place(x=50 + 400 + 2, y=200, height=200 + 20)

        self.tv.configure(yscrollcommand=self.vsb.set)

        self.tv.place(x=50, y=200)

        # Je charge en mémoire les mails si le fichier est existant
        self.reloadMail()

    def reloadMail(self):
        self.tv.delete(*self.tv.get_children())
        for mail in self._listmail:
            self.tv.insert("", 'end', text=mail, values=('~'))

    def loadCsv(self):
        csv_filechooser = tk.filedialog.askopenfile(title='Choisir le csv', filetypes=[("CSV files","*.csv")])
        myFile = csv_filechooser.name
        with open(myFile, 'r') as myCsv:
            spamreader = csv.reader(myCsv, delimiter=',', quotechar='|')
            for row in spamreader:
                mail = re.sub(r"[]'[]", "", row[0])
                self._listmail.append(mail)
        self.reloadMail()

    def crawlMail(self):
        myUrl = tk.simpledialog.askstring(title="Choisisez une url", prompt="Adresse url à crawler", parent=self)
        plainPage = requests.get(myUrl).text
        beautifulPage = str(BeautifulSoup(plainPage, "html.parser"))
        result = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', beautifulPage)
        self._listmail.extend(result)
        self.reloadMail()

    def dedupe(self):
        newlistmail = list()
        for mail in self._listmail:
            if mail not in newlistmail:
                newlistmail.append(mail)
        self._listmail = newlistmail
        self.reloadMail()

    def validityMail(self):
        keys = self.tv.get_children()
        invalidMailKey = []
        for item in keys:
            current_item = self.tv.item(item)
            current_mail = current_item['text']
            self.tv.item(item, values=['OK'])
            try:
                self.tv.item(item, values=['OK'])
            except EmailNotValidError as e:
                print(e)
                invalidMailKey.append(item)
                self.tv.item(item, values=['ERROR'])
        if invalidMailKey:


    def saveMail(self):
        myFile = self._parent.campaign.get() + '.csv'
        with open(myFile, 'w+') as myCsv:
            spamwriter = csv.writer(myCsv, delimiter=' ', quotechar='|')
            for item in self._listmail:
                if type(item) is list:
                    spamwriter.writerow(item)
                else:
                    spamwriter.writerow([item])
    def next(self):
        self.saveMail()
        self.withdraw()
        myWriteMail = writeMail.writeMail(self._listmail, self)
        myWriteMail.mainloop()

    def back(self):
        self.saveMail()
        self._parent.deiconify()
        self.destroy()


