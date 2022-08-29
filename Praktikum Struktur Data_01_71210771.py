#71210711 - Christophorus Adyatma
from ast import Break

while True:
    hasil=0

    print("KALKULATOR")
    print("Pilih Menu: \n1. Tambah \n2. Kurang \n3. Kali \n4. Bagi")

    
    pilih = str(input("Pilihan Anda: "))

    if pilih == "1":
        
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        hasil=angka1+angka2
    elif pilih=="2":
        
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        hasil=angka1-angka2
    elif pilih=="3":
        
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        hasil=angka1*angka2
    elif pilih=="4":
        
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))
        hasil=angka1/angka2
    elif pilih =="Q":
        break
        
    
    print("Hasil :",hasil)

