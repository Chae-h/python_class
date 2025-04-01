# 파이썬 17회차

# 1. GUI 프로그래밍
#    CLI(Command Line Interface) : 키보드로 Command(명령어)를 줄 단위로 입력해서 사용하는 방식 (터미널 환경)
#    GUI(Graphic User Interface) : 그래픽 화면에서 마우스를 사용하는 환경 (예:윈도우 환경)

# 2. tkinter
#   Python으로 GUI를 만드는 이유
# 1) 쉬운 구현 : 적은 코드로 GUI 프로그램을 만들 수 있음
# 2) 크로스 플랫폼 - 윈도우, Mac, Linux 등 다양한 운영체제에서 동작
# 3) 다양한 라이브러리 지원 :Tkinter, PyQt, PySide, Kivy 등 다양한 GUI 라이브러리 제공
# 4) 빠른 개발 속도 :  웹 기반이 아닌 독립 실행형 데스크톱 앱을 쉽게 제작가능

# 3. 기본 구성
# import tkinter as tk #Tkinter 임포트
# root = tk Tk() #기본 창 생성
# root.title("Tkinter 기본창") # 창제목 설정   title("제목") > 창의 제목 설정
# root.geometry("300x200") # 창 크기 설정
# root.mainloop() # GUI 실행   #프로그램이 실행되고 사용자의 입력을 기다리는 이벤트 루프 실행


# 4. 위젯
#   Label : 텍스트 또는 이미지 표시 [주요속성 : text, fontm fg(전경색:글자색), bg(배경색:글자배경색), image]
#   Button : 버튼 클릭 이벤트 처리 [주요속성 : text, command(메소드), state, fg, bg]
#   Entry : 한 줄 텍스트 입력 필드 [주요속성 : textvariable, show(비밀번호 입력:***로 표시)]
#   Text : 여러줄 텍스트 입력 필드 [주요속성 : height, widthm wrap]
#   Checkbutton : 체크박스(참/거짓) [주요속성 : variable, onvalue, offvalue]
#   Radiobutton : 라디오버튼(하나만 선택) [주요속성 : variable, value, text]

# 5. 레이아웃
#   1) Pack(상대 위치 지정)
        # - 위젯들을 부모 위젯에 모두 패킹하여 불필요한 공간을 없앤다.
        # - 정확한 위치 설정 불가능
#   2) Grid(그리드 위치 지정)
        # - 위젯들을 테이블 레이아웃에서 지정된 rowm, column에 놓는다.
#   3) Place(절대 위치 지정)
        # - 위젯의 위치를 절대(absolute) 좌표로 설정 한다.
        # - 창 크기에 따라 위치가 변하지 않기 때문에 많이 사용되지는 않는다.



# 1교시-----------------------------

# Git Bash 에서 pip install tkinter

import tkinter as tk
from tkinter import messagebox

from cProfile import label

from PIL.ImageMath import lambda_eval
from pandas.core.dtypes.common import is_1d_only_ea_dtype

# 1. 기본창 구성
# root = tk.Tk() # 창 생성
# root.title("GUI프로그램 실습") # 창 제목(타이틀)
# root.geometry("800x800") # 창 크기 설정(가로x세로)
# # root.resizable(False, False) # 창 크기 조절 가능/불가능을 결정 (가로,  세로) 현재 코드는 불가능
# root.resizable(True, True) # 창 크기 조절 가능/불가능을 결정 (가로,  세로) 현재 코드는 가능
#
# # 2. 구성된 창에 텍스트 넣기
# label = tk.Label(root, text="안녕하세요", fg="red", bg="blue") # 텍스트 = "내용" , 글자색 및 배경색 지정
# ## label.pack()
# label.pack(side="top") # top, bottom, left, right (텍스트 위치 설정)
#
# # 3. 버튼 생성 및 실행 메소드 지정
# def button_click():
#     print("클릭됨")
#     print(chk_var.get()) # 체크된 상태를 0과 1로 구분 (0: 체크 안함, 1: 체크됨)  chk_var은 아래에 체크박스 만들기에 있고 같이 연동
#     print(radio_var.get()) # 체크된 옵션을 출력(선택된 문자열)  radio_var은 아래에 라디오 버튼 만들기에 있고 같이 연동
#     root.quit() # 종료 버튼 및 창 종료 실행 메소드
#
# button = tk.Button(root, text="종료", command=button_click)
# button.pack(side="bottom")
#
# # 4. 입력창 만들기
# entry = tk.Entry(root)    # entry : 한줄 텍스트를 입력 받을 수 있는 공간 생성. (공간만 생성할뿐 메소드가 없는 상태에서는 실행되는 것이 없음)
# entry.pack(side="top")
#
# text = tk.Text(root)  # 여러 줄을 입력할 수 있는 텍스트 창 생성.
# ## text = tk.Text(root, wrap=" ? ")  # 줄바꿈 설정
# text = tk.Text(root, wrap="word")  # none : 창크기에 도달해도 자동 내려쓰기 하지 않음, char : 창크기에 도달하면 자동 내려 쓰기, wrap : 단어 단위로 줄 바꿈(내림)
# text.pack(side="top")
#
# # 4. 체크박스 생성하기
# chk_var = tk.IntVar()  # 체크 된 상태를 변수에 담아두는 곳  IntVar 숫자로 받는다 0과 1
# chk = tk.Checkbutton(root, text="위 내용에 거짓이 없음을 동의 합니다.", variable=chk_var)
# chk.pack(side="bottom")
#
# # 5. 라디오 버튼 만들기 (옵션 고르기)
# # 기본 구성
# # radio_var = tk.StringVar()   # 선택된 옵션을 담는 변수  StringVar 문자열로 받는다
# # r1 = tk.Radiobutton(root, text="옵션1", variable=radio_var, value="옵션 1")  # value 선택되었을때 선택된 것을 StringVar(문자열) 변수에 담는다
# # r2 = tk.Radiobutton(root, text="옵션2", variable=radio_var, value="옵션 2")
# # r3 = tk.Radiobutton(root, text="옵션3", variable=radio_var, value="옵션 3")
# # r1.pack(side="top")
# # r2.pack(side="top")
# # r3.pack(side="top")
#
# # 다른 버전 옵션 선택과 동시에 print 출력
# def value_print():
#     print(radio_var.get())
#
# radio_var = tk.StringVar()
# r1 = tk.Radiobutton(root, text="옵션1", variable=radio_var, value="옵션 1", command=value_print)  # command=value_print 을 통해 선택과 동시에 클릭된 값을 출력한다.
# r2 = tk.Radiobutton(root, text="옵션2", variable=radio_var, value="옵션 2", command=value_print)
# r3 = tk.Radiobutton(root, text="옵션3", variable=radio_var, value="옵션 3", command=value_print)
# r1.pack(side="top")
# r2.pack(side="top")
# r3.pack(side="top")

