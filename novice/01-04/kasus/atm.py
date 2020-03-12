class Deposit:
    def tambah(self, deposit = 0):
        d = deposit
        print("Masukkan Nominal : ", end = "Rp ")
        d = int(input())
        saldo = saldo + d


class Wihtdraw:
    def kurang(self, wihtdraw = 0):
        w = wihtdraw
        print("Masukkan Nominal : ", end = "RP ")
        w = int(input())
        saldo = saldo - w

class Balance:
    def cek(self, balance = 0):
        b = balance
        print("Saldo yang anda miliki : RP ", saldo)

class ATMMachine:
    def menunya():
    print ("""
    "----------- PILIH MENU ----------"
    "[1] Menabung"
    "[2] Menarik"
    "[3] Cek Saldo"
    "[4] Exit"
    """)
    menu = input("PILIH MENU> ")
     
    if menu == 1:
        jumlah = Deposit.tambah()
    elif menu == 2:
        jumlah = Wihtdraw.kurang()
    elif menu == 3:
        jumlah = Balance.cek()
    elif menu == 4:
        exit()
    else:
        print "Salah pilih!"

saldo = 0
p = ATMMachine.menunya()

print(p)