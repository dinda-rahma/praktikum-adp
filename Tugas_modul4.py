#program form penilaian calon penerimaan tim pengajar Himpunan Matematika dan Sains Data.
n=int(input("jumlah pendaftar : "))
print(" ")

for i in range (n):
    print(f"Data pendaftar ke-{i+1}")
    nama=str(input("nama : "))
    matkul=str(input("mata kuliah yang diminati : "))
    x=0
    while x<=0:
        wawancara=float(input("penilaian wawancara (1-100): "))
        if 1<=wawancara<=100:
            x+=1
        else:
            print(" silakan masukkan nilai kembali ( 1 sampai 100)")
    y=0
    while y<=0:
        tes_tulis=float(input("penilaian tes tulis (1-100): "))
        if 1<=tes_tulis<=100:
            y+=1
        else:
             print(" silakan masukkan nilai kembali ( 1 sampai 100)")
    z=0
    while z<=0:
        mengajar=float(input("penilaian mengajar (1-100): "))
        if 1<=mengajar<=100:
            z+=1
        else:
             print(" silakan masukkan nilai kembali ( range : 1-100)")

    rata_rata=(wawancara+tes_tulis+mengajar)/3
    print(f"nilai rata-rata = {rata_rata:.2f} ")
    if rata_rata>80:
        print("predikat : LULUS")
    else :
        print("predikat : TIDAK LULUS")
    print(" ")