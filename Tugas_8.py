from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# Input batas perulangan
batas = int(input("Masukkan batas perulangan : "))
print()
# Inisialisasi Fungsi yang akan dgunakan:
def cetak(i):
	for i in range(1, batas+1):
	   if i %2 == 1:
	     print(i, "Ganjil", "-ID proses", getpid()) 
	     continue
	   print(i, "Genap", "-ID proses", getpid())
	sleep(1)
# 1-Pemrosesan sekuensial
print("Sekuensial")
## Untuk mendapatkan waktu sebelum eksekusi
sekuensial_awal = time()
## Proses berlangsung
for i in range(1):
	cetak(i)
## Untuk mendapatkan waktu setelah eksekusi
sekuensial_akhir = time()
print()


# 2- Multiprocessing dengan kelas Process
print("Multiprocessing.Process")
## Untuk menampung proses-proses
kumpulan_proses = []
## untuk mebdapatkan waktu sebelum eksekusi
process_awal =  time()
## proses berlangsung
for i in range(1):
	p = Process(target=cetak, args=(i, ))
	kumpulan_proses.append(p)
	p.start()
## Untuk menggabungkan proses-proses agar tidak  loncat ke proses sebelumnya
for  i in kumpulan_proses:
	p.join()
## Untuk mendapatkan waktu setelah eksekusi
process_akhir = time()
print()


# 3-Multiprocessing dengan kelas Pool
print("Multiprocessing.Pool")
# Untuk mendapatkan waktu sebelum eksekusi
pool_awal = time()
## proses berlangsung
pool = Pool()
pool.map(cetak, range(0,1))
pool.close()
## untuk mendapatkan waktu setelah eksekusi
pool_akhir = time()
print()

# perbandingan waktu eksekusi
print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu multiprocessing.Pool", pool_akhir - pool_awal, "detik")

