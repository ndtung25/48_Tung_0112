m=int(input("Nhập m: "))
n=int(input("Nhập n: "))
for i in range(1,n+1):
    if i%m==0:
        print("Các số chia hết cho m:",i)