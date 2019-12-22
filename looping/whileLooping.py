#Basic While Looping
#while(True):
    #jalankan perintah looping
    #jalankan perintah looping
#steatment ini berada di luar looping
akhir = 10;
print(30*"=")
while(akhir <= 10):
    akhir-=1
    print("Nilai i adalah ",akhir)
    if akhir == 0:
        break

#Special For Looping
print(30*"=")
daftarMenu = ["BAKSO","SOTO","MIE AYAM","NASI GORENG","MAGELANGAN"]
while(daftarMenu) :
    print(daftarMenu)
    if(len(daftarMenu)):
        break
print(30*"=")
start = True
i = 0
while (start):
    print("Nilai dari i adalah ",i)
    i+=1
    if(i == 10):
        start = False
print(30*"=")