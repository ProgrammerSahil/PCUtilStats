import tkinter as tk
from psutil_functions import SystemMeasure

current = SystemMeasure()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        super().resizable(False, False)
        super().geometry("500x400")
        super().title("CPU Util")
        self.mainLabel = tk.Label()
        self.mainLabel.pack()

    def mainProg(self):
        self.update()
        
    def update(self):
        self.stats = current.returnAll()
        self.mainLabel.config(text=str(self.stats['RAMUsagePercentage'])+" "+str(self.stats['AvailableRAM']))
        self.after(800, self.update)




app = App()
app.mainProg()
app.mainloop()



