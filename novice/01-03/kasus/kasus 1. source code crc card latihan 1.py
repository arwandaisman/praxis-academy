class buku:
    jumlahBuku = 0
    def __init__(self, no_buku, nama_buku, pengarang):
        self.no_buku = no_buku
        self.nama_buku = nama_buku
        self.pengarang = pengarang
        buku.jumlahBuku = buku.jumlahBuku+1
    def lihat_buku(self):
        print("Data Buku : ")
        print("Nomor Buku : ", self.no_buku)
        print("Nama Buku : ", self.nama_buku )
        print("Nama Pengarang : ", self.pengarang)
        print("--------------------------------------")

buku1 = buku("001", "Apapun yang Kau Mau ", "Arwanda")
buku1.lihat_buku()

buku2 = buku("002", "Makan dan Minum", "Isman")
buku2.lihat_buku()

print("Jumlah buku yang ada saat ini : ", buku.jumlahBuku)

    
