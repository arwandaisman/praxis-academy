def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries 
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
#finction di atas dapat kita panggil dengan cara berikut
ask_ok('Do you really want to quit?') #default
ask_ok('OK to overwrite the file?', 2) #retris dirubah menjadi 2
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!') #reminder diganti


i = 5
def f(arg=i):
    print(arg)
i = 6
f()
#akan tetap muncul 5 karena i=6 berada dibawah function

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3)) 

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#isi dari array L akan terus bertambah saat function f dijalankan