# 6. 프로그램 실행하기
# root.mainloop() # 창 실행 (맨 마지막에 위치한다. 모든 위젯이 설계된 후 )

#-------------------------------------------
# 레이아웃 - 2) 그리드로 텍스트 위치 정하기
# root = tk.Tk()
# root.title("레이아웃 실습")
# root.geometry("800x600")
#
# label1 = tk.Label(root, text="안녕하세요")
# label1.grid(row=0, column=3)    # grid : 가상의 공간에서 텍스트 위치를 지정
#                                 # column=3 : 왼쪽을 기준으로 가로 0-1-2-3 칸중 가로 4번째 위치에 둠
#                                 # row=0 : 세로 기준 0-1-2-3 기준에서 첫번째 위치에 둠
#
# label2 = tk.Label(root, text="반갑습니다")
# label2.grid(row=1, column=2, columnspan=2) # columnspan=2 : 칸 합치기 라고 생각 하면됨. 원래는 가로칸 0-1-2-3 4칸 중에서 3번째 칸에 들어가야하지만  columnspan를 통해 3번째와 4번째가 합쳐진 중간 위치에 텍스트를 둔다
#
# label3 = tk.Label(root, text="소통해요")
# label3.grid(row=2, column=1)
#
# label4 = tk.Label(root, text="파이썬하이")
# label4.grid(row=3, column=2)
#
#
# root.mainloop()

#--------------------------------------
# 레이아웃 - 3) 플레이스로 텍스트 위치 지정

# root = tk.Tk()
# root.title("레이아웃 실습")
# root.geometry("800x600")
#
# label1 = tk.Label(root, text="안녕하세요")
# label1.place(x=0, y=0)   # 픽셀 단위 지정  X축 = 좌표값  Y축=좌표값
#
# label2 = tk.Label(root, text="반갑습니다")
# label2.place(x=0, y=100)
#
# label3 = tk.Label(root, text="소통해요")
# label3.place(x=0, y=200)
#
# label4 = tk.Label(root, text="파이썬하이")
# label4.place(x=0, y=300)
#
# label5 = tk.Label(root, text="하하하하")
# label5.place(x=0, y=400)
#
# root.mainloop()



#--------------
#(실습하기1)

root = tk. Tk()
root.title("회원가입 창")
root.geometry("500x200")

# 아이디 입력창 만들기
id_label = tk.Label(root, text="아이디 : ")
id_label.grid(row=0, column=0, pady=10) # row : 가로,   colume : 세로,   pad : 여백 y축

id_entry = tk.Entry(root)   # 한줄 입력창 생성
id_entry.grid(row=0, column=1, padx=5) # pad : 여백 x축

# 새로운 메세지박스 띄우기1
def dupl_click():
    tk.messagebox.showinfo("중복확인", "중복환인 되었습니다.")  # 새로운 확인 창을 띄움

# 버튼 생성1
dupl_btn = tk.Button(root, text="ID중복확인", command=dupl_click)
dupl_btn.grid(row=0, column=2)

# 비밀번호 입력창 만들기
password_label = tk.Label(root, text="비밀번호 : ")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")   # show : 입력받는 텍스트를 *로 보여지게함
password_entry.grid(row=1, column=1, padx=5) # pad : 여백 x축

# 체크박스 생성
chk_var = tk.IntVar()
chk = tk.Checkbutton(root, text="약관 내용에 동의 합니다.", variable=chk_var)
chk.grid(row=2, column=1)

# 선택되는 체크옵션에 따른 실행 조건문
def signup_click():
    if chk_var.get() == 0:
        chk_value = "동의 안함"
    else:
        chk_value = "동의함"
    tk.messagebox.showinfo("회원가입 완료", f"아이디:{id_entry.get()}\n 약관동의:{chk_value}")  #\n 다음줄에 띄워라
    # 메세지박스2 생성

# 버튼생성2
signup_btn = tk.Button(root, text="회원가입", command=signup_click)
signup_btn.grid(row=3, column=2)


root.mainloop()