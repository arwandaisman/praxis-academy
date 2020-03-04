# **Tutorial Python**

Python adalah bahasa pemrograman yang kuat dan mudah dipelajari. Ini memiliki struktur data tingkat tinggi yang efisien dan pendekatan yang sederhana namun efektif untuk pemrograman berorientasi objek. Sintaksis elegan dan pengetikan dinamis Python, bersama dengan sifatnya yang ditafsirkan, menjadikannya bahasa yang ideal untuk skrip dan pengembangan aplikasi yang cepat di banyak area di sebagian besar platform.

# BAB 1

Python mudah digunakan, tetapi ini adalah bahasa pemrograman nyata, menawarkan lebih banyak struktur dan dukungan untuk program besar daripada skrip shell atau file batch dapat menawarkan.

Python memungkinkan Anda untuk membagi program Anda menjadi modul yang dapat digunakan kembali di program Python lainnya. Muncul dengan koleksi besar modul standar yang dapat Anda gunakan sebagai dasar program Anda - atau sebagai contoh untuk mulai belajar memprogram dengan Python. Beberapa modul ini menyediakan hal-hal seperti file I / O, panggilan sistem, soket, dan bahkan antarmuka ke toolkit antarmuka pengguna grafis seperti Tk.

Python adalah bahasa yang ditafsirkan, yang dapat menghemat waktu Anda selama pengembangan program karena tidak diperlukan kompilasi dan penautan. Penerjemah dapat digunakan secara interaktif, yang membuatnya mudah untuk bereksperimen dengan fitur-fitur bahasa, untuk menulis program yang dibuang, atau untuk menguji fungsi selama pengembangan program dari bawah ke atas. Ini juga merupakan kalkulator meja yang berguna.

Python memungkinkan program ditulis secara ringkas dan mudah dibaca. Program yang ditulis dengan Python biasanya jauh lebih pendek daripada program C, C ++, atau Java yang setara, karena beberapa alasan:

1. tipe data tingkat tinggi memungkinkan Anda untuk mengekspresikan operasi yang kompleks dalam satu pernyataan;

2. pengelompokan pernyataan dilakukan dengan lekukan alih-alih tanda kurung awal dan akhir;

3. tidak ada deklarasi variabel atau argumen yang diperlukan.


# BAB 2
**Using the Python Interpreter**

Penerjemah Python biasanya diinstal sebagai /usr/local/bin/python3.8 pada mesin-mesin di mana tersedia; menempatkan / usr / local / bin di jalur pencarian Unix shell Anda memungkinkan untuk memulainya dengan mengetikkan perintah:

```
python3.8
```

```$ python3.8
Python 3.8 (default, Sep 16 2015, 09:25:04)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
untuk keluar dari interpreter dapat menggunakan perintah ctrl + D atau ctrl + Z, dan jika tidak bisa dapat mengetikkan perintah exit().


# BAB 3
**Python sebagai kalkulator**

ANGKA

operator yang digunakan : 

' + ' (penjumlahan) 

' - ' (pengurangan)

' * ' (perkalian)

' / ' (pembagian)

' // ' (pembagian dengan membuang bagian pecahan)

' % ' (sisa hasil bagi/modulo)

' ** ' (untuk melakukan pemangkatan)


> Dapat menggunakan variabel: 
```
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
**STRING**

Penulisan kalimat menggunakan ''

ex : 'saya makan'

apabila di tengah kata ada yang harus menggunakan ' maka dapat kita tulis dengan \'  

```
'do\'a'
```

atau dapat juga menggunakan ""

 ```
 "do'a"
 ```

didalam perntah \n adalah ganti baris ketika di cetak maka ketika ada perintah yang menggunakan \n 
```
'C:\some\name'
```
maka di awal kalimat sebelim ' kita beri r 
```
r'C:\some\name'
```

untuk menulis baris beberapa baris maka dapat kita gunakan """....""""

untuk menampilkan huruf di sebuah kata dapat kita gunakan array ([])
```
word = 'makanan'
```
untuk menampilkan huruf ke 5 maka kita dapat masukkna perintah word[4] 
array dimulai dari 0 

untuk menghutung panjang karakter disebuah kalimat dapat kita berikan perntah len(variabel kalimat)

LIST
```
>>> a = [1,2,3,4,5,6]
```
dapat kita panggil dengan perintah 
```
>>> a
```
untuk merubah salahsatu isi dari list di atas dapat kita masukkan perintah
```
>>>a[2]= 9 
[1,2,9,4,5,6]
>>>a[2:4]
[9,4]
```


# BAB 4

**More Control Flow Tools**







