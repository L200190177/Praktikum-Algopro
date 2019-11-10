Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Kiki Nur Indah Sari'
>>> NIM = 177
>>> Tinggi = 1.60
>>> Berat = 48
>>> TahunLahir = 2000
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # merupakan tipe tuple yang berisi sekumpulan data yang memuat TahunLahir, Berat, Tinggi, NIM, dan Nama dan tipe data tuple tidak dapat diubah
>>> Aku [0]
2000
>>> # menampilkan elemen tuple indeks ke-0 yaitu TahunLahir atau data 2000
>>> a = NIM % 4; Aku[a]
48
>>> # karena hasil sisa bagi dari variabel NIM dengan 4 adalah 0 dan disimpan dalam variabel a kemudian Aku[a] akan menjadi Aku[1] dimana akan menampilkan elemen tuple Aku indeks ke-1 atau Berat
>>> type(Aku[a])
<class 'int'>
>>> # elemen tuple Aku indeks ke 1(1 merupakan data dari variabel a) atau Berat adalah 48
>>> Aku[a:4]
(48, 1.6, 177)
>>> # menampilkan elemen dari tuple Aku mulai dari indeks ke-1 hingga sebelum indeks ke-4 yang berisi Berat, Tinggi dan NIM
>>> type(Aku[4])
<class 'str'>
>>> # elemen tuple Aku indeks ke-4 merupakan data tipe string karena berisi Nama
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # terjadi tipe eror karena data tipe tuple tidak dapat diubah sedangkan program ingin mengubah elemen tuple indeks ke-0 dari TanggalLahir menjadi 'ok' maka terjadi tipe error
>>> type(Data)
<class 'list'>
>>> # karena variabel Data merupakan tipe list karena berisi sekumpulan data atau karakter dan data dalam list dapat diubah
>>> type(Data[4])
<class 'str'>
>>> # karena elemen list indeks ke-4 atau yang berisi Nama merupakan data yang bertipe string karena mengandung karakter
>>> Data[4][5]
'N'
>>> # karena elemen list indeks ke-4 atau yang berisi Nama kemudian program akan menjadi Nama[5] atau indeks ke-5 dari data yang telah disimpan dalam variabel Nama yaitu huruf N
>>> Data[4][a:6]
'iki N'
>>> # karena elemen list Data indeks ke-4 yang berisi Nama kemudian program akan menjadi Nama[a:6] dimana a berisi data 1 maka akan menjadi Nama[0:6] yang akan meampilkan elemen list indeks ke-1 hingga sebelum indeks ke-6 yaitu iki N
>>> Data[0] = 'ok'; Data
['ok', 48, 1.6, 177, 'Kiki Nur Indah Sari']
>>> # karena elemen list Data indeks ke-0 diubah dari TanggalLahir menjadi 'ok' dan kemudian program menampilkan data dari list Data
>>> Data[-a]
'Kiki Nur Indah Sari'
>>> # karena variabel a berisi data 1 maka program menjadi Data[-1] yang akan menampilkan elemen list Data indeks ke-(-1)
>>> range(a)
range(0, 1)
>>> # karena range adalah (0) dan program akan menampilkan range dari 0 hingga 1 atau jika ditulis dalam program range(0, 1)
