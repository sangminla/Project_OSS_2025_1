import datetime
import json
from expense import Expense
from collections import defaultdict

class Budget:
    def __init__(self):
        self.expenses = []
        self.goals = {}

    def add_expense(self, category, description, amount):
        today = datetime.date.today().isoformat()
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("지출이 추가되었습니다.\n")

    def list_expenses(self):
        if not self.expenses:
            print("지출 내역이 없습니다.\n")
            return
        print("\n[지출 목록]")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print()

    def total_spent(self):
        total = sum(e.amount for e in self.expenses)
        print(f"총 지출: {total}원\n")

    # ✅ 카테고리별 예산 목표 설정
    def set_goals(self):
        print("이번 달 카테고리별 지출 목표를 설정합니다.")
        categories = set(e.category for e in self.expenses)
        if not categories:
            print("먼저 지출 항목을 1개 이상 등록해주세요.\n")
            return

        for cat in categories:
            try:
                amount = int(input(f"- {cat} 목표 금액(원): "))
                self.goals[cat] = amount
            except ValueError:
                print("⚠️ 숫자만 입력해주세요.")
        print("✅ 예산 목표가 설정되었습니다.\n")

    # ✅ 목표 대비 지출 분석
    def analyze_goals(self):
        if not self.goals:
            print("❌ 설정된 목표가 없습니다. 먼저 예산 목표를 설정해주세요.\n")
            return
        if not self.expenses:
            print("❌ 지출 내역이 없습니다.\n")
            return

        actual = defaultdict(int)
        for e in self.expenses:
            actual[e.category] += e.amount

        print("\n📊 카테고리별 목표 달성 현황:")
        for cat, goal in self.goals.items():
            spent = actual.get(cat, 0)
            percent = spent / goal * 100 if goal > 0 else 0
            status = "🔺초과" if spent > goal else "✅정상"
            print(f"- {cat}: {spent:,}원 / {goal:,}원 ({percent:.1f}%) {status}")
        print()
