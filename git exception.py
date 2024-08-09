#1
# try:
#     first = int(input("vvedite pervoye delimoye:  "))
#     second = int(input("vvedite vtoroye delimoye:  "))
#     result = first / second
#     print(result)
# except ZeroDivisionError:
#     print("chislo ne delitsa na nol")

#2
# try:
#     with open('21 test.txt' , 'r') as file:
#         reader = file.read()
#         print(reader)
# except FileNotFoundError:
#     print("file is not found")
# except FileExistsError:
#     print("may be file is not exsisting")

#3
# try:
#     chislo = int(input("vvedite chislo: "))
#     b = chislo / 100
#     print(b)
# except ZeroDivisionError:
#     print("chislo ravna 0 poprobuyte eshe raz")
#     chislo = int(input("vvedite chislo"))
# except ValueError:
#     print("pishite chisla pls")
#     chislo = int(input("vvedite chislo: "))

#4
# try:
#     with open('21 test.txt' , 'w') as file:
#         wr = input("vvedite sude svoy messege:  ")
#         writer = file.write(wr)
# except FileExistsError:
#     print("file mojet bit ne sushestvuet")
#     wr = input("vvedite sude svoy messege , poprobuyte eshe raz")
# except FileNotFoundError:
#     print("file ne nayden , poprobuyte eshe raz")
#     wr = input("vvedite sude svoy messege")

#5
# try:
#     a = input('vvedite chislo:  ')
#     number = int(a)
# except ValueError:
#     print("chto to poshlo ne tak poprobuyte eshe raz")
#     a = input('vvedite chislo:  ')
# else:
#     print(f"{number} podoydet")
# finally:
#     print("this is final text")