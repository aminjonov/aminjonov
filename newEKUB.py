while True:
    def div(a,b):
        if a==b:
            return a
        while a!=b:
            if a%b==0:
                return b
            elif b%a==0:
                return a
            elif a>b:
                a=a%b
            elif a<b:
                b=b%a
    num1=int(input("1-sonni kiriting: "))
    num2=int(input("2-sonni kiriting: "))

    ekub=div(num1,num2)
    ekuk=int((num1*num2)/ekub)
    print(f"EKUBI: {ekub}\nEKUKI: {ekuk}")