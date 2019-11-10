## Program Akun
## Dibuat oleh Kiki Nur Indah Sari L200190177
import random
angka = random.randint(0,1000)

Nama = 'Kiki Nur Indah Sari'
TanggalLahir = '9 Oktober 2000'
NamaSingkat = Nama[0] + '- ' + Nama[5] + '- ' + Nama[15:19]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[10:14]
Password = Nama[0:3] + str(angka)

print(Nama)
print(TanggalLahir)
print(NamaSingkat)
print(Username)
print(Password)
