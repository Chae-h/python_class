# 파이썬 18회차 2번째
# 로그인창 만들기

import tkinter as tk
from tkinter import messagebox

# 가상의 데이터 베이스
user_db = {}
# {}딕셔너리는 키:값으로 되어 있다.
# id : 비번



root = tk.Tk()
root.title("로그인")
root.geometry("360x350")

# 기본구성 - 아이디 라벨 및 입력칸 만들기
id_label = tk.Label(root, text="아이디:")
id_label.grid(row=0, column=0, pady=10, padx=5)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

# 기본구성 - 비밀번호 라벨 및 입력칸 만들기
password_label = tk.Label(root, text="비밀번호:")
password_label.grid(row=1, column=0, pady=10, padx=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1)

# 기능1 - 로그인
def login():
    user_id = id_entry.get().strip()    # strip() : 문자열 양쪽 공백 제거
    user_pw = password_entry.get().strip()

    if not user_id or not user_pw:
        messagebox.showwarning("경고", "아이디나 비밀번호를 입력해 주세요")
    elif user_id not in user_db:
        messagebox.showerror("에러", "존재하지 않는 아이디 입니다.")
    elif user_db.get(user_id) == user_pw:   # user_db[user_id] == user_pw
          # 정상적으로 키와 값이 맞을때 (미리 키에러 뜰것을 방지)
        messagebox.showinfo("고르인 성공", f"{user_id}님 반갑습니다.")
    else:
        messagebox.showerror("에러", "비밀번호가 맞지 않습니다.")


# 기본구성 로그인 버튼 만들기 및 기능추가
login_btn = tk.Button(root, text="로그인", command=login)
login_btn.grid(row=2, column=1)

def signup_click():
    signup_screen = tk.Toplevel(root) # tk.Toplevlel(root) 창위에 창을 띄움
    signup_screen.title("회원가입")
    signup_screen.geometry("400x200")

    # 아이디 입력
    signup_id_label = tk.Label(signup_screen, text="아이디:")
    signup_id_label.grid(row=0, column=0, pady=10, padx=5)
    signup_id_entry = tk.Entry(signup_screen)
    signup_id_entry.grid(row=0, column=1)

    # 비밀번호 입력
    signup_password_label = tk.Label(signup_screen, text="비밀번호:")
    signup_password_label.grid(row=1, column=0, pady=10, padx=5)
    signup_password_entry = tk.Entry(signup_screen, show="*")
    signup_password_entry.grid(row=1, column=1)

    def register():
        user_id = signup_id_entry.get().strip()
        user_pw = signup_password_entry.get().strip()

        user_db[user_id] = user_pw
        messagebox.showinfo("회원가입 완료", "정상적으로 회원가입이 완료되었습니다.")
        signup_screen.destroy()


    # 회원가입 버튼
    submit_btn = tk.Button(signup_screen, text="회원가입", command=register)
    submit_btn.grid(row=2, column=1)

# 회원가입 버튼
signup_btn = tk.Button(root, text="회원가입", command=signup_click)
signup_btn.grid(row=3, column=1)

root.mainloop()