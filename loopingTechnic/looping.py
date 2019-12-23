#tekhnik Looping

bandName = ['Payung Teduh',
            'NOAH',
            'Fourtwenty',
            'Didi Kempot',
            'Guyon Waton'
            ]
songTitle = ['Untuk Perempuan Yang Sedang Dalam Pelukan',
             'Separuh Aku',
             'Zona Nyaman',
             'Pamer Bojo',
             'Korban Janji'
             ]
#=======================================================================================================================
#print list
no = 1
for band in bandName:
    print(no, "Nama Band : ", band)
    no+=1
print(80*"=")

#Enumerate
for i,band in enumerate(bandName):
    print(i,"Nama Band : ", band)

#Menggabungkan List (zip)
#Jika ukurannya berbeda maka tidak akan ditampilkan
#ZIP menggabungkan list dengan index
for band, title in zip(bandName,songTitle):
    print("Nama Band ",band, " Dengan Lagu Berjudul ", title)
#=======================================================================================================================
#Looping Set tidak menggunakn index
playlist = {'Separuh Aku','Korban Janji','Jaran Goyang','Belahan Jiwa'}
#print tidak berurutan dan tidak sesuai urutan
for song in playlist:
    print("Playlist ",song)
print(80 * "=")
#print tidak berurutan dan tidak sesuai urutan
for song in sorted(playlist) :
    print("Playlist ",song)
#=======================================================================================================================
print(80 * "=")
#Looping Dictionary
playlist2 = {'Payung Teduh':'Untuk Perempuan Yang Sedang Dalam Pelukan',
            'NOAH':'Separuh Aku',
            'Fourtwenty': 'Zona Nyaman',
            'Didi Kempot': 'Pamer Bojo',
            'Guyon Waton': 'Korban Janji'
}

#print all items
for band,song in playlist2.items() :
    print(band,song)
print(80 * "=")
#print index
for band in playlist2.values() :
    print(band)
print(80 * "=")
#print keys
for band in playlist2.keys() :
    print(band)
print(80 * "=")