from view.input_nilai import *

def lihat():
    print("============================================")
    print("nim \t nama \t tugas \t uts \t uas \t akhir")
    print("============================================")
    for i in range(len(nim)):
        print(nim[i]['nim'], '\t', nama[i]['nama'], '\t', tugas[i]['tugas'], '\t', uts[i]['uts'], '\t',uas[i]['uas'], '\t', akhir[i]['akhir'], '\t')
        ops = False

def cari():
    cari = input("masukan data yang dicari : ")
    if cari == "nim":
        for i in range(len(nim)):
            print(nim[i]['nim'])
    elif cari == "nama":
        if cari == "nama":
            for i in range(len(nama)):
                print(nama[i]['nama'])
    elif cari == "tugas":
        if cari == "tugas":
            for i in range(len(tugas)):
                print(tugas[i]['tugas'])
    elif cari == "uas":
        if cari == "uas":
            for i in range(len(uas)):
                print(uas[i]['uas'])
    elif cari == "uts":
        if cari == "uts":
            for i in range(len(uts)):
                print(uts[i]['uts'])
    elif cari == "akhir":
        if cari == "akhir":
            for i in range(len(akhir)):
                print(akhir[i]['akhir'])
    else:
            print("data yang anda cari tidak ada")