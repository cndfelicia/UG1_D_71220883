print("--------Nilai ke 1--------")
a=int(input("Nilai Harian : "))
b=int(input("Nilai UTS : "))
c=int(input("Nilai UAS : "))
print("--------Nilai ke 2--------")
d=int(input("Nilai Harian : "))
e=int(input("Nilai UTS : "))
f=int(input("Nilai UAS : "))
print("--------Total Nilai--------")
total1=a*30/100+d*30/100
total2=b*30/100+e*30/100
total3=c*40/100+f*40/100
totalnya=total1+total2+total3
hasilnya=totalnya/2

print("Total nilai yang didapat: ",hasilnya)
if hasilnya>=80:
    print("Total nilai dalam huruf: A")
elif hasilnya>=60:
    print("Total nilai dalam huruf: B")
elif hasilnya>=40:
    print("Total nilai dalam huruf: C")
elif hasilnya>=20:
    print("Total nilai dalam huruf: D")
else:
    print("Total nilai dalam huruf: E")