nim = []
nama = []
tugas = []
uts = []
uas = []
akhir = []
pilihan = True

def tambah():
    nim1 = input("masukkan nim: ")
    nim.append({'nim': nim1})
    nama1 = input("masukkan nama: ")
    nama.append({'nama': nama1})
    tugas1 = input("masukkan nilai tugas: ")
    tugas.append({'tugas': tugas1})
    uts1 = input("masukkan nilai UTS: ")
    uts.append({'uts': uts1})
    uas1 = input("masukkan nilai UAS: ")
    uas.append({'uas': uas1})
    akhir1 = 0.3 * float(tugas1) + 0.35 * float(uts1) + 0.35 * float(uas1)
    akhir.append({'akhir': akhir1})
    pilihan == False