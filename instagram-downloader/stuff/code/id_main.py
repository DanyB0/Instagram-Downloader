import os
import sys
import tkinter as tk
import id_functions as idf
from PIL import Image, ImageTk
from tkinter import messagebox

class self(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("Instagram Downloader")
        self.master.resizable(0,0)
        self.grid()
        self.widgets()
        #self.master.overrideredirect(True)
        self.img_sfondo_1 = ImageTk.PhotoImage(Image.open("insta_1.png"))
        self.img_sfondo_2 = self.img_sfondo_1
        self.master.wm_attributes("-topmost", False)
        self.master.wm_attributes("-transparentcolor", "green")
        self.master.iconbitmap("logo.ICO")

    #def pressed(self, event):
    #   self.x = event.x
    #    self.y = event.y

    #def mouseDragged(self, event):
    #    deltax = event.x - self.x
    #    deltay = event.y - self.y
 
    #    newX = self.master.winfo_x() + deltax
    #    newY = self.master.winfo_y() + deltay
 
    #    self.master.geometry("+%d+%d"% (newX, newY))
    
    def widgets(self):
        #Elements in the window
        #Elementi nella finestra
        self.img_sfondo = ImageTk.PhotoImage(Image.open("insta_2.jpeg"))
        self.img_sfondo2 = self.img_sfondo

        self.sfondo = tk.Label(self, image=self.img_sfondo, bg="green")
        self.sfondo.grid(row=0, column=0)
        
        self.logi = tk.Label(self, text="Login", font=("Helvetica", 12), bg=sfondo, fg=scritte, width=6).grid(row=0, column=0, padx=5, pady=33, sticky="se")
        
        self.log = tk.Button(self, text=("▼"), font=("Helvetica", 12), command=idf.mostra_login, bg=sfondo, fg=scritte, width=3,  activebackground=sfondo, activeforeground=scritte)
        self.log.grid(row=0,column=0, padx=3, pady=3, sticky="se")
        self.log.configure(bd=0, relief="flat")
        
        self.elimin = tk.Button(self, text=("▲"), font=("Helvetica", 12), command=idf.elimina_login, bg=sfondo, fg=scritte, width=3, activebackground=sfondo, activeforeground=scritte)
        self.elimin.grid(row=0,column=0, padx=35, pady=3, sticky="se")
        self.elimin.configure(bd=0, relief="flat")

        self.menu = tk.Button(self, text=("Menu"), font=("Helvetica", 12), command=idf.menu, bg=sfondo, fg=scritte, width=5, activebackground=sfondo, activeforeground=scritte)
        self.menu.grid(row=0,column=0, padx=3, pady=3, sticky="nw")
        self.menu.configure(bd=0, relief="flat")

        self.docu = tk.Button(self, text=(" Doc."), font=("Helvetica", 12), command=idf.docum, bg=sfondo, fg=scritte, width=5, activebackground=sfondo, activeforeground=scritte)
        self.docu.grid(row=0,column=0, padx=3, pady=36, sticky="nw")
        self.docu.configure(bd=0, relief="flat")
        
        self.dany = tk.Label(self, text="DanyB0", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=0, column=0, padx=3, pady=3, sticky="sw")

        #self.sfondo.bind( "<Button-1>", self.pressed )
        #self.sfondo.bind( "<B1-Motion>", self.mouseDragged )

        idf.insta_frame()

def main():
    w = self()
    w.mainloop()

#Ask the user if he wants to read the documentation
#Chiede all'utente se vuole leggere la ducumentazione
def doc():
    directory24 = os.getcwd().replace("imm","") + r"\file-testo"
    os.chdir(directory24)    
    domanda = tk.messagebox.askquestion ("Open Documentation","Do you want to open the documentation?", icon = "question")
    if domanda == "yes":
        os.system("README.md")
        open("num.txt", "w").write("1").close()
    else:
        open("num.txt", "w").write("1").close()
        pass
    #Change directory into the images one
    #Cambio la directory nelle immagini
    directory2 = os.getcwd().replace("file-testo","") + r"\imm"
    os.chdir(directory2)

#Save the color code and the number (0 or 1)
#Salvo in varibili i colori e il numero
sfondo = open("colore-sfondo.txt", "r").readline()
scritte = open("colore-scritte.txt", "r").readline()
numero = open("num.txt", "r").readline()

#Change directory into the images one
#Cambio la directory nelle immagini
directory2 = os.getcwd().replace("file-testo","") + r"\imm"
os.chdir(directory2)

#Skip the "documentation ask" at every lauch
#Per evitare che ad ogni avvio chieda se si vuole leggere la documentazione
if numero == "0":
    doc()
else:
    pass

print("DanyB0")
print("\n!!! NON CHIUDERE QUESTA FINESTRA !!!\n")

main()