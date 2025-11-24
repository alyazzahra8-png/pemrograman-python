# 1. Minta input dari pengguna
# kita gunakan try_except untuk menangani jika pengguna memasukkan selain angka
try:
    angka_input = int(input("masukkan sebuah bilangan (maks 7 digit): "))
 
    # 2. proses perhitungan nilai tempat
    # Asumsi berdasarkan contoh, kita batasi hingga 7289450
    if 0 <= angka_input <= 7289450:
        
        # Ambil nilai jutaan
        jutaan = angka_input // 1000000
        # Hitung sisa setelah diambil jutaannya
        sisa_jutaan = angka_input % 1000000
        _
        # Ambil nilai ratus ribuan
        ratus_ribuan = sisa_jutaan // 100000
        # Hitung sisa setelah diambil ratus ribuannya
        sisa_ratus_ribuan = sisa_jutaan % 100000
        
        # Ambil nilai puluh ribuan
        puluh_ribuan = sisa_ratus_ribuan // 10000
        # Hitung sisa setelah diambil puluh ribuannya
        sisa_puluh_ribuan = sisa_ratus_ribuan % 10000
        
        # Ambil nilai ribuan
        ribuan = sisa_puluh_ribuan // 1000
        # Hitung sisa setelah diambil ribuannya
        sisa_ribuan = sisa_puluh_ribuan % 1000
        
        # Ambil nilai ratusan
        ratusan = sisa_ribuan // 100
        # Hitung sisa setelah diambil ratusannya
        sisa_ratusan = sisa_ribuan % 100
        
        # Ambil nilai puluhan
        puluhan = sisa_ratusan // 10 
        # Hitung sisa setelah diambil puluhannya
        satuan = sisa_ratusan % 10
        
        # 3. Tampilkan hasil sesuai format
        print(f"\nAnda memasukkan bilangan {angka_input} dimana;")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratus_ribuan} merupakan ratus ribuan")
        print(f"{puluh_ribuan} merupakan puluh ribuan")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")
    
    else:
         print("Harap masukkan bilangan antara 0 dan 1000000.")
         
except ValueError:
    print("Input tidak valid Harap masukkan angka saja")