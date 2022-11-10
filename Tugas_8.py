from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

def cetak(i):
    if (i+1)%2==0:
       print(i+1, "Genap - ID proses", getpid())
    else:
       print(i+1, "Ganjil - ID proses", getpid())
    sleep(1)

a=int(input("Masukkan batas perulangan: "))

# Sekuensial
sekuensial_awal = time()
print("Sekuensial")
for i in range(a):
    cetak(i)
sekuensial_akhir = time()

# Multiprocessing dengan Kelas Process
process_awal = time()
print("multiprocessing.Process")
for i in range(a):
    p=Process(target=cetak, args=(i, ))
    p.start()
    p.join()
process_akhir = time()

# Multiprocessing dengan Kelas Pool
pool_awal = time()
pool = Pool()
print("multiprocessing.Pool")
pool.map(cetak, range(0,a))
pool.close()
pool_akhir = time()

# Membandingkan waktu eksekusi
print("Waktu eksekusi sekuensial : ", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process : ", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool : ", pool_akhir - pool_awal, "detik")
