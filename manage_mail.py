import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk
import os, csv

class manageMail(tk.Tk):

    def __init__(self, thismailist):
        super().__init__()
        self.fontTitle = font.Font(family='Helvetica', size=28)
        self.fontCommun = font.Font(family='Helvetica', size=15)

        self._listmail = thismailist

        self.geometry("500x800")

        self.deleteDoubleButton = tk.Button(self, text="Dédoublouner", font=self.fontCommun)
        self.deleteDoubleButton.place(x=45,y=50)

        self.AvailableButton = tk.Button(self, text="Test de la Mailist", font=self.fontCommun)
        self.AvailableButton.place(x=280,y=50)

        self.CSVButton = tk.Button(self, text="CSV", font=self.fontCommun, command= lambda: self.loadCSV("test.csv"))
        self.CSVButton.place(x=85, y=110)

        self.LinkButton = tk.Button(self, text="URL", font=self.fontCommun)
        self.LinkButton.place(x=330, y=110)


        self.tv = ttk.Treeview(self)
        self.tv['columns'] = ('validity')
        self.tv.heading("#0", text='Email')
        self.tv.column("#0", width=300)
        self.tv.heading('validity', text='Validité')
        self.tv.column('validity', anchor='center', width=100)

        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tv.yview)
        self.vsb.place(x=50+400+2, y=200, height=200+20)

        self.tv.configure(yscrollcommand=self.vsb.set)

        self.tv.place(x=50,y=200)

    def loadMail(self):
        for mail in self._listmail:
            self.tv.insert("", 'end', text=mail, values=('~'))
    
    def loadCSV(self, myFile):
        
        if os.path.isfile(myFile):
            listResult = list()
            with open(myFile, 'r') as myCsv:
                spamreader = csv.reader(myCsv, delimiter=',', quotechar='|')
                for row in spamreader:
                    self._listmail.append(row)
                    self.tv.insert("", 'end', text=row, value=('~'))
        print("ok")
            
    


        

mm = manageMail(["royerquentin.pro@outlook.com", "ted@ted.fr"])
mm.after(2, mm.loadMail())
mm.mainloop()