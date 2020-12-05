import subprocess
from tkinter import END

class wifi:
    def __init__(self, text):
        data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
        profiles =  [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

        text.insert(END, "{:<30}|  {:<}\n\n".format("Wi-fi Name", "Password"))
        for i in profiles:
            results = subprocess.check_output(['netsh','wlan','show','profiles', i, 'key=clear']).decode('utf-8').split('\n')
            results = [r.split(":")[1][1:-1] for r in results if "Key Content" in r]

            try:
                text.insert(END, "{:<30}|  {:<}\n".format(i, results[0]))
            except IndexError:
                text.insert(END, "{:<30}|  {:<}\n".format(i, ""))
            text.update()