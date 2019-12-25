import os
from apoteker import *
choice = 0
while True :
    print(50*"=")
    print(10*" ","APOTEKER PTYHON PERCOBAAN")
    print(50*"=")
    print("1. USER")
    print("2. ADMIN")
    print("3. EXIT")
    print(50*"=")
    choice = (int)(input("PILIH : "))
    if(choice == 1):
        userMenu()
    elif(choice == 2):
        adminMenu()
    elif(choice == 3):
        print("TERIMA KASIH TELAH MENGGUNAKAN APLIKASI INI!!!")
        os.system(exit())
    else :
        print("MENU YANG ANDA MASSUKAN SALAH!!!")
        break