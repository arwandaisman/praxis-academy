# **Latihan 5**
## **DDL dan DML**

**DDL (Data Definition Language)**

Mendefinisikan struktur database :
 - CREATE
 - RENAME
 - ALTER
 - DROP

**DML(Data Manipulation Language)**

 Manipulasi atau pengolahan data dalam table :

 - SELECT
 - INSERT
 - DELETE
 - UPDATE

---
## Membuat Database Baru
---
> Membuat database dengan nama latihan5
```
CREATE DATABASE latihan5;
```

> Menggunakan database latihan5
```
USE latihan5;
```


> Membuat tabel baru
```
CREATE TABLE anggota(
    -> no_id VARCHAR(5) PRIMARY KEY,
    -> nama VARCHAR(50) NOT NULL,
    -> alamat TEXT NOT NULL,
    -> no_hp VARCHAR(15)
    -> );
```

> Mengisikan data tabel

```
INSERT INTO anggota VALUES('00001', 'Arwanda Isman', 'Sleman', '082242903653');
```
> Tambah data
```
INSERT INTO anggota VALUES('00002', 'Rizki Baskara Putra', 'Gunung Kidul', '');

INSERT INTO anggota VALUES('00003', 'Muhammad Aziz Shobari', 'Sleman', '');

INSERT INTO anggota VALUES('00004', 'Mansyur Sallim', 'Cilacap', '');
```

> Menampilkan data dari tabel
```
SELECT * FROM anggota;
```

> Hasil

```
+-------+-----------------------+--------------+--------------+
| no_id | nama                  | alamat       | no_hp        |
+-------+-----------------------+--------------+--------------+
| 00001 | Arwanda Isman         | Sleman       | 082242903653 |
| 00002 | Rizki Baskara Putra   | Gunung Kidul |              |
| 00003 | Muhammad Aziz Shobari | Sleman       |              |
| 00004 | Mansyur Sallim        | Cilacap      |              |
+-------+-----------------------+--------------+--------------+

```





