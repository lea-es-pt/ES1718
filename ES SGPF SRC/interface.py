# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:27:40 2017

@author: Andreea Aniculaesei
"""

#basic and ugly

import Tkinter as tk
import subprocess

class App(tk.Frame):
    def __init__(self, master):
        #basic
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("SGPF Application")
        
        tk.Label(self, text="This is the first GUI! ").pack()
        
        #basic appearance
        self.master.resizable(True, True)
        self.master.tk_setPalette(background= '#ececec')
        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        self.master.geometry("+{}+{}".format(x, y))
        self.master.config(menu=tk.Menu(self.master))
        
        #adding more frames
        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15)
        
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady = (0,15), anchor='e')
        
        #buttons 
        tk.Button(button_frame, text = 'Ok', default = 'active', command=self.click_ok).pack(side='right')
        tk.Button(button_frame, text = 'Cancel', command=self.click_cancel).pack(side='right')

        
    def click_ok(self):
            print("The user clicked OK ")
            
    def click_cancel(self):
        print("The user clicked Cancel")
        self.master.destroy()
        
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.mainloop()
    
    #basic appearance
    subprocess.call(['/usr/bin/osascript', '-e', 'tell app "Finder" to set fronmost of process "Python" to true'])
    