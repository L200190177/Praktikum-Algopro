Data = {"NIM":"L200190177", "Nama":"Kiki Nur Indah Sari","Tempat/Tanggal lahir":"Klaten, 9 Oktober 2000", "Jenis Kelamin":"Perempuan", "Agama":"Islam", "Pekerjaan":"Mahasiswa", "Alamat":"Pencil, Bendo, Pedan, Klaten"}
def TampilNIM():
    print(Data["NIM"])
def TampilNama():
    print(Data["Nama"])
def TampilTTL():
    print(Data["Tempat/Tanggal lahir"])
def TampilJK():
    print(Data["Jenis Kelamin"])
def TampilAgama():
    print(Data["Agama"])
def TampilAlamat():
    print(Data["Alamat"])
def TampilPekerjaan():
    print(Data["Pekerjaan"])

print("Pilihan Yang Tersedia:")
print("a menampilakan bantuaan ini")
print("b menampilakan NIM")
print("c menampilakan Nama")
print("d menampilakan Tempat/Tanggal lahir")
print("e menampilakan Jenis Kelamin")
print("f menampilakan Agama")
print("g menampilakan Alamat")
print("h menampilakan Pekerjaan")
print("i untuk keluar")
print(" ")

a = """Pilihan Yang Tersededia:
a menampilakan bantuaan ini
b menampilakan NIM
c menampilakan Nama
d menampilakan Tempat/Tanggal lahir
e menampilakan Jenis Kelamin
f menampilakan Agama
g menampilakan Alamat
h menampilakan Pekerjaan
i untuk keluar"""

print(a)
i = "Terima Kasih"
x = input("Masukkan huruf:")
while x != "i":
    if x == "a":
        print(a)
        print(" ")
        x = input("Masukkan huruf:")
    elif x == "b":
        TampilNIM()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "c":
        TampilNama()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "d":
        TampilTTL()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "e":
        TampilJK()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "f":
        TampilAgama()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "g":
        TampilAlamat()
        print(" ")
        x = input("Masukkan huruf")
    elif x == "h":
        TampilPekerjaan()
        print(" ")
        x = input("Masukkan huruf")
print(i)
