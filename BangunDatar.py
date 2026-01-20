# Daftar bangun datar yang didukung (minimal 4 jenis)
daftar_bangun =["1.persegi", "2.persegi panjang", "3.segitiga", "4.lingkaran"]



def luaspersegi(sisi):
    return sisi * sisi
def kelilingpersegi(sisi):
    return 4 * sisi
# Tambahkan fungsi untuk bangun datar lain
def luaspersegipanjang(panjang, lebar):
    return panjang * lebar
def kelilingpersegipanjang (panjang,lebar):
    return 2 * (panjang + lebar)
def luassegitiga(alas, tinggi):
    return (alas * tinggi) / 2
def kelilingsegitiga(s1, s2, s3):
    return s1 + s2 + s3
def luaslingkaran(jari2):
    return 3.14 * jari2 * jari2
def kelilinglingkaran(jari2):
    return 2 * 3.14 * jari2
nama = input("masukkan nama anda:") 

print(nama, " ,selamat datang di program Bangung datar")
print("pillih bangun datar:")
daftar_bangun_datar = ["1. persegi", "2.persegi panjang", "3.segitiga", " 4.lingkaran"]
for item in daftar_bangun_datar:
    print (item) 
while True:
    pilihan = int(input("masukan pilihan anda(1-4): "))    
    if   pilihan == 1:
        sisi = int(input("masukkan sisi persegi: ")) 
        print("luas persegi adalah:",luaspersegi(sisi))
        print("keliling persegi adalah:",kelilingpersegi(sisi))
        break # keluar loop setelah hitung selesai
    elif pilihan == 2:
        print("Anda Memilih Persegi Panjang")
        panjang = int(input("masukan panjang: "))
        lebar = int(input("masukkan lebar: "))
        print("luas persegi panjang adalah:", luaspersegipanjang(panjang,lebar))
        print("keliling persegi panjang:", kelilingpersegipanjang(panjang,lebar))
        break
    elif pilihan == 3:
        print("aAnda Memilih Segitiga")
        alas = int(input("Masukan Alas:"))
        tinggi = int(input("Masukan Tinggi: "))
        print("luas segitiga adalah:",luassegitiga(alas, tinggi))
        s1 = int(input("masukan sisi 1:"))
        s2 = int(input("masukan sisi 2:"))
        s3 = int(input("masukan sisi 3"))
        print("keliling segitiga adalah:",kelilingsegitiga(s1, s2, s3))
        break
    elif pilihan == 4:
        print("Anda Memilih Lingkaran")
        jari2 = int(input("masukan jari-jari: "))
        print("luas lingkaran adalah:",luaslingkaran(jari2))
        print("keliling lingkaran adalah:",kelilinglingkaran(jari2))
        break
    else:
        print("pilihan tidak tersedia")
        break


   
        
        

    
    

    