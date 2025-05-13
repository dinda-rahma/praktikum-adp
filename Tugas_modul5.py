A=["No. Pelanggan"]
B=["Nama Pelanggan"]
C=["Total Belanja"]

x=True    
while x:
    print(" ")
    print ("Menu utama :","    1. Tambah Data","    2. Hapus Data","    3. Cetak Data","    4. Keluar",sep="\n")
    pilihan = int(input("Pilih Menu : "))

    if pilihan==1:
        print(" ","Tambah Data ",sep="\n")
        nomor=input("   No. Pelanggan : ")
        A.append(nomor)
        nama=input("   Nama Pelanggan : ")
        B.append(nama)
        total=input("   Total Belanja :")
        C.append(total)
        print(" ","Data berhasil ditambahkan!",sep="\n")

    elif pilihan==2:
        print("Hapus Data")
        h=int(input("   No Pelanggan yang ingin dihapus : "))
        A.pop(h)
        B.pop(h)
        C.pop(h)
        print(" ","Data berhasil dihapus!",sep="\n")

    elif pilihan==3:
        print(" ")
        print("Data Pelanggan")
        print(" ")
        n=len(A)
        if n>1:
            for i in range (n):
                print(f"{A[i]:<20} {B[i]:<20} {C[i]:<20}")
        else:
            print("Data kosong, silahkan tambahkan data")
            
    elif pilihan==4:
        print("Terimakasih telah menggunakan program ini.")
        x=False