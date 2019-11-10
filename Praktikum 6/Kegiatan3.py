Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Kiki Nur Indah Sari'
>>> NIM = 'L200190177'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # variabel a merupakan data tipe integer karena telah diubah dari data tipe string menjadi data tipe integer
>>> type(b)
<class 'int'>
>>> # variabel b merupakan data tipe integer karena data tersebut mengandung intruksi len yang mana len adalah jumlah anggota dari suatu objek
>>> a / b
61.94736842105263
>>> # merupakan data yang bertipe float karena 1177 dibagi 19 menghasilkan bilangan float 61.94736842105263 atau mengandung nilai desimal
>>> a // b
61
>>> # merupakan data yang bertipe integer karena hasil bagi dari 1177 dibagi 19 yang hasilnya 61.94736842105263 dibulat kan kebawah menjadi 61 yang bertipe integer, karena data bertipe integer dibagi data bertipe integer maka menghasilkan data bertipe integer pula
>>> 10 * (a - 999)
1780
>>> # merupakan data yang bertipe integer , karena data dari variabel a dikurang 999 adalah 178 dan kemudian dikalikan dengan 10 menghasilkan data 1780
>>> b ** 2
361
>>> # merupakan data yang bertipe integer , karena data dari variabel b pangkat kan 2 atau 19 pangkat 2 yang menghasilkan data 361
>>> a % b
18
>>> # merupakan data yang bertipe integer , karena simbol % merupakan sisa hasil bagi dari data variabel a dibagi data variabel b atau sisa hasil bagi dari 1177 dibagi 19 yaitu 18
>>> c = 12.5
>>> # data 12.5 disimpan dalam variabel c
>>> type(c)
<class 'float'>
>>> # variabel c merupakan data float karena mengandung nilai desimal
>>> a / c
94.16
>>> # merupakan data bertipe float karena data variabel a dibagi dengan data variabel c sama dengan 94.16 atau 1177 dibagi 12.5 menghasilkan data 94.16 yang bertipe float atau bernilai desimal
>>> a // c
94.0
>>> # merupakan data yang bertipe float karena dalam variabel c mengandung data bertipe float maka hasil pembagian dibulatkan kebawah dari variabel data bertipe integer dibagi variabel data bertipe float adalah data bertipe float (1177 dibagi 12.5 dan dibulatkan ke bawah menghasilkan data 94.0)
>>> a % c
2.0
>>> # merupakan data yang bertipe float karena sisa hasil bagi(%) antara data variabel a(1177) dengan data variabel c(12.5) menghasilkan 2.0 yang mengandung nilai desimal
>>> c > b
False
>>> # merupakan data yang bertipe boolean yang bernilai atau berkondisi False karena data variabel c (12.5) lebih kecil dari data variabel b (19) sedangkan dalam program ditulis data variabel c lebih besar dari pada data variabel b maka menghasilkan kondisi atau nilai False
>>> type(c > b)
<class 'bool'>
>>> # merupakan data yang bertipe boolean yang memiliki 2 kondisi atau nilai yaitu True dan False , merupakan operator logika
>>> a > b and b > c
True
>>> # merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > b bernilai True dan b > c bernilai True juga , dalam operator 'and' apabila kedua data memiliki nilai True maka menghasilkan data bernilai True
>>> a > 1100 or b < 10
True
>>> # merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > 1100 bernilai True dan b < 10 bernilai False , dalam operator 'or' apabila salah satu memiliki nilai True maka menghasilkan data bernilai True juga
