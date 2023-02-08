print("================== KASIR ==================")
n=int(input("Harga Barang : "))
a=input("Apakah anda membeli barang lagi? [yes/no] : ")
total=0
while(a=="yes"):
    total+= n 
    n=int(input("Harga Barang : "))
    a=input("Apakah anda membeli barang lagi? [yes/no] : ")
    if a=="no":
        print("TOTAL BELANJA: ",total)
    else:
        print("INVALID")