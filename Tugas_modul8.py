catatan = {}
x = True
while x:
    print("===== MENU UTAMA =====")
    print("1. Lihat catatan","2. Buat catatan baru","3. Exit", sep="\n")
    pilihan=int(input("Pilihan menu : "))
    

    if pilihan==1:
        f = open ('catatan.txt','r')
        print ("== LIST JUDUL ==","silhakan pilih judul catatan yang ingin anda buka",sep="\n")
        print()
        for judul,isi in catatan.items():
            print (f"- {judul}\n")
        pilih = input("judul catatan : ")
        if pilih in catatan:
            print("isi catatan : ",catatan[pilih])
            print()
        else :
            print()
            print("(catatan tidak ditemukan)")
            print()
    elif pilihan==2:
        f = open ('catatan.txt','a')
        # for judul,isi in catatan:
        judul = str(input ("Judul catatan : "))
        isi = input (" isi catatan : ")
        catatan[judul] = isi
        f.write(f"Judul : {judul}")
        f.write(f"\nIsi : {isi}\n")
        f.close()
        print()
        print ("catatan anda sudah ditambahkan!")
        print ()
    elif pilihan==3:
        x = False
        f=open ('catatan.txt','w')
        f.close()
        print()
        print ("Terimakasih sudah menggunakan program ini")
        print()
    else :
        print()
        print("silahkan pilih menu yang tersedia")
        print()

    # print(catatan)