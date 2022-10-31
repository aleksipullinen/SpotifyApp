from logging import root
from mimetypes import init
from tkinter import Tk, ttk
from tkinter import *
from turtle import left, right, width
from main import Kappaleet
import tkinter as tk


class UI:
    def __init__(self, root):
        self.root = root
        self.topLista = Kappaleet()

    def start(self):
        #Avaa ruudun, luo napit ja listat
        paivitys = tk.Button(master= self.root, text ="Päivitä lista", command=lambda:self.paivitys())
        paivitys.pack()
        
        tulostus1 = tk.Button(master= self.root, text ="Tulosta top50", command=lambda:self.suosituimpien_tulostus())
        tulostus1.pack()

        tulostus2 = tk.Button(master=self.root, text="Tulosta viimeaikaiset", command=lambda:self.viimeaikaisten_tulostus())
        tulostus2.pack()

        tulostus3 = tk.Button(master=self.root, text="Tulosta valence", command=lambda:self.mood_mittari())
        tulostus3.pack()

        self.listbox = tk.Listbox(height=50)
        self.listbox.pack(side="left")

        self.listbox2 = tk.Listbox(height=50)
        self.listbox2.pack(side="right")

        self.listbox3 = tk.Listbox(height=50)
        self.listbox3.pack()
       
    def paivitys(self):
        #kutsu funktioon joka päivittää listan ja luo yhteyden
        Kappaleet.paivita(self.topLista)

    def suosituimpien_tulostus(self):
        #Tulostaa top50 listan listboxiin
        ranking = 0
        for i in self.topLista.etsi_kappaleet():
            ranking += 1
            self.listbox.insert(END,f"Sija {ranking}: {i}")

    def viimeaikaisten_tulostus(self):
        #tulostaa viimeksi kuunnellut kappaleet(50kpl)
        for i in self.topLista.viimeaikaiset():
            self.listbox2.insert(END, i)

    def mood_mittari(self):
        for i in self.topLista.mood():
            self.listbox3.insert(END, i)

window = tk.Tk()
window.title("Paulify")
window.geometry("600x600")
ui = UI(window)
ui.start()
window.mainloop()