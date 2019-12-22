#Basic For Looping
#for index in range(bankyak_perulangan)
    #jalankan perintah looping
    #jalankan perintah looping
#steatment ini berada di luar looping
akhir = 10;
print(30*"=")
for i in range(akhir):
    if(i == 6):
        print("Nilai anda saat ini adalah ",i)
        #break : untuk berhenti dari looping
        #continue : untuk melanjutkan ke steatment for
        #looping akan langsung kembali ke awal, dan steatment di bawahnya tidak di jalankan
    print("Nilai i adalah ",i)

#Special For Looping
print(30*"=")
daftarMenu = ["BAKSO","SOTO","MIE AYAM","NASI GORENG","MAGELANGAN"]
for i in daftarMenu :
    print(i)
print(30*"=")

akhir = 10;
for i in range(1,10):
    print("Nilai i adalah ",i)