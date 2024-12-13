import tkinter as tk
from shuttle_input import personal #personal 클래스를 shuttle_input에서 참조함
from shuttle import shuttlebus #shuttlebus3 클래스를 shuttle에서 참조함

def input_shuttle(): #승차인원 입력창 함수 정의
  global inputwindow
  inputwindow = tk.Toplevel(root)
  inputwindow.title("오늘의 승차인원 입력")
  app1 = personal(inputwindow) #승차인원 입력창을 띄움

def import_shuttle(): #승차인원 확인창 함수 정의
  global shuttlewindow
  shuttlewindow = tk.Toplevel(root)
  shuttlewindow.title("승차인원 확인")
  app2 = shuttlebus(shuttlewindow) #승차인원 확인창을 띄움

root = tk.Tk()
root.title("ShuttleMain")
connectbutton = tk.Button(root, text = "승차인원 입력", command = input_shuttle) #input_shuttle 참조
connectbutton.pack()
databutton = tk.Button(root, text = "하루의 승차인원 확인", command = import_shuttle) #import_shuttle 참조
databutton.pack()
root.mainloop()