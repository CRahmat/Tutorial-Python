import os
#Input User
from builtins import int

a = (eval(input("Massukan Nilai a = ")))
b = (eval(input("Massukan Nilai b = ")))
#Python tidak memperhatikan tipe data atau tipe data dalam python sudah otomatis
#Jadi jika terdapat variable bernilai double maka python sudah mengenalinya dengan otomatis
print("------------------ OPERATOR ARITMATIKA ------------------ ")
#Penjumlahan
c = a+b
print("Hasil Penjumlahan %d + %d adalah = %d" % (a,b,c))
#Pengurangan
c = a-b
print("Hasil Pengurangan %d - %d adalah = %d" % (a,b,c))
#Perkalian
c = a*b
print("Hasil Perkalian %d * %d adalah = %d" % (a,b,c))
#Pembagian
c = a/b
print("Hasil Pembagian %d / %d adalah = %d" % (a,b,c))
#MOD
c = a%b
print("Sisa Hasil Bagi %d %% %d adalah = %d" % (a,b,c))
#Pemangkatan
c = a**b
print("Hasil Perpangkata %d ** %d adalah = %d" % (a,b,c))
#Pada contoh diatas, kita menggunakan string formatting(%)
os.system('CLS')
print("------------------ OPERATOR PENUGASAN ------------------ ")
a = (eval(input("Massukan Nilai a = ")))
#Tambahkan a dengan 10
a += 2
print("Hasil dari Penugasan Penambahan dengan 2 adalah = ",a)
a -= 2
print("Hasil dari Penugasan Pengurangan dengan 2 adalah = ",a)
a *= 2
print("Hasil dari Penugasan Perkalian dengan 2 adalah = ",a)
a /= 2
print("Hasil dari Penugasan Pembagian dengan 2 adalah = ",a)
a **= 2
print("Hasil dari Penugasan Pemangkatan dengan 2 adalah = ",a)
os.system('CLS')

print("------------------ OPERATOR PEMBANDING ------------------ ")
a = (eval(input("Massukan Nilai a = ")))
b = (eval(input("Massukan Nilai b = ")))
#Apakah a sama dengan b
c = a == b
print("Apakah %d == %d = %r" %(a,b,c))
c = a > b
#Apakah a > b
print("Apakah %d > %d = %r" %(a,b,c))
#Apakah a < b
c = a < b
print("Apakah %d < %d = %r" %(a,b,c))
#Apakah a >= b
c = a <= b
print("Apakah %d >= %d = %r" %(a,b,c))
#Apakah a <= b
c = a >= b
print("Apakah %d <= %d = %r" %(a,b,c))
#Apakah a tidak sama dengan b
c = a != b
print("Apakah %d != %d = %r" %(a,b,c))
os.system('CLS')

print("------------------ OPERATOR TERNARY ------------------ ")
#Operator ternary sebenarnya tidak ada dalam python, namun python pnya cara untuk menggantikannnya dengan ? dan :

#<nilai true> if Kondisi else <nilai false>
umur = eval(input("Massukan Umur anda = "))
umur = "Anak Anak" if(umur <= 10) else "Dewasa"
print("Anda Tergolong Dalam = ",umur)

#Sekian