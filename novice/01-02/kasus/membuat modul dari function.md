# Membuat Modul dari Function

Modul Pertama dengan nama kasus1.py
```
def tukar(lists,i,j):
    lists[i],lists[j]=lists[j], lists[i]
    
def bubbleTugas(listku):
    perubahan = True
    sesi = len(listku) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j]<listku[j-1]:
                perubahan = True
                tukar(listku,j,j-1) 
            j+=1
        print(listku)
        #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
        if not perubahan:
            print("hasil akhir = %s" %str(listku))
        sesi-=1
print("==================================================================")
print("Sebelum Bubble Sort")
mylist=[54,26,13,93,17,77,44,31]
print(mylist)
print("Setelah Bubble Sort")
bubbleTugas(mylist)
```

Cara Menggunakan Modul 

```
import kasus1

kasus1.bubbleTugas(listku)
print('mylist',kasus1.__mylist__ )

```

Modul Kedua dengan nama quickshort.py
```
def quickshort(a,start,end):
    if start<end:
        pindex = partition(a,start,end)
        quickshort(a,start,pindex-1)
        quickshort(a,pindex+1,end)
 
def partition(a,start,end):
    middle = int(end/2)
    pivot = a[middle]
    pindex = start
    for i in range(start,middle):
        if a[i]>=pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex = pindex + 1
    a[pindex],a[middle]=a[middle],a[pindex]
    print(a)
    return pindex
 
a = [68,90,78,44,34,20,100,56,34,2]
quickshort(a,0,len(a)-1)
```

Cara Menggunakan Modul 

```
import quickshort

quickshort.bubbleTugas(listku)
print('a',quickshort.__a__ )

```
Modul Ketiga dengan nama SelectionSort.py
```
def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
SelectionSort(DaftarAngka)
print(DaftarAngka)
```

Cara Menggunakan Modul 

```
import SelectionSort

print('DaftarAngka', SelectionSort.__DaftarAngka__)
```
Modul Keempat dengan nama InsertionSort.py
```
def InsertionSort(val):
   for index in range(1,len(val)):
 
     valueaktif = val[index]
     posisi = index
 
     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1
 
     val[posisi]=valueaktif
 
DaftarAngka = [23,7,32,99,4,15,11,20]
InsertionSort(DaftarAngka)
print(DaftarAngka)
```

Cara Menggunakan Modul 

```
import InsertionSort

print('DaftarAngka', DaftarAngka.__DaftarAngka__)
```
Modul Kelima dengan nama BubbleSort.py
```
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)
print(DaftarAngka)
```

Cara Menggunakan Modul 

```
import BubbleSort

print('DaftarAngka', BubbleSort.__DaftarAngka__)
```