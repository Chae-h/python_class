# 파이선(18회차)

# 1. to do list 만들기
# 2. 로그인창 만들기

# 1교시--------------------

# 1. to do list 만들기

# [[기획/설계 하기]]
# 1. 할 일 추가
# 2. 할 일 제거
# 3. 할 일 목록
# 4. 할 일 수정
# 5. 할 일 전체 제거
# 6. 할 일 저장
# 7. 할 일 불러오기

import tkinter as tk
from operator import index
from tkinter import messagebox

import json
SAVE_FILE = "save.json"  # 상수변수 : 변경될 일이 없다고 선언하는 변수(대문자)

import os

# 2. 기능 만들기
# 기능1 : 추가 버튼
def add_todo():
    todo = to_do_entry.get()   # to_do_entry = tk.Entry 에서 입력 받는 값을 가져온다.
    if todo:        # to_do_entry = tk.Entry 에 입력 받은 데이터가 있다면
        to_do_list_box.insert(tk.END, todo) # to_do_list_box에 담을 것이다. # (tk.END, todo)는 맨 끝에 입력받은 todo를
        to_do_entry.delete(0, tk.END) # 입력칸에서 입력받은 내용을 자동 지움 (이것을 안해 놓으면 매번 커서위치에서 삭제하고 사용자가 입력해야함)
    else:   # 데이터를 입력하지 않고 추가 버튼을 눌렀다면
        messagebox.showwarning("경고", "할 일을 입력하세요!") # 추가창을 띄운다. 창 이름은 "경고", 메세지는 " 할일을 입력하세요"

# 기능2 : 삭제 버튼
def remove_todo():
    try:
        todo = to_do_list_box.curselection()  # 선택된 것들이 튜플 형태로 가져온다.
        if not todo:
            raise IndexError # 선택된것이 없이 삭제를 누르면 인덱스 에러를 발생 선택
        to_do_list_box.delete(todo[0]) # 문제가 없으면 인덱스 0번을 삭제한다.
    except IndexError:
        messagebox.showwarning("경고", "삭제할 할 일을 선택하세요!")

# 기능3 : 전체 삭제 버튼
def clear_todo():   # 전체삭제
    if to_do_list_box.size() == 0:   # 리스트의 항목 갯수를 들고 온다. 만약에 0개면 아무것도 없는것
        messagebox.showwarning("경고", "삭제할 할 일이 없습니다!") # 삭제할 데이터가 없으면 에러 발생시키기
    else:
        to_do_list_box.delete(0, tk.END) # (0, tk.END) 처음부터 끝까지 삭제

# 기능4 : 저장하기
def save_todo():
    todo_list = to_do_list_box.get(0, tk.END)  # to_do_list_boxd의 데이터를 튜플 형태로 다 들고옴
    try:
        with open(SAVE_FILE, "w", encoding="utf-8")as file:
            json.dump(todo_list, file, indent=4, ensure_ascii=False)   # indent=4 들여쓰기 4칸, ensure_ascii=False 아스키코드 안함
        messagebox.showinfo("저장완료", "저장이 완료되었습니다!")

    except Exception as e:  # 저장 오류가 발생시
        messagebox.showerror("오류", f"저장 중 오류 발생:{e}")

# 기능5 : 불러오기
def load_todo():
    if os.path.exists(SAVE_FILE): # 같은 경로에 저장 파일이 있다면
        try:
            with open(SAVE_FILE, "r", encoding="utf-8")as file:
                todo_list = json.load(file)
                if not isinstance(todo_list, list):     # isinstance(todo_list, list) : todo_list안의 클래스로 만든 객채가 list형태로 되어 있는가? 라고 물어보는 명령어
                    raise ValueError("올바른 형식이 아닙니다.")
                if to_do_list_box.size() != 0:     # to_do_list_box.size() 항목안의 갯수가 만약에 리스트 박스에 0개가 아니면(!=)
                    clear_todo() # 리스트 클리어
                for todo in todo_list:
                    to_do_list_box.insert(tk.END, todo)
        except (json.JSONDecodeError, ValueError):      # JSONDecoder : 불러오는데 읽기 형태가 올바르지 않을 경우(파일이 깨진경우)
            messagebox.showerror("오류", "파일 데이터가 손상 되었습니다!")
        except Exception as e:
            messagebox.showerror("오류", f"불러오기 중 오류 발생:{e}")
    else:
        messagebox.showwarning("경고", "불러올 저장 파일이 없습니다!")


# 1.창 기본 구성
root = tk.Tk() # tk : 명령어 root : 창을 뜻
root.title("TO DO LIST") # 창 이름
root.geometry("400x500") # 창 크기

# 입력칸 및 버튼 만들기
# 입력칸
to_do_entry = tk.Entry(root, width=40)
to_do_entry.pack(pady=10)  # pady=10 픽셀 여백 y축

# 버튼1
btn_frame = tk.Frame(root)  # 버튼을 담을 가상의 틀 생성
btn_frame.pack() # 입력칸인 to_do_entry.pack 밑에 쌓인다.

add_btn = tk.Button(btn_frame, text="추가", width=10, command=add_todo)  # btn_frame 가상프레임안에 위치한다 # command=add_todo  프로그램 연결
add_btn.grid(row=0, column=0) # row=0 : 세로 기준 0-1-2-3~ 기준에서 첫번째 위치에 둠
                              # column=0 : 왼쪽을 기준으로 가로 0-1-2~ 칸중 가로 첫번째 위치에 둠

remove_btn = tk.Button(btn_frame, text="삭제", width=10, command=remove_todo)
remove_btn.grid(row=0, column=1, padx=20)

clear_btn = tk.Button(btn_frame, text="전체 삭제", width=10, command=clear_todo)
clear_btn.grid(row=0, column=2)

# 목록 담는칸 만들기
to_do_list_box = tk.Listbox(root, width=50, height=20, selectmode="extended")
# width 가로  height 세로 설정
# 기능 : browse : 하나만 선택(클릭으로) "기본값 : 입력하지 않아도  browse으로 자동실행"
#       selectmode="single"(스페이스바)
#       selectmode="extended" : 여러개 선택(쉬프트와 컨트롤 키를 누른상태 이용. 전체 선택 또는 개별 선택)
#       selectmode="multiple" : 클릭 할 때마다 선택 및 중복선택/해제가 가능
to_do_list_box.pack(pady=10) #pack 칸의 여백 설정

# 버튼2
btn_frame2 = tk.Frame(root)   # 저장과 불러오기 버튼을 담을 가상의 프레임 생성
btn_frame2.pack()

save_btn = tk.Button(btn_frame2, text="저장", command=save_todo)
save_btn.grid(row=0, column=0, padx=20)

load_btn = tk.Button(btn_frame2, text="불러오기", command=load_todo)
load_btn.grid(row=0, column=1, padx=20)


root.mainloop() # 창 실행


