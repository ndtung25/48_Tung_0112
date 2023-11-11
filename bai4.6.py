#giải hệ pt bậc nhất
a=float(input("nhập hệ số a:"))
b=float(input("nhập hệ số b:"))
if a==0:
    if b==0:
        print("pt vô số nghiệm")
    else:
        print("pt vô nghiệm")
else:
    print("pt có nghiệm duy nhất là:",-b/a)
#Tính số ngày của 1 tháng 1 năm nào đó 
#Thuận toán tìm UCLN
def ucln(a,b):
    if (b==0):
        return a;
    return ucln(b,a%b);
a = int(input("nhập số a :"))
b = int(input("nhập số b :"))
print("Ước chung lớn nhất là:",ucln(a,b))
   