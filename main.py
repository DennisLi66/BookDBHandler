import tkinter as tk
from tkinter import *
from tkinter import ttk
#read file for mysql credentials

class Interface(Frame):
    def frontPage(self):
        title = tk.Label(self,text = "Welcome to the Interface!");
        title.grid(row = 0,column=1);
    def __init__(self):
        tk.Frame.__init__(self);
        self.pack();
        self.master.title("Interface");
        self.master.geometry("500x500");
        self.frontPage();


def run():
    Interface().mainloop();


if __name__ == '__main__':
    run()
