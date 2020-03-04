# **Modul dalam Pyton**

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py ditambahkan. Contoh kita membuat modul dengan nama fibo.py dengan konten:

```
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result
```

kemudian kita dapat panggil modul tersebut dengan perintah :
```
import fibo
```
Jika saat menggunakan modul maka kita harus panggil modul tersebut, contoh:

```
import sys
```
