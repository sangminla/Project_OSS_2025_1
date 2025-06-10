import tkinter as tk
from tkinter import simpledialog, messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x450")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '구속 계산']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        elif char == '구속 계산':
            self.calculate_pitch_speed_time()
            return
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_pitch_speed_time(self):
        try:
            # 속도 입력 (단위: km/h)
            speed_kmh = simpledialog.askfloat("구속 입력", "공의 속도를 입력하세요 (km/h):")
            if speed_kmh is None:
                return
            if speed_kmh <= 0:
                raise ValueError("속도는 0보다 커야 합니다.")

            distance = 18.44  # 투수-포수 거리 (미터)
            speed_mps = speed_kmh * 1000 / 3600  # km/h → m/s
            time = distance / speed_mps  # 도달 시간 (초)

            self.expression = f"{time:.2f}초"

        except Exception as e:
            messagebox.showerror("오류", f"입력 오류: {e}")
            self.expression = ""
cd
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
