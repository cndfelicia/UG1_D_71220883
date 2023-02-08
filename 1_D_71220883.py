print("================== KASIR ==================")
n=int(input("Harga Barang : "))
a=input("Apakah anda membeli barang lagi? [yes/no] : ")
while(a=="yes"):
    n+= n 
    n=int(input("Harga Barang : "))
    a=input("Apakah anda membeli barang lagi? [yes/no] : ")
    if a=="no":
        print("TOTAL BELANJA: ",n+n)
    else:
        print("INVALID")