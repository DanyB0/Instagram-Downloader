import os
import sys
from datetime import datetime
import instaloader
import tkinter as tk
import colorama
import shutil
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
from tkcolorpicker import askcolor

colorama.init()

direct = os.getcwd().replace(r"Instagram-Downloader","")
dire2 = direct.replace(r"\imm", r"\Instagram-Downloader")
dire3 = direct.replace(r"\instagram-downloader\stuff","")
dire4 = direct.replace(r"\stuff","")

#Change directory into the text files one
#Cambio la directory nei file di testo
def chd_1():
    directory4 = direct + r"\imm"
    os.chdir(directory4)
    return directory4

#Change directory into the images one
#Cambio la directory nelle immagini
def chd_2():
    directory3 = direct + r"\file-testo"
    os.chdir(directory3)
    return directory3

#Change directory into the posts one
#Cambio la directory nella cartella dei post
def chd_3():
    os.chdir(dire3)
    if not os.path.exists(dire3 + r"\posts"):
        os.mkdir("posts")
        os.chdir(dire3 + r"\posts")
    else:
        os.chdir(dire3 + r"\posts")

#menu
def menu():
    global menu

    menu = tk.Frame(bg=sfondo)
    menu.grid(row=0, column=0, sticky="nw", padx=3, pady=34)
  
    #dire_button = tk.Button(menu, text=("Change Directory"), font=("Helvetica", 12), command=directory, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    #dire_button.grid(row=0,column=0, padx=3, pady=3, sticky="nwe")
    #dire_button.configure(bd=0, relief="flat")

    cambia_colore = tk.Button(menu, text="Change Color", font=("Helvetica", 12), command=change_frame, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    cambia_colore.grid(row=1, column=0, padx=3, pady=3, sticky="sew")
    cambia_colore.configure(bd=0, relief="flat")

    restart_lbl = tk.Button(menu, text="Restart", font=("Helvetica", 12), command=restart, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    restart_lbl.grid(row=2, column=0, padx=3, pady=3, sticky="sew")
    restart_lbl.configure(bd=0, relief="flat")

    esci = tk.Button(menu, text="Exit", font=("Helvetica", 12), command=uscita, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    esci.grid(row=3, column=0, padx=3, pady=3, sticky="sew")
    esci.configure(bd=0, relief="flat")
  
    togli_menu = tk.Button(menu, text="◄", font=("Helvetica", 12), command=elimina_menu, bg=sfondo, fg=scritte, activebackground=sfondo, activeforeground=scritte)
    togli_menu.grid(row=4, column=0, padx=3, pady=3, sticky="sew")
    togli_menu.configure(bd=0, relief="flat")

#Open the documentation
#Apro la documentazione
def docum():
    #Change directory into the text files one
    #Cambio la directory nei file di testo
    chd_2()
    os.system("readme.md")
    chd_1()

#Asks where the post will bve saved
#Chiedo dove salvare i post e cambio la directory corrente
#def directory():
#    directo = filedialog.askdirectory(title="Saving Directory")
#    os.chdir(directo)

def restart():
    os.chdir(dire4)
    print("\nrestarting...")
    os.startfile("restart.bat")

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
        print("logging in...")
        mod.login(noome, paassword)
    except instaloader.exceptions.BadCredentialsException:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "wrong password")
        messagebox.showerror("Wrong Password", "The password is incorrect.")
    except instaloader.exceptions.InvalidArgumentException:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "inexistent user")
        messagebox.showerror("User doesn't exist", "The user does not exist")
    except instaloader.exceptions.ConnectionException:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "missing password")
        messagebox.showerror("Missing Password", "The password is missing.")
    else:
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "login completed")
        messagebox.showinfo("Successful Login", "The login was successful.\nYou can now download pics from private profiles.")
    print(colorama.Fore.WHITE)

