import calendar

year = 2025

for month in range(1, 13):
    print(f"\n{year}년 {month}월")
    print("일 월 화 수 목 금 토")
    cal = calendar.monthcalendar(year, month)
    for week in cal:
        print(" ".join(f"{day:2d}" if day != 0 else "  " for day in week))

    print("-" * 20)
# This code prints the calendar for each month of the year 2025 in a formatted manner.
# Each month is displayed with the days of the week in Korean.dddddddd

# The output includes the year and month header, followed by the days of the week and the dates aligned properly.
# 내주민번호 입력 했는데
print("프로그램 종료")

# 랜덤 메일 주소 생성 함수
import random
import string

def generate_random_email():
    letters = random.choices(string.ascii_letters, k=8)
    digits = random.choices(string.digits, k=4)
    local_part = ''.join(letters + digits)
    email = f"{local_part}@naver.com"
    return email

print("랜덤 메일 주소:", generate_random_email())
print("프로그램 종료")


