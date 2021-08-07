# -*- coding: utf-8 -*-
import time, os
import codecs

# Hiệu ứng loading
from time import sleep

# while True:
#     ns = input("Nhập ngày tháng năm sinh của bạn: \n")
#     # Nếu Nhập Đúng
#     # thay cả trên này nữa nha cả 2 cái trên và dưới thay giống nhau
#     if ns == "31/03/2007":
#         print("Chính Xác !!!")
#         time.sleep(1)
#         # lệnh thoát vòng lặp khi nhập đúng
#         break
#     # Nếu Nhập Sai
#     else:
#         ns_2 = input("Bạn nhập sai rồi ! Nhập lại nào: \n")
#         # các bạn chỉnh ngày sinh tùy ý nhé !
#         if ns_2 == "31/03/2007":
#             print("Chính Xác !!!")
#         else:
#             print("Bạn nhập sai rồi ! Thoát")
#             exit()
#         time.sleep(1)
#         # lệnh tiếp tục vòng lặp khi nhập key sai
#         break
# time.sleep(3)
os.system("clear")
# time.sleep(2)
print("          ██╗      ██████╗  █████╗ ██████╗ ██╗███╗   ██╗ ██████╗ ")
print("          ██║     ██╔═══██╗██╔══██╗██╔══██╗██║████╗  ██║██╔════╝ ")
print("          ██║     ██║   ██║███████║██║  ██║██║██╔██╗ ██║██║  ███╗")
print("          ██║     ██║   ██║██╔══██║██║  ██║██║██║╚██╗██║██║   ██║")
print("          ███████╗╚██████╔╝██║  ██║██████╔╝██║██║ ╚████║╚██████╔╝")
print("          ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝ ")
print("")


def loadbar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill="█"):
    percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    # print(f'\r{prefix} |{bar}| {percent}% {suffix}', end='\r')
    print('{} |{}| {}% {}'.format(prefix, bar, percent, suffix), end='\r')
    if iteration == total:
        print('')


items = list(range(0, 50))
l = len(items)

loadbar(0, l, prefix='Progress:', suffix='Complete', length=l)
for i, item in enumerate(items):
    sleep(0.1)
    loadbar(i + 1, l, prefix='Progress:', suffix='Complete', length=l)
print("\n")
time.sleep(2)

with codecs.open('unicode.rst', encoding='utf-8') as f:
    for line in f:
        print(repr(line))
        time.sleep(0.1)
