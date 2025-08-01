import tkinter as tk
from psutil_functions import SystemMeasure

current = SystemMeasure()

print(current.returnAll())


