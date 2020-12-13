import subprocess
from tkinter import END

from prettytable import PrettyTable


class wifi:
    def __init__(self, text):
        x = PrettyTable()

        data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
        profiles =  [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        x.field_names = ["Wi-fi Name".center(17), "Password".center(17)]
        text.insert(END, x)
        for i in profiles:
            results = subprocess.check_output(['netsh','wlan','show','profiles', i, 'key=clear']).decode('utf-8').split('\n')
            results = [r.split(":")[1][1:-1] for r in results if "Key Content" in r]

            try:
                text.delete(1.0, END)
                x.add_row([i, results[0]])
                text.insert(END, x)
            except IndexError:
                text.delete(1.0, END)
                x.add_row([i, ""])
                text.insert(END, x)
            text.update()