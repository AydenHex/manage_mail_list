import os
import re
import csv
import tkinter as tk
from tkinter import font
import manage_mail


class homePage(tk.Tk):

    def __init__(self):
        super().__init__()
        self.fontTitle = font.Font(family='Helvetica', size=28)
        self.fontName = font.Font(family='Helvetica', size=15)

        self.geometry("500x500")

        self.campaign = tk.StringVar()

        self.labelTitre = tk.Label(self, text="Nom de la compagne", font=self.fontTitle)
        self.inputName = tk.Entry(self, textvariable=self.campaign, justify="center", width=40, font=self.fontName)
        self.buttonLaunch = tk.Button(self, text="Commencer !", font=self.fontName, command=lambda: self.launchMailingList())

        self.labelTitre.place(x=70, y=150)
        self.inputName.place(x=25, y=220)
        self.buttonLaunch.place(x=180, y=300)

    def launchMailingList(self):
        listResult = list()
        myFile = self.campaign.get() + '.csv'
        if os.path.isfile(myFile):
            with open(myFile, 'r') as myCsv:
                spamreader = csv.reader(myCsv, delimiter=',', quotechar='|')
                for row in spamreader:
                    mail = row
                    listResult.append(mail)
        else:
            os.mknod(myFile)

        self.withdraw()
        my_manage_mail = manage_mail.manageMail(listResult, self)
        my_manage_mail.mainloop()






            

hp = homePage()
hp.mainloop()