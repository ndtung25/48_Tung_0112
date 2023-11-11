def sumofdigits(a):
    sum=0
    while (a!=0):
        sum = sum + a%10
        a=int(a/10)
    return sum 
a=int(input("nhập số nguyên bất kỳ:"))
print("tổng các chữ số của",a,"là",sumofdigits(a))
