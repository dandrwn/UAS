from view.input_nilai import *

def ubah():
    milih = input("masukkan data yang akan diubah : ")
    if milih == "nim":
        nim3 = str(input("masukkan nim :"))
        nim4 = str(input("masukkan nim yang baru :"))
        for i in range(len(nim)):
            if nim3 == nim[i]['nim']:
                nim[i]['nim'] = nim4
    elif milih == "nama":
        nama3 = str(input("masukkan nama :"))
        nama4 = str(input("masukkan nama yang baru :"))
        for i in range(len(nama)):
            if nama3 == nama[i]['nama']:
                nama[i]['nama'] = nama4
    elif milih == "tugas":
        tugas3 = str(input("masukkan nilai tugas :"))
        tugas4 = str(input("masukkan nilai tugas yang baru :"))
        for i in range(len(tugas)):
            if tugas3 == tugas[i]['tugas']:
                tugas[i]['tugas'] = tugas4
    elif milih == "uts":
        uts3 = input("masukkan nilai uts :")
        uts4 = input("masukkan nilai uts yang baru :")
        for i in range(len(uts)):
            if uts3 == uts[i]['uts']:
                uts[i]['uts'] = uts4
    elif milih == "uas":
        uas3 = str(input("masukkan nilai uas : "))
        uas4 = input("masukkan nilai uas yang baru :")
        for i in range(len(uas)):
            if uas3 == uas[i]['uas']:
                uas[i]['uas'] = uas4

def hapus():
    nim3 = input("masukan nim : ")
    for i in range(len(nim)):
        if nim3 == nim[i]['nim']:
            del nim[i]
    nama3 = input("masukan nama : ")
    for i in range(len(nama)):        
        if nama3 == nama[i]['nama']:
             del nama[i]
    tugas3 = input("masukan tugas : ")
    for i in range(len(tugas)):         
        if tugas3 == tugas[i]['tugas']:
            del tugas[i]
    uts3 = input("masukan uts : ")
    for i in range(len(uts)):        
        if uts3 == uts[i]['uts']:
             del uts[i]
    uas3 = input("masukan uas : ")
    for i in range(len(uas)):         
        if uas3 == uas[i]['uas']:
             del uas[i]     

def keluar():
    print("pilihan yang anda masukkan tidak ada")