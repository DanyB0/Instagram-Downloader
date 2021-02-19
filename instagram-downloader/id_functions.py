import os
import sys
import instaloader
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkcolorpicker import askcolor

#Change directory into the text files one
#Cambio la directory nei file di testo
def chd_1():
    directory4 = os.getcwd().replace("file-testo","") + r"\immagini"
    os.chdir(directory4)

#Change directory into the images one
#Cambio la directory nelle immagini
def chd_2():
    directory3 = os.getcwd().replace("immagini","") + r"\file-testo"
    os.chdir(directory3)

#menu
def menu():
    global menu

    menu = tk.Frame(bg=sfondo)
    menu.grid(row=0, column=0, sticky="nw", padx=3, pady=34)
    #guida_button = tk.Button(menu, text=("Guide"), font=("Helvetica", 12), command=guida, bg=sfondo, fg=scritte)
    #guida_button.grid(row=0,column=0, padx=3, pady=3, sticky="nwe")
    #guida_button.configure(relief="flat")
  
    dire_button = tk.Button(menu, text=("Change Directory"), font=("Helvetica", 12), command=directory, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    dire_button.grid(row=0,column=0, padx=3, pady=3, sticky="nwe")
    dire_button.configure(bd=0, relief="flat")

    cambia_colore = tk.Button(menu, text="Change Color", font=("Helvetica", 12), command=change_frame, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    cambia_colore.grid(row=1, column=0, padx=3, pady=3, sticky="sew")
    cambia_colore.configure(bd=0, relief="flat")

    esci = tk.Button(menu, text="Exit", font=("Helvetica", 12), command=uscita, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    esci.grid(row=2, column=0, padx=3, pady=3, sticky="sew")
    esci.configure(bd=0, relief="flat")
  
    togli_menu = tk.Button(menu, text="◄", font=("Helvetica", 12), command=elimina_menu, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    togli_menu.grid(row=3, column=0, padx=3, pady=3, sticky="sew")
    togli_menu.configure(bd=0, relief="flat")

#Open the documentation
#Apro la documentazione
def docum():
    #Change directory into the text files one
    #Cambio la directory nei file di testo
    chd_2()
    os.system("readme.md")

#Asks where the post will bve saved
#Chiedo dove salvare i post e cambio la directory corrente
def directory(): 
    directory = filedialog.askdirectory(title="Saving Directory")
    os.chdir(directory)

#Guide
#Guida
#def guida():
#    finestra_guida = tk.Toplevel(bg=sfondo)
#    finestra_guida.wm_attributes("-topmost", True)
#    finestra_guida.resizable(0,0)
#    a = tk.Label(finestra_guida, text="\nFirst of all you have to login into your Instagram account (only if you want to download pictures from a private profile). ", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=0, column=1)
#    b = tk.Label(finestra_guida, text="Next you have to type the name of the profile under <Download Posts>.", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=1, column=1)
#    z = tk.Label(finestra_guida, text="The default download directory is where you have the folder with the "".exe"" file of Instagram Downloader.", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=2, column=1)
#    f = tk.Label(finestra_guida, text="(You can change the directory in the menu)", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=3, column=1)
 
#Exit
#Ece dal programma
def uscita():
    sys.exit()

#Delete the menu frame
#Elimina il frame per il menu
def elimina_menu():
    menu.grid_forget()

#The user log into his account --- exceptions handling
#L'utente effettua il login al proprio account instagram --- gestisco le eccezioni
def login(event):
    noome = nome_entry.get()
    paassword = psw_entry.get()
    try:
        mod.login(noome, paassword)
    except instaloader.exceptions.BadCredentialsException:
        messagebox.showerror("Wrong Password", "The password is incorrect.")
    except instaloader.exceptions.InvalidArgumentException:
        messagebox.showerror("User doesn't exist", "The user does not exist")
    except instaloader.exceptions.ConnectionException:
        messagebox.showerror("Missing Password", "The password is missing.")
    else:
        messagebox.showinfo("Successful Login", "The login was successful.\nYou can now download pics from private profiles.")

#Download posts fo the desired profile --- exceptions handling
#Scarico i post del profilo desiderato e gestisco le eccezioni
def insta(event):
    utente = nome_utente.get()
    try:
        mod.download_profile(utente)
    except instaloader.exceptions.ProfileNotExistsException:
        messagebox.showerror("Inexistent Profile", "The profile does not exist.")
    except instaloader.exceptions.PrivateProfileNotFollowedException: 
        messagebox.showerror("Private and not followed profile", "The profile is private and not followed.\nIt's been downloaded only the profile pic.")
    except instaloader.exceptions.LoginRequiredException:
        messagebox.showerror("Login Needed", "To download posts from this profile you need to login.\nIt's been downloaded only the profile pic.")
    except FileExistsError:
        messagebox.showwarning("Folder Elimination", "You need to delete the folder with the profile pic.")
    else:
        messagebox.showinfo("Posts downloaded", "The profile posts have been downloaded correctly.")
        frame_info.destroy()

#Show the login frame
#Mostra il frame per il login
def mostra_login():
    global login_frame
    global nome_entry
    global psw_entry

    login_frame = tk.Frame(width=420, bg="#f0f0f0")
    login_frame.grid(row=1, column=0)
  
    nome = tk.StringVar()
    psw = tk.StringVar()
        
    login_scritta = tk.Label(login_frame, text="LOGIN", font=("Helvetica", 12), bg="#f0f0f0", fg=scritte).grid(row=0, column=1, sticky="nwe")
  
    nome_utente = tk.Label(login_frame, text="Username", font=("Helvetica", 12), bg="#f0f0f0", fg=scritte).grid(row=1, column=0, sticky="w")
  
    password = tk.Label(login_frame, text="Password", font=("Helvetica", 12), bg="#f0f0f0", fg=scritte).grid(row=2, column=0, sticky="w")      
        
    nome_entry = tk.Entry(login_frame, textvariable=nome, bg=sfondo, fg=scritte)
    nome_entry.grid(row=1, column=1, sticky="w", pady=1)
        
    psw_entry = tk.Entry(login_frame, textvariable=psw, show="*", bg=sfondo, fg=scritte)
    psw_entry.grid(row=2, column=1, sticky="w", pady=10)
  
    psw_entry.bind("<KeyPress-Return>", login)
    login_frame.bind("<Enter>", view_bt)
    login_frame.bind("<Leave>", cut_bt)

#Show the "*" that cover the characters and the "Show" button
#Visualizzo l'asterisco al posto dei caratteri e il pulsante per toglierlo
def view_bt(event):
    global show_bt
    psw_entry.config(show="*")
    show_bt = tk.Button(login_frame, text="Show", relief="flat", bd=0, command=hide_bt_fc, bg="#f0f0f0", fg=scritte, activebackground="#f0f0f0", activeforeground=scritte)
    show_bt.grid(row=2, column=2, sticky="w", pady=10, padx=2)

#Show the "*" that cover the characters and the "Show" button
#Visualizzo l'asterisco al posto dei caratteri e il pulsante per toglierlo
def view_bt_2():
  global show_bt
  psw_entry.config(show="*")
  show_bt = tk.Button(login_frame, text="Show", relief="flat", command=hide_bt_fc, bd=0, bg="#f0f0f0", fg=scritte, activebackground="#f0f0f0", activeforeground=scritte)
  show_bt.grid(row=2, column=2, sticky="w", pady=10, padx=2)

#Show the characters instead of the "*" and the "Hide" button
#Visualizzo i caratteri al posto dell'asterisco e il pulsante per rimetterlo
def hide_bt_fc():
    psw_entry.config(show="")
    show_bt.config(text="Hide ", relief="flat", command=view_bt_2, bd=0, bg="#f0f0f0", fg=scritte)

def cut_bt(event):
    show_bt.grid_forget()

#Delete the login frame
#Elimina il frame per il login
def elimina_login():
    login_frame.destroy()

#Show the download posts frame
#Mostra il frame per il download dei post
def insta_frame():
    global frame_insta
    global nome_utente
  
    frame_insta = tk.Frame(bg=sfondo)
    frame_insta.grid(row=0, column=0, pady=3, sticky="n")
  
    frame_insta.img = ImageTk.PhotoImage(Image.open("insta_3.jpeg"))
    frame_insta.img2 = frame_insta.img
  
    sfondo2 = tk.Label(frame_insta, image=frame_insta.img).grid(row=0, column=0)
  
    nome_utente2 = tk.StringVar()
  
    post = tk.Label(frame_insta, text="Download Posts", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=0, column=0, pady=3, sticky="n")
    nome_utente = tk.Entry(frame_insta, textvariable=nome_utente2, bg=sfondo, fg=scritte)
    nome_utente.grid(row=0, column=0, pady=35)
  
    nome_utente.bind("<KeyPress-Return>", insta)

def change_frame():
    frame_change = tk.Toplevel(bg=sfondo)
    frame_change.wm_attributes("-topmost", True)
    frame_change.resizable(0,0)

    sfondo_colore = tk.Button(frame_change, text="Background Color", font=("Helvetica", 15, "underline"), bg=sfondo, fg=scritte, relief="flat", activebackground=sfondo, activeforeground=scritte, bd=0, command=bg_color).grid(row=0, column=0, sticky="ns", padx=10, pady=10)
    scritte_colore = tk.Button(frame_change, text="Font Color", font=("Helvetica", 15, "underline"), bg=sfondo, fg=scritte, relief="flat", activebackground=sfondo, activeforeground=scritte, bd=0, command=fnt_color).grid(row=0, column=1, sticky="ns", padx=10, pady=10)

def bg_color():
    colore1 = askcolor()[1]
    if colore1:
        file_colore2 = open("colore-evidenza.txt", "w").write(colore1)
        messagebox.showinfo("Background color Saved", "The background color has been saved. Restart the app to apply the changes")
    else:
        pass

def fnt_color():
    colore2 = askcolor()[1]
    if colore2:
        file_colore2 = open("colore-evidenza.txt", "w").write(colore2)
        messagebox.showinfo("Background color Saved", "The background color has been saved. Restart the app to apply the changes")
    else:
        pass

#Change directory into the text files one
#Cambio la directory nei file di testo
chd_2()

mod = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern="", download_comments=False, download_geotags=False)
sfondo = open("colore-evidenza.txt", "r").readline()
scritte = open("colore-scritte.txt", "r").readline()