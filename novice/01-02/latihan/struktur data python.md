# **Struktur Data Pada Bahasa Python**

ipe data daftar list memiliki beberapa metode lagi. Berikut ini semua metode dari objek daftar list:

list.append(x)

    Tambahkan item ke akhir daftar list. Setara dengan a[len(a):] = [x].

list.extend(iterable)

    Perpanjang daftar list dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable.

list.insert(i, x)

    Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum memasukkan, jadi a.insert(0, x) memasukkan di bagian depan daftar list, dan a.insert(len(a), x) sama dengan a.append(x).

list.remove(x)

    Hapus item pertama dari daftar list yang nilainya sama dengan x. Ini memunculkan ValueError jika tidak ada item seperti itu.

list.pop([i])

    Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar. (Tanda kurung siku di sekitar i dalam pengenal signature metode menunjukkan bahwa parameternya opsional, bukan Anda harus mengetik tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)

list.clear()

    Hapus semua item dari daftar list. Setara dengan del a[:].

list.index(x[, start[, end]])

    Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menimbulkan ValueError jika tidak ada item seperti itu.

    Argumen opsional start dan end ditafsirkan seperti dalam notasi slice dan digunakan untuk membatasi pencarian ke urutan tertentu dari daftar. Indeks yang dikembalikan dihitung relatif terhadap awal urutan penuh daripada argumen start.

list.count(x)

    Kembalikan berapa kali x muncul dalam daftar.

list.sort(key=None, reverse=False)

    Urutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan ubahsuaian customization, lihat sorted() untuk penjelasannya).

list.reverse()

    Balikkan elemen daftar list di tempatnya.

list.copy()

    Kembalikan salinan daftar list yang dangkal. Setara dengan a[:].


Contoh yang menggunakan sebagian besar metode daftar list:
```

>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2

>>> fruits.count('tangerine')
0

>>> fruits.index('banana')
3

>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6

>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

>>> fruits.pop()
'pear'

```

## Menggunakan Daftar Lists sebagai Tumpukan *Stacks*

Untuk menambahkan item ke atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit. Sebagai contoh: 

```
>>> stack = [3, 4, 5]
>>> stack.append(6)
>>> stack.append(7)
>>> stack
[3, 4, 5, 6, 7]
>>> stack.pop()
7
>>> stack
[3, 4, 5, 6]
>>> stack.pop()
6
>>> stack.pop()
5
>>> stack
[3, 4]
```

## Menggunakan Daftar Lists sebagai Antrian *Queues*

```
rom collections import deque
>>> queue = deque(["Eric", "John", "Michael"])
>>> queue.append("Terry")           # Terry arrives
>>> queue.append("Graham")          # Graham arrives
>>> queue.popleft()                 # The first to arrive now leaves
'Eric'
>>> queue.popleft()                 # The second to arrive now leaves
'John'
>>> queue                           # Remaining queue in order of arrival
deque(['Michael', 'Terry', 'Graham'])
```

## Daftar List Comprehensions

Pemahaman daftar list comprehensions menyediakan cara singkat untuk membuat daftar.
```
>>> squares = []
>>> for x in range(10):
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

```

## Pernyataan del

Cara untuk menghapus item dari daftar yang diberikan indeksnya, bukan nilainya: pernyataan del. Ini berbeda dari metode pop() yang mengembalikan nilai. Pernyataan del juga dapat digunakan untuk menghapus irisan dari daftar list atau menghapus seluruh daftar list
```
>>> a = [-1, 1, 66.25, 333, 333, 1234.5]
>>> del a[0]
>>> a
[1, 66.25, 333, 333, 1234.5]
>>> del a[2:4]
>>> a
[1, 66.25, 1234.5]
>>> del a[:]
>>> a
[]
```

## Tuples and Urutan Sequences

Sebuah tuple terdiri dari sejumlah nilai yang dipisahkan oleh koma, misalnya:

```
>>> t = 12345, 54321, 'hello!'
>>> t[0]
12345
>>> t
(12345, 54321, 'hello!')
>>> # Tuples may be nested:
... u = t, (1, 2, 3, 4, 5)
>>> u
((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
>>> # Tuples are immutable:
... t[0] = 88888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> # but they can contain mutable objects:
... v = ([1, 2, 3], [3, 2, 1])
>>> v
([1, 2, 3], [3, 2, 1])

```

## *Set*

Fungsi set() dapat digunakan untuk membuat himpunan. Untuk membuat himpunan kosong kita harus menggunakan set(), bukan {}
```
>>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
>>> print(basket)                      # show that duplicates have been removed
{'orange', 'banana', 'pear', 'apple'}
>>> 'orange' in basket                 # fast membership testing
True
>>> 'crabgrass' in basket
False

>>> # Demonstrate set operations on unique letters from two words
...
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

## Dictionaries
Melakukan list(d) pada kamus mengembalikan daftar list semua kunci yang digunakan dalam kamus, dalam urutan penyisipan (jika kita ingin mengurutkan, cukup gunakan sorted(d) sebagai gantinya). Untuk memeriksa apakah ada satu kunci dalam kamus, gunakan kaca kunci in

```
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
>>> tel['jack']
4098
>>> del tel['sape']
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'guido': 4127, 'irv': 4127}
>>> list(tel)
['jack', 'guido', 'irv']
>>> sorted(tel)
['guido', 'irv', 'jack']
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

Pembangun constructor dict() membangun kamus langsung dari urutan pasangan kunci-nilai:
```
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

## Teknik Perulangan
```
items() -> mengambil key dan value dengan waktu yang sama

enumerate() -> mengambil posisi dan value dengan waktu yang sama

zip() -> mengulang dua urutan atau lebih secara bersamaan

reversed() -> mengulang urutan secara terbalik

```

## Perbandingan

Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa pun, bukan hanya perbandingan.

Operator perbandingan in dan not in memeriksa apakah suatu nilai terjadi (tidak terjadi) secara berurutan. Operator is dan is not membandingkan apakah dua objek benar-benar objek yang sama. 

Perbandingan bisa dibuat berantai. Sebagai contoh, a < b == c menguji apakah a kurang dari b dan apa b sama dengan c.

Perbandingan dapat digabungkan menggunakan operator Boolean and dan or, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not. Ini memiliki prioritas lebih rendah daripada operator pembanding; di antara mereka, not memiliki prioritas tertinggi dan or terendah, sehingga A and not B or C setara dengan (A and (not B)) or C . Seperti biasa, tanda kurung dapat digunakan untuk mengekspresikan komposisi yang diinginkan.

Operator Boolean and dan or disebut operator short-circuit: argumen mereka dievaluasi dari kiri ke kanan, dan evaluasi berhenti segera setelah hasilnya ditentukan.