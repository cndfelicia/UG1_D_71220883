jumlah=int(input("Masukkan angka : "))
for i in range(jumlah):
    print(' '*(jumlah-i-1) + '* '*(i+1) )
for i in range(jumlah):
    print(' '*(i+1) + '* '*(jumlah-i-1))