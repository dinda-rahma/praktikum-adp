n=int(input("masukkan nilai n (partisi) = "))
a=1
b=3
delta_x=(b-a)/n
luas_daerah=0
for i in range (n):
    xi = a+(i+1)*delta_x
    fxi = xi**2+2*xi
    luas_daerah+= fxi*delta_x
print(f"Luas daerah dari fungsi x^2 + 2x dengan batas daerah x=1 dan x=3 dan jumlah partisi {n} adalah {luas_daerah:.2f} ")