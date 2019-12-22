nilai = (int)(input("Massukan nilai Anda : "))
#Nesting If
if(nilai<=100):
    if(nilai == 100): #Equals
        print("Nilai Anda Sangat Baik!!!")
        print("Anda Lulus Dalam Ujian Ini!!!")
        if(80 <= nilai <= 100):
            print("Anda mendapatkan nilai A")
        if (70 <= nilai <= 80):
            print("Anda mendapatkan nilai B")
        if (50 <= nilai <= 70):
            print("Anda mendapatkan nilai C")
        if (40 <= nilai <= 50):
            print("Anda mendapatkan nilai D")
            print("Anda disarankan untuk mengulang ujian ini!!!")
        if(0 <= nilai <= 40):
            print("Nilai Anda Terlalu Buruk!!!")
            print("Anda Wajib Mengulang Kuliah Ini!!!")
    elif(nilai>=100):
        print("Nilai Yang Anda Massukan Salah!!!")
    elif(nilai<0):
        print("Nilai Yang Anda Massukan Salah!!!")
else:
    print("Anda Tidak LULUS!!!")

#condition in python tidak menggunakan kurung kurawal melainkan dengan memperhatikan posisinya
#Steatment dari condition berada pada 1 tab dari condition