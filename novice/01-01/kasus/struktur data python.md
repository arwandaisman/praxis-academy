# **Struktur Data Pada Bahasa Python**

Struktur data(SD) adalah cara mengatur dan menyimpan data sehingga dapat diakses dan dikerjakan dengan efisien [1], 
SD mendefinisikan hubungan antara data, dan operasi yang dapat dilakukan pada data.
SD pada dasarnya struktur yang dapat menyimpan beberapa data bersama, 
dengan kata lain, SD digunakan untuk menyimpan koleksi data terkait.

Ada empat struktur data bawaan di Python, list, tuple, dictionary, dan set [2] dan akan kita bahas satu per satu

## List
list / daftar adalah Struktur data pada Python yang digunakan untuk menyimpan koleksi item yang heterogen. List mampu menyimpan lebih dari satu data [3], seperti array. list dapat diisi dengan tipe data apa saja, string, integer, float, double, boolean, object, dan sebagainya. Kita juga bisa mencampur isinya, dan list bersifat mutable yang artinya isi nya bisa kita ubah.

Pada latihan hari ini, kita akan membahas cara menggunakan list di Python dari yang paling sederhana sampai yang sedikit kompleks.
* Cara Membuat List dan Mengisinya
* Cara Mangambil nilai dari List
* Cara Menambahkan dan Menghapus isi List
* Operasi pada List

#### Membuat list dan Mengisinya

```Python
# Membuat List kosong
warna = []

# Membuat list dengan isi 1 item
hobi = ["membaca"]

# Membuat list dengan isi 5 item
warna = ["merah", "kuning", "hijau", "Orange", "Biru"]
```
    
### Mangambil nilai dari List
```python
# Kita punya list nama-nama warna
warna = ["merah", "kuning", "hijau", "Orange", "Biru"]

# kita ingin mengambil warna Orange
# Maka indeknya adalah 3, karena index/urutan array dimulai dari angka 0
print (warna[3])
```
Akan menghasilkan output
    
    "Orange"

### Menambahkan Item List

Terdapat Tiga metode (method) atau fungsi yang bisa digunakan untuk menambahkan isi atau item ke List:

1. prepend(item) menambahkan item dari depan;
2. append(item) menambahkan item dari belakang.
3. insert(index, item) menambahkan item dari indeks tertentu

Contoh
##### 1. prepend
```python    
#list awal
warna = ["merah", "kuning", "hijau", "Orange", "Biru"]
#Tambahkan warna Coklat
warna.prepend("Coklat")
```    
Maka "Coklat" akan ditambahkan pada awal list.
```python
warna = [ "Coklat", "merah", "kuning", "hijau", "Orange", "Biru"]
```    
##### 2.append
```python
#list awal
warna = ["merah", "kuning", "hijau", "Orange", "Biru"]
#Tambahkan warna Coklat
warna.append("Coklat")
```    
Hasil output menjadi :
```python    
warna = ["merah", "kuning", "hijau", "Orange", "Biru", "Coklat"]
```
##### 3. insert
```python
#list awal
warna = ["merah", "kuning", "hijau", "Orange", "Biru"]

#Tambahkan warna Emas
warna.insert(3,"Emas")
 
#Maka warna Emas akan ditambahkan setelah Index array ke 3
    
warna = ["merah", "kuning", "hijau", "Emas", "Orange", "Biru"]
```    
    
### Menghapus List
Ketikan perintah del untuk menghapus lis
```python
#list awal
warna = ["merah", "kuning", "hijau", "Orange", "Biru"]
del warna[2] #menghapus warna pada array ke 2
print(warna)
```
hasilnya adalah
```python
warna = ["merah", "kuning", "Orange", "Biru"]
```
### Operasi List

Ada beberapa operasi yang bisa dilakukan terhadap List, diantaranya:

    Penggabungan (+)
    Perkalian (*)
Contoh:

```python
# Beberapa warna
list_warna = [
    "Merah",
    "kuning",
    "Hijau"
    ]

# lagu pelangi
lagu_pelangi= [
    "Pelangi",
    "Pelangi"
]

# Mari kita gabungkan keduanya
lagu = lagu_pelangi + list_warna

print(lagu)
```

Hasilnya
```python
[pelangi,pelangi,merah,kuning,hijau]
```
Sedangkan untuk operasi perkalian hanya dapat dilakukan dengan bilangan.
Contoh:
```python
list_a=["pelangi","merah"]
b = list_a * 7 # kalikan list sebanyak 7 x

print(b)
```
Hasilnya
```python
['pelangi', 'merah', 'pelangi', 'merah', 'pelangi', 'merah', 'pelangi', 'merah', 'pelangi', 'merah', 'pelangi', 'merah', 'pelangi', 'merah'] 
```
## Tuple
Tuple dalam Python adalah stuktur data yang digunakan untuk menyimpan sekumpulan data. Tupe bersifat immutable, artinya isi tuple tidak bisa kita ubah dan hapus. Namun, dapat kita isi dengan berbagai macam nilai dan objek.

Hari ini kita akan membahas:

1. Cara Membuat Tuple
2. Cara Mengakses Nilai Tuple
3. Slicing Nilai Tuple

### Cara Membuat Tuple di Python

Tuple biasanya dibuat dengan tanda kurung kecil ()
```python
tpl = (1234,9876, "Hello python")
# Atau Bisa Juga Tanpa Kurung
tpl = 1234,9876, "Hello python"
```
### Cara Akses Nilai Tuple
Sama seperti list, Tuple juga memiliki indeks untuk Mengakses item di dalamnya. 
Indeks pada Tuple dan list selalu dimulai dari nol 0.
```python
tpl = (1234,9876, "Hello python")
print(tpl[2])
```
Hasilnya
```python
Hello Python
```
### Sliching pada tuple
```python
tpl = (1234,9876, "Hello python")
# lalu kita ingin potong agar ditampilkan
# dari indeks nomer 1 sampai 2
print(tpl[1:2])
```
Hasilnya
```python
(9876,)
```
## Set
Set adalah struktur data berisi kumpulan data tak terurut (unordered). Set bersifat mutable, kita dapat menambah maupun
mengurangi data yang ada di dalamnya. Elemen di dalam set harus unik, tidak boleh ada duplikasi elemen pada set. Elemen di
dalam set harus berupa eleman yang immutable, setiap elemen yang ada tidak boleh berubah (bedakan dengan set-nya sendiri yang
mutable). Ini berarti, Elemen set hanya dapat berupa string, number, dan tuple [4].

#### daftar pustaka

1. https://www.datacamp.com/community/tutorials/data-structures-python
2. https://python.swaroopch.com/data_structures.html
3. https://www.petanikode.com/python-list/
4. https://koding.alza.web.id/struktur-data-set/
