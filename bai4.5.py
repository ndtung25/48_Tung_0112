def ucln(a,b):
    if (b==0):
        return a;
    return ucln(b,a%b);
def bcnn(a,b):
    return int((a*b)/ucln(a,b));   
a = int(input("nhập số a :"))
b = int(input("nhập số b :"))
print("BCNN của 2 số",a,"và",b,"là",bcnn(a,b))