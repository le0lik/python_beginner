from sys import argv

try:
    script_name, pay_hours, pay_per_hour, pay_extra = argv
except ValueError:
    script_name = argv
    print(f"Неправильный формат вызова скрипта\n"
          f"{script_name} <Выработка в часах> <Ставка в час> <Премия>")
    exit(-1)

print(f"Выработка в часах = {pay_hours}\nСтавка в час = {pay_per_hour}\n"
      f"Премия = {pay_extra}\nИтого зарплата = {(float(pay_hours) * float(pay_per_hour)) + float(pay_extra)}")
