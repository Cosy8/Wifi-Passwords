import tkinter as tk, sys
from tkinter import END, scrolledtext
from wifi_passwords import wifi

class gui:
    def __init__(self):
        root = tk.Tk()
        root.title('Wifi Passwords')
        root.geometry('400x360')
        root.protocol("WM_PROTOCOL", sys.exit)

        #*  Scrolled text attributes
        self.text = scrolledtext.ScrolledText(root, height=20)
        self.text.configure(font=("Courier", 10))
        self.text.edit_modified(False)   #!  Auto follow the inserted text
        def showEnd(event): 
            self.text.see(END)
            self.text.edit_modified(False)
        self.text.bind('<<Modified>>', showEnd)

        #*  Button attributes
        button = tk.Button(root, text='Start', command=lambda: self.clicked())

        #*   Pack objects into the root frame
        self.text.pack(fill=tk.X, expand=True, anchor='n')
        button.pack(pady=5)

        root.mainloop()

    def clicked(self):
        wifi(self.text)

gui()