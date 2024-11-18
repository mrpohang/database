import pymysql
import tkinter as tk

class shuttlebus:
   def core():
     root= tk.Tk()
     root.title("shuttle") 
     root.mainloop()
   def __init__(self, master):
    self.master = master
    self.host = "127.0.0.1"
    self.port = 3306
    self.database = "shuttle"
    self.username = "root"
    self.password = "root"

    self.conflag = True

    
    try:
     self.label_prepare = tk.Label(self.master, text = '데이터베이스 연결 준비..')
     self.label_prepare.pack()
     self.conn = pymysql.connect(host = self.host, user = self.username, passwd = self.password, db = self.database, port = self.port, charset = 'utf8')
     self.master.after(5000, self.label_prepare.destroy())
     self.label_success = tk.Label(self.master, text = "데이터베이스 연결 성공")
     self.label_success.pack()
     self.label_success.destroy()
    except Exception as e: #예외 발생시 에러 메시지 출력
     self.master.after(5000, self.label_prepare.destroy())
     self.label_fail = tk.Label(self.master, text = "데이터베이스 연결 실패")
     self.label_fail.pack()
     self.conflag = False

    if self.conflag == True:
     self.cursor = self.conn.cursor()

     sqlstring = 'select * from shuttle;'

     res = self.cursor.execute(sqlstring)

     data = self.cursor.fetchall()

     self.label_front = tk.Label(self.master, text = '{0}\t{1:<12}\t{2:<}'.format('shuttledate', 'shuttletime', 'shuttlepassenger'))
     self.label_front.pack()
     for rowdata in data:
        self.label_data = tk.Label(self.master, text = '{0}\t{1:<12}\t{2:<}'.format(rowdata[0], rowdata[1], rowdata[2]))
        self.label_data.pack()

     self.cursor.close()

     self.conn.close()
   



    