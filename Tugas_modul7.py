def tagihan_listrik(pemakaian,golongan):
    if golongan==1:
        if pemakaian <= 100:
            tarif=pemakaian*1500
        else:
            tarif=((pemakaian-100)*2000)+(100*1500)
    elif golongan==2:
        if pemakaian <= 100:
            tarif=pemakaian*2500
        else:
            tarif=((pemakaian-100)*3000)+(100*2500)
    elif golongan==4:
        if pemakaian <= 100:
            tarif=pemakaian*5000
        else:
            tarif=((pemakaian-100)*7000)+(100*5000)
    else:
        if pemakaian <= 100:
            tarif=pemakaian*4000
        else:
            tarif=((pemakaian-100)*5000)+(100*4000)
    print()
    print(f"Total tagihan listrik anda adalah Rp.{tarif}")

print("== Tagihan Listrik ==")
pemakaian=float(input("Jumlah pemakaian (dalam kwh): "))
golongan=int(input("Golongan tarif (1-4): "))

tagihan_listrik(pemakaian,golongan)
