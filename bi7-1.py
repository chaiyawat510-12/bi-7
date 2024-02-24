income = float(input("กรุณาระบุรายได้ (บาท): "))

if income >= 15000 and income < 20000:
    creditcard = "บัตร Sliver"
elif income < 100000:
    creditcard = "บัตร Gold"
else:
    creditcard = "บัตร Platinum"

print(f"รายได้ของคุณ {income:.2f} บาท สามารถทำ{creditcard} ได้")