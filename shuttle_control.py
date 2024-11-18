import tkinter as tk
from shuttle import shuttlebus
import pymysql

def import_shuttle():
  global shuttlewindow
  shuttlewindow = tk.Toplevel(root)
  app1 = shuttlebus(shuttlewindow)

root = tk.Tk()
root.title("ShuttleMain")
databutton = tk.Button(root, text = "하루의 승차인원 확인", command = import_shuttle)
databutton.pack()
root.mainloop()