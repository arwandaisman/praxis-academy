# Errors and Exceptions.

Error adalah sebuah kesalahan dimana tidak sesuai dengan ketentuan yang ada, sedangkan exceptions adalah cara penyampaian pesan dari error.
contoh:
```
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
```