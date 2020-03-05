# **CRC Card**

| Order                                           |             |
|-------------------------------------------------|-------------|
| harga  |  pelanggan |
| persediaan | |
| nama barang | |
| pembayaran| |


# **OOP di Python**

## Classes
Contoh sederhana :

Kita simpan dengan nama oop_simplestclass.py
```
class Person:
    pass  # An empty block

p = Person()
print(p)
```
Output
```
$ python oop_simplestclass.py
<__main__.Person instance at 0x10171f518>
```
Class adalah sebuah entitas dari Methods.

## Methods

Methods adalah sebuah function yang ada didalam class.

Contoh: 
```
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
```

Contoh diatas berisikan class Person denhan method sau_hi. 

## Method Init 
pada pemrograman python terdapat sebuah method dengan nama __init__(), Fungsi Method Init Pada Pemrograman Python yaitu merupakan method yang pertama kali di jalankan atau di proses sebelum method-method yang lainnya dan method __init__() berguna untuk melakukan inisialisasi pembuatan object dari class.

perbedaan method init dan method yang lainya yaitu, jika method pada umumnya untuk mengakses method tersebut kita harus memanggil nama methodnya, nah sedangkan  method init kita tidak perlu memanggil nama methodnya dan secara otomatis proses yang terdapat di dalam method tersebut akan di jalankan.

## Class And Object Variables 

**Class Variabel** -> dibagi - mereka dapat diakses oleh semua instance dari kelas itu. Hanya ada satu salinan variabel kelas dan ketika salah satu objek membuat perubahan ke variabel kelas, perubahan itu akan dilihat oleh semua instance lainnya.

**Object Variabel** -> dimiliki oleh setiap objek individu / instance dari kelas.


## Inheritance/pewarisan


---
---


# Python standard library 1 

Modul os menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi.
```
>>> import os
>>> os.getcwd()      # Return the current working directory
'C:\\Python38'
>>> os.chdir('/server/accesslogs')   # Change current working directory
>>> os.system('mkdir today')   # Run the command mkdir in the system shell
0
```

Modul shutil menyediakan antarmuka level yang lebih tinggi yang lebih mudah digunakan.
```
>>> import shutil
>>> shutil.copyfile('data.db', 'archive.db')
'archive.db'
>>> shutil.move('/build/executables', 'installdir')
'installdir'

```

Modul glob menyediakan fungsi untuk membuat daftar berkas dari pencarian wildcard di direktori.
```
>>> import glob
>>> glob.glob('*.py')
['primes.py', 'random.py', 'quote.py']
```
Modul sys memproses argumen baris perintah.
```
import sys
>>> print(sys.argv)
```
Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Script berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional untuk ditampilkan.
```
import argparse

parser = argparse.ArgumentParser(prog = 'top',
    description = 'Show top lines from each file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)
args = parser.parse_args()
print(args)
```
Modul re menyediakan alat ekspresi reguler untuk pemrosesan string lanjutan. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan.
```
>>> import re
>>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
['foot', 'fell', 'fastest']
>>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
'cat in the hat'
```

Modul math memberikan akses ke fungsi-fungsi pustaka C yang mendasari untuk matematika angka pecahan floating point:

```
>>> import math
>>> math.cos(math.pi / 4)
0.70710678118654757
>>> math.log(1024, 2)
10.0
```

Modul random menyediakan alat untuk membuat pilihan acak
```
>>> import random
>>> random.choice(['apple', 'pear', 'banana'])
'apple'
>>> random.sample(range(100), 10)   # sampling without replacement
[30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
>>> random.random()    # random float
0.17970987693706186
>>> random.randrange(6)    # random integer chosen from range(6)
4

```

Modul statistics menghitung sifat statistik dasar (rata-rata, median, varian, dll.) dari data numerik:

```
>>> import statistics
>>> data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
>>> statistics.mean(data)
1.6071428571428572
>>> statistics.median(data)
1.25
>>> statistics.variance(data)
1.3720238095238095
```