#Download posts fo the desired profile --- exceptions handling
#Scarico i post del profilo desiderato e gestisco le eccezioni
def insta(event):
    bho = 0
    if os.getcwd() != chd_1 or chd_2:
        pass
    else:
        os.chdir(direct)
    chd_3()
    utente = nome_utente.get()
    tempo_inizio = datetime.now()
    try:
        mod.download_profile(utente)
    except instaloader.exceptions.ProfileNotExistsException:
        print(colorama.Fore.RED + colorama.Style.BRIGHT + "inexistent profile")
        messagebox.showerror("Inexistent Profile", "The profile does not exist.")
        print(colorama.Fore.WHITE)
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "the profile is private and not followed")
        messagebox.showwarning("Private and not followed profile", "The profile is private and not followed.\nIt's been downloaded only the profile pic.")
        print(colorama.Fore.WHITE)
    except instaloader.exceptions.LoginRequiredException:
        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "login needed")
        messagebox.showwarning("Login Needed", "To download posts from this profile you need to login.\nIt's been downloaded only the profile pic.")
        print(colorama.Fore.WHITE)
    except FileExistsError:
        print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + "delete the folder with the profile pic.")
        messagebox.showwarning("Folder Elimination", "You need to delete the folder with the profile pic.")
        print(colorama.Fore.WHITE)
    else:
        tempo_fine = datetime.now()
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "posts downloaded in {}".format(tempo_fine - tempo_inizio))
        print(colorama.Fore.WHITE + "dividing images from videos...")
        #Cambio directory nella cartella con il nome del profilo di cui si stanno scaricando i post
        os.chdir(os.getcwd() + "\\" + utente)
        #Prendo e salvo in una lista il nome dei file nella cartella
        cartella_downl = os.listdir(os.getcwd())
        #Creo le cartelle "video" e "immagini" se non ci sono e sposto i file nelle rispettive cartelle
        for file in range (len(cartella_downl)):
            if cartella_downl[file].endswith(".mp4"):
                bho = 1
                try:
                    if not os.path.exists(os.getcwd() + r"\video"): #Se la cartella video non esiste la creo e sposto lì i video
                        os.mkdir("video")
                        shutil.move(os.path.abspath(cartella_downl[file]), os.getcwd() + r"\video")
                    else:
                        shutil.move(os.path.abspath(cartella_downl[file]), os.getcwd() + r"\video")
                #Elimino i file doppioni
                except shutil.Error:
                    os.remove(cartella_downl[file])
            elif cartella_downl[file].endswith(".jpg"):
                try:
                    if not os.path.exists(os.getcwd() + r"\immagini"): #Se la cartella immagini non esiste la creo e sposto lì le immagini
                        os.mkdir("immagini")
                        shutil.move(os.path.abspath(cartella_downl[file]), os.getcwd() + r"\immagini")
                    else:
                        shutil.move(os.path.abspath(cartella_downl[file]), os.getcwd() + r"\immagini")
                #Elimino i file doppioni
                except shutil.Error:
                    os.remove(cartella_downl[file])
        if bho == 1:
            #Cambio directory nei video e rinomino i file. Elimino i doppioni
            os.chdir(os.getcwd() + r"\video")
            file_video = os.listdir(os.getcwd())
            for file2 in range (len(file_video)):
                try:
                    os.rename(file_video[file2], utente + "_" + str(file2+1) + ".mp4")
                except FileExistsError:
                    os.remove(file_video[file2])
            #Cambio directory nelle immagini e rinomino i file. Elimino i doppioni
            os.chdir(os.getcwd().replace("video","immagini"))
            file_imm = os.listdir(os.getcwd())
            for file3 in range (len(file_imm)):
                try:
                    os.rename(file_imm[file3], utente + "_" + str(file3+1) + ".png")
                except FileExistsError:
                    os.remove(file_imm[file3])
        else:
            #Cambio directory nelle immagini e rinomino i file. Elimino i doppioni
            os.chdir(os.getcwd() + r"\immagini")
            file_imm_2 = os.listdir(os.getcwd())
            for file4 in range (len(file_imm_2)):
                try:
                    os.rename(file_imm_2[file4], utente + "_" + str(file4+1) + ".png")
                except FileExistsError:
                    os.remove(file_imm_2[file4])
        print(colorama.Fore.GREEN + colorama.Style.BRIGHT + "division completed")
        messagebox.showinfo("Posts downloaded", "The profile posts are now in their folder.")
    print(colorama.Fore.WHITE)
    #"Rimetto" la directory delle immagini
    os.chdir(direct)

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
        
    nome_entry = tk.Entry(login_frame, textvariable=nome, bd=0, bg=sfondo, fg=scritte)
    nome_entry.grid(row=1, column=1, sticky="w", pady=1)
        
    psw_entry = tk.Entry(login_frame, textvariable=psw, bd=0, show="*", bg=sfondo, fg=scritte)
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
  
    frame_insta.img = ImageTk.PhotoImage(Image.open("insta_3.jpg"))
    frame_insta.img2 = frame_insta.img
  
    sfondo2 = tk.Label(frame_insta, image=frame_insta.img).grid(row=0, column=0)
  
    nome_utente2 = tk.StringVar()
  
    post = tk.Label(frame_insta, text="Download Posts", font=("Helvetica", 12), bg=sfondo, fg=scritte).grid(row=0, column=0, pady=3, sticky="n")
    nome_utente = tk.Entry(frame_insta, textvariable=nome_utente2, bd=0, bg=sfondo, fg=scritte)
    nome_utente.grid(row=0, column=0, pady=35)
  
    nome_utente.bind("<KeyPress-Return>", insta)

def change_frame():
    frame_change = tk.Toplevel(bg=sfondo)
    frame_change.iconbitmap("logo.ICO")
    frame_change.resizable(0,0)

    sfondo_colore = tk.Button(frame_change, text="Background Color", font=("Helvetica", 15, "underline"), bg=sfondo, fg=scritte, relief="flat", activebackground=sfondo, activeforeground=scritte, bd=0, command=bg_color).grid(row=0, column=0, sticky="ns", padx=10, pady=10)
    scritte_colore = tk.Button(frame_change, text="Font Color", font=("Helvetica", 15, "underline"), bg=sfondo, fg=scritte, relief="flat", activebackground=sfondo, activeforeground=scritte, bd=0, command=fnt_color).grid(row=0, column=1, sticky="ns", padx=10, pady=10)

def bg_color():
    colore1 = askcolor()[1]
    if colore1:
        chd_2()
        file_colore1 = open("colore-sfondo.txt", "w").write(colore1)
        chd_1()
        messagebox.showinfo("Background color Saved", "The background color has been saved. Restart the app to apply the changes")
    else:
        pass

def fnt_color():
    colore2 = askcolor()[1]
    if colore2:
        chd_2()
        file_colore2 = open("colore-scritte.txt", "w").write(colore2)
        chd_1()
        messagebox.showinfo("Font color Saved", "The font color has been saved. Restart the app to apply the changes")
    else:
        pass

#Change directory into the text files one
#Cambio la directory nei file di testo
chd_2()

mod = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern="", download_comments=False, download_geotags=False)
sfondo = open("colore-sfondo.txt", "r").readline()
scritte = open("colore-scritte.txt", "r").readline()