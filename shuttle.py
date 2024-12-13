import pymysql #pymysql 참조
import tkinter as tk
from tkinter import*
from tkinter import messagebox #메시지박스 이용을 위한 참조
from tkinter import ttk #스크롤바 사용

class shuttlebus:
  #핵심 기능 정의
  def core():
     root= tk.Tk()
     root.title("shuttle")
     app = shuttlebus(root)
     root.protocol("WM_DELETE_WINDOW", app.close_connection) #창을 닫으면 연결이 종료됨
     root.mainloop()

  #데이터베이스 설정
  def __init__(self, master):
    self.master = master
    self.host = "127.0.0.1"
    self.port = 3306
    self.database = "shuttle"
    self.username = "root"
    self.password = "root"

    self.conflag = True

    try:
     messagebox.showinfo('연결상태 알림','데이터베이스 연결 준비..') #연결 준비 메시지를 띄움움
     self.conn = pymysql.connect(host = self.host, user = self.username, passwd = self.password, db = self.database, port = self.port, charset = 'utf8')
     messagebox.showinfo("연결상태 알림", "데이터베이스 연결 성공") #연결 성공 시 성공 메시지를 띄움

     if self.conflag == True: #연결 성공 시 실행
      self.cursor = self.conn.cursor()

      sqlstring = 'select * from shuttle;'

      res = self.cursor.execute(sqlstring)

      data = self.cursor.fetchall()

      self.label_front = tk.Label(self.master, text = '{0}\t{1:<}\t{2:<}'.format('shuttledate', 'shuttletime', 'shuttlepassenger')) #self.master가 없으면 새 창이 안 뜸
      self.label_front.pack() #날짜, 시간, 승객 수 삽입

      #프레임 및 리스트박스, 스크롤바 장착
      shuttleframe = tk.Frame(self.master)
      shuttleframe.pack() #프레임 장착
      self.shuttlelistbox = tk.Listbox(shuttleframe, width = 50, height = 30)
      self.shuttlelistbox.pack(side = tk.LEFT, fill = tk.BOTH) #리스트박스 장착
      self.shuttlescroll = ttk.Scrollbar(shuttleframe, orient = tk.VERTICAL, command = self.shuttlelistbox.yview) #스크롤바 정의
      self.shuttlescroll.pack(side = tk.RIGHT, fill = tk.Y) #스크롤바 장착

      self.shuttlelistbox.config(yscrollcommand = self.shuttlescroll.set) #스크롤바/리스트박스 연동

     for rowdata in data:
        self.shuttlelistbox.insert(tk.END,' '.join(map(str, rowdata))) # 그날의 승차 인원 및 승객 수 출력 #뤼튼 참고고

    except Exception as e: #예외 발생시 에러 메시지 출력
     messagebox.showinfo("연결상태 알림", "데이터베이스 연결 실패")
     self.conflag = False

  def connection_confirm(self): #connection_confirm 메소드 추가
    if hasattr(self, 'cursor'):
      self.cursor.close()
    if hasattr(self, 'conn'):
      self.conn.close() #연결 확인 후 연결을 끝냄