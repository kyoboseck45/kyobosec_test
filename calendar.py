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
# Each month is displayed with the days of the week in Korean.dddd