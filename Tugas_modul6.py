
banyak_pers=int(input("Banyak Persamaan Linier (2/3): "))
banyak_var=int(input("Banyak Variabel dalam Persamaan Linier (1/2/3): "))

if banyak_pers!=banyak_var:
    if banyak_pers>banyak_var:
        print("SPL tidak memiliki solusi.")
    else:
        print("SPL memiliki banyak solusi")
else:
    A=[]
    B=[]
    for i in range (banyak_pers):
        baris1 = []
        for j in range(banyak_var):
            koef=float(input(f"Koefisien x{j+1} di persamaan {i+1}: "))
            baris1.append(koef)
        A.append(baris1)
        konstan=float(input(f"Konstanta di persamaan {i+1}: "))
        B.append(konstan)

    if banyak_var == 2:
            detA = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    elif banyak_var == 3:
            detA = (A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
                - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
                + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]))
    else:
        print("Jumlah variabel harus 1, 2, atau 3.")
        detA = 0
    if detA == 0:
        print("SPL tidak memiliki solusi unik.")
    else:
        hasil = []
        for i in range(banyak_var):
            Ai = []
            for j in range(banyak_pers):
                baris2 = A[j][:]
                baris2[i] = B[j]
                Ai.append(baris2)
            if banyak_var == 2:
                detAi = Ai[0][0]*Ai[1][1] - Ai[0][1]*Ai[1][0]
            else:
                detAi = (Ai[0][0]*(Ai[1][1]*Ai[2][2] - Ai[1][2]*Ai[2][1])
                    - Ai[0][1]*(Ai[1][0]*Ai[2][2] - Ai[1][2]*Ai[2][0])
                    + Ai[0][2]*(Ai[1][0]*Ai[2][1] - Ai[1][1]*Ai[2][0]))
            hasil.append(detAi / detA)
    print("SPL memiliki solusi tunggal : ")
    for i in range(banyak_var):
        print(f"x{i+1}={hasil[i]}")

