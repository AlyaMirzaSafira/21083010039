from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

# Inisialisasi Fungsi yang akan digunakan:
def cetak(i):
	print("Cetak angka", i+1, "-punya ID proses", getpid())
	sleep(1)

# 1-Pemrosesan Sekuensial
print("1-Pemrosesan Sekuensial")
## Untuk mendapatkan waktu sebelum ekseskusi
sekuensial_awal = time()
## Pemrosesan berlangsunh
for i in range (10):
	cetak(i)
## Untuk mendapatakan Waktu Setelah Eksekusi
sekuensial_akhir = time()
print()


## 2-Multiprocessing dengan kelas Process:
print("2-Multiprocessing dengan kelas Process")
## Untuk menampung proses-proses
kumpulan_proses = []
## Untuk mendapatkan waktu sebelum eksekusi
process_awal = time()
##Proses berlangsung
for i in range(10):
	p = Process(target=cetak, args=(i,))
	kumpulan_proses.append(p)
	p.start()
## untuk menggabungkan proses-proses agar tidak loncat ke proses sebelumnya
for i in kumpulan_proses:
	p.join()
## Untuk mendapatkan waktu setelah eksekusi 
process_akhir= time()
print()


## 3 -Multiprocessing debgan Kelas Pool:
print("3-Multiprocessing dengan kelas Pool")
## Untuk mendapatkan waktu sebelum eksekusi
pool_awal = time()
##Proses berlangsung
pool =  Pool()
pool.map(cetak, range(0, 10))
pool.close
## Untuk mendapatkan waktu setelah eksekusi
pool_akhir = time()
print()

## Membandingakabn waktu eksekusi:
print("Perbandingan waktu Eksekusi")
print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pol :", pool_akhir - pool_awal, "detik")

