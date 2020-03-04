# **I/O pada Python**

Ada beberapa cara untuk mempresentasikan output suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang.

**A.  Fancier Output Formatting**

Saat ini ada 2 cara menuilskan function print():

+ Untuk menggunakan string literal yang diformat, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda bisa menulis ekspresi Python antara karakter {dan} yang bisa merujuk ke variabel atau nilai literal.

+ Metode str.format () dari string membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan {dan} untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.

---

- Formatted String Literals   

- The String format() Method

    Basic usage of the str.format() method looks like this:


```
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

- Manual String Formatting

Ini adalah tabel kotak dan kubus yang sama, yang diformat secara manual:

```
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     # Note use of 'end' on previous line
...     print(repr(x*x*x).rjust(4))
...
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
```


- Old string formatting

Operator % juga dapat digunakan untuk pemformatan string. Ini mengartikan argumen kiri seperti string format gaya sprintf () untuk diterapkan pada argumen yang benar, dan mengembalikan string yang dihasilkan dari operasi pemformatan ini. Sebagai contoh:

```
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

**B. Reading and Writing Files**


Open () mengembalikan objek file, dan paling umum digunakan dengan dua argumen: open (filename, mode).
```
>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```

- Methods of File Objects

Untuk membaca konten file, panggil f.read (size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner).
```
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''
```


- Saving structured data with json

Format JSON umumnya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Banyak programmer sudah terbiasa dengannya, yang menjadikannya pilihan yang baik untuk interoperabilitas.

If you have an object x, you can view its JSON string representation with a simple line of code:
```
>>> import json
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'

```



