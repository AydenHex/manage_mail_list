# 12/09/18 - Help My Flower
# Group 5 - Project 4


from Tkinter import *

class App:
    def __init__(self, stateWindows):

        # Configuration de la fenêtre principale
        stateWindows.title("Help My Flower")
        stateWindows.configure(background="#d3ffce")
        stateWindows.geometry("600x600")
        stateWindows.resizable(False, False)
        stateWindows.iconbitmap('ressources/hmf_icon.ico')

        #HMF
        title = Label(stateWindows, text="Help My Flower", font=("Segoe Script", 32), background="#d3ffce").place(x=120, y=10)
        slogan = Label(stateWindows, text="Parce qu'elles le valent bien", font=("Segoe Script", 14), background="#d3ffce").place(x=150, y=90)

        #Affichage du logo
        logo = PhotoImage(file='ressources/hmf_logo.png')
        emplacement_logo = Canvas(stateWindows, background="#d3ffce", highlightthickness=0)
        emplacement_logo.create_image(200, 150, image=logo)
        emplacement_logo.image = logo
        emplacement_logo.place(x=100, y=160)

        #Boutons
        dashbord = Button(stateWindows, text="Accéder au dashboard", width=50, height=5, command=self.launchDashboar).place(x=120, y=500)

        # Variables de stockage
        self.humidity = StringVar()
        self.luminosity = StringVar()


root = Tk()
app = App(root)
root.mainloop()
