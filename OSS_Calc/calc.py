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

        # 버튼 정의
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', '음속']
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
        elif char == '음속':
            self.calculate_sound_travel_time()
            return
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def calculate_sound_travel_time(self):
        try:
            # 거리 입력 (단위는 m)
            distance = simpledialog.askfloat("소리 도달 시간 계산", "거리를 입력하세요 (미터 단위):")
            if distance is None:
                return  # 사용자가 취소
            if distance < 0:
                raise ValueError("음수는 안 됩니다.")

            sound_speed = 340.0  # m/s
            time = distance / sound_speed
            self.expression = f"{time:.2f}초"

            # ✅ 결과를 GUI에 출력
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.expression)

        except Exception as e:
            messagebox.showerror("오류", f"입력 오류: {e}")
            self.expression = ""
