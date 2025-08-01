import tkinter as tk
from psutil_functions import SystemMeasure

current = SystemMeasure()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        super().resizable(False, False)
        super().geometry("500x400")
        super().title("CPU Util")
        tk.Label().grid(row=0, column=0)

        self.ramUsagePercentageLabel = tk.Label(text="Ram Usage: ")
        self.ramUsagePercentageLabel.grid(row=1, column=0)
        self.totalRamLabel = tk.Label(text="Total RAM: ")
        self.totalRamLabel.grid(row=1, column=1)
        self.availableRamLabel = tk.Label(text="Availablel RAM: ")
        self.availableRamLabel.grid(row=1, column=2)


    def mainProg(self):
        self.update()

    def update(self):
        self.stats = current.returnAll()

        self.ramUsagePercentageLabel.config(text="Ram Usage: {:.2f}%".format(float(self.stats['RAMUsagePercentage'])))
        self.totalRamLabel.config(text="Total RAM: {:.2f} GB".format(float(self.stats['TotalRamInGigaBytes'])))
        self.availableRamLabel.config(text="Availeble RAM: {:.2f} GB".format(float(self.stats['AvailableRAM'])))


        self.after(800, self.update)




app = App()
app.mainProg()
app.mainloop()



