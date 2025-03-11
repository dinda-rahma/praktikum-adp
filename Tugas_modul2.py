#program kasir sederhana
nama_barang = str(input("Nama barang : "))
kuantitas = int(input("Kuantitas : "))
#list barang dan harga satuan:
baju_kaos=60000 #1
rok_dasar=80000 #2
celana_dasar=85000 #3
kemeja=90000 #4
hvs_A4=55000 #5
tas_ransel=85000 #6
kalkulator_scientific=75000 #7
tumbler=70000 #8
kotak_bekal=50000 #9
sepatu_sekolah=100000 #10
#
if nama_barang=="Baju kaos":
    harga_satuan=baju_kaos
    harga_total=baju_kaos*kuantitas
elif nama_barang=="Rok dasar":
    harga_satuan=rok_dasar
    harga_total=rok_dasar*kuantitas
elif nama_barang=="Celana dasar":
    harga_satuan=celana_dasar
    harga_total=celana_dasar*kuantitas
elif nama_barang=="Kemeja":
    harga_satuan=kemeja
    harga_total=kemeja*kuantitas
elif nama_barang=="HVS A4":
    harga_satuan=hvs_A4
    harga_total=hvs_A4*kuantitas
elif nama_barang=="Tas ransel":
    harga_satuan=tas_ransel
    harga_total=tas_ransel*kuantitas
elif nama_barang=="Kalkulator scientific":
    harga_satuan=kalkulator_scientific
    harga_total=kalkulator_scientific*kuantitas
elif nama_barang=="Tumbler":
    harga_satuan=tumbler
    harga_total=tumbler*kuantitas
elif nama_barang=="Kotak bekal":
    harga_satuan=kotak_bekal
    harga_total=kotak_bekal*kuantitas
elif nama_barang=="Sepatu sekolah":
    harga_satuan=sepatu_sekolah
    harga_total=sepatu_sekolah*kuantitas
#list promo
diskon1=int(harga_total*0.1)
diskon2=int(harga_total*0.15)
#total bayar
if harga_total<1000000:
    potongan_harga="0"
    total_bayar=harga_total
elif 1000000<=harga_total<=1500000:
    potongan_harga=diskon1
    total_bayar=harga_total-diskon1
else:
    potongan_harga=diskon2
    total_bayar=harga_total-diskon2
#output
print("Harga Satuan : Rp",harga_satuan)
print("Harga Total : Rp",harga_total)
print("Potongan Harga : Rp",potongan_harga)
print("Total Bayar : Rp",total_bayar)