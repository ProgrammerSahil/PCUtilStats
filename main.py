import tkinter as tk
from psutil_functions import SystemMeasure

current = SystemMeasure()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        super().resizable(False, False)
        super().geometry("500x400")
        super().title("CPU Util")
        
        self.ramUsagePercentageLabel = tk.Label(text="Ram Usage: ")
        self.ramUsagePercentageLabel.grid(row=0, column=0)

        self.totalRamLabel = tk.Label(text="Total RAM: ")
        self.totalRamLabel.grid(row=0, column=1)

    def mainProg(self):
        self.update()
        
    def update(self):
        self.stats = current.returnAll()
        self.ramUsagePercentageLabel.config(text=f"Ram Usage: {str(float(self.stats['RAMUsagePercentage']))}%")

        self.totalRamLabel.config(text="Total RAM: {:.2f} GB".format(float(self.stats['TotalRamInGigaBytes'])))

        self.after(800, self.update)




app = App()
app.mainProg()
app.mainloop()



