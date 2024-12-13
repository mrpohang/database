import pymysql #pymysql 참조
import tkinter as tk
from tkinter import*
from tkinter import messagebox #메시지박스 사용을 위한 참조

class personal:
    date = '0'
    time = '0'
    bus = 45
    passenger = 0

    def core2(): #창 연결 제어
       root= tk.Tk()
       root.title("shuttle_input")
       app = personal(root)
       root.protocol("WM_DELETE_WINDOW", app.close_connection) #창을 닫으면 연결이 종료됨
       root.mainloop()

    def __init__(self, master):
     self.master = master
     self.host = "127.0.0.1" #ip주소
     self.port = 3306
     self.database = "shuttle"
     self.username = "root"
     self.password = "root"

     self.conflag = True

     try:
      messagebox.showinfo('연결 알림', '데이터베이스 연결 준비..')
      self.conn = pymysql.connect(host = self.host, user = self.username, passwd = self.password, db = self.database, port = self.port, charset = 'utf8')
      messagebox.showinfo("연결 알림", "데이터베이스 연결 성공") #성공시 성공 메시지를 띄움
     except Exception as e: #예외 발생시 에러 메시지 출력
      messagebox.showinfo("연결 알림", "데이터베이스 연결 실패")
      self.conflag = False

     if self.conflag == True:
      self.cursor = self.conn.cursor()

      sqlstring = 'select * from shuttle;' #sql 실행 문장

      res = self.cursor.execute(sqlstring)

      data = self.cursor.fetchall()

      self.label_date = tk.Label(self.master, text = "날짜를 입력하세요: ") #오늘의 날짜 입력
      self.label_date.pack()
      self.entry1 = Entry(self.master,width = 10, bg = 'white')
      self.entry1.pack()
      self.label_time = tk.Label(self.master,text = "시간을 입력하세요: ") # 현재 시간 입력
      self.label_time.pack()
      self.entry2 = Entry(self.master,width = 10, bg = 'white')
      self.entry2.pack()
      self.label_passenger = tk.Label(self.master, text = "탑승 인원 수를 입력하세요: ") #승차 인원 수 입력
      self.label_passenger.pack()
      self.entry3 = Entry(self.master, width = 10, bg = 'white')
      self.entry3.pack()

      def shuttlepassenger():
        date = self.entry1.get() #날짜
        time = self.entry2.get() #시간
        passenger = self.entry3.get() #승객 수

        query = "insert into shuttle(shuttledate, shuttletime, shuttlepassenger) values(%s, %s, %s)"
        data = (date, time, passenger) #날짜, 시간, 승객 수를 저장함
        self.cursor.execute(query, data) #변경된 데이터 입력
        self.conn.commit()

        try:
          messagebox.showinfo("입력 확인","입력 완료") #정상 입력시 입력 완료 창을 띄움
        except Exception as e: #예외 발생시 에러 메시지 출력
          messagebox.showinfo("입력 확인", "입력에 문제가 있습니다.")


      self.button_insert = tk.Button(self.master,text = "입력", command = shuttlepassenger) #입력 버튼을 누르면 데이터 입력
      self.button_insert.pack()
      
    def connection_confirm(self): #connection_confirm 메소드 추가
      if hasattr(self, 'cursor'):
        self.cursor.close()
      if hasattr(self, 'conn'):
        self.conn.close() #연결 확인 후 연결을 끝냄