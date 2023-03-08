#1st way:

a, b, c=list(map(float,input().split()))

if(a>=(b+c) or b >= (a+c) or c >= (a+b)):
    print("NAO FORMA TRIANGULO")
elif(a*a == (b*b+c*c) or b*b == (a*a + c*c) or c*c == (a*a + b*b)):
     print("TRIANGULO RETANGULO")
elif(a*a > (b*b + c*c) or b*b > (a*a + c*c) or c*c > (a*a + b*b)):
    print("TRIANGULO OBTUSANGULO")
elif(a*a < (b*b + c*c) or b*b < (a*a + c*c) or c*c < (a*a + b*b)):
    print("TRIANGULO ACUTANGULO")
    
if(a == b and b == c):
    print("TRIANGULO EQUILATERO")
elif((a == b and a != c)  or (a == c and a != b) or (b == c and b != a)):
    print("TRIANGULO ISOSCELES")
    
    
   
   
#2nd way:

a,b,c=list(map(float,input().split()))
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
if(a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif(a*a == (b*b+c*c)):
     print("TRIANGULO RETANGULO")
elif(a * a > (b*b+ c*c)):
    print("TRIANGULO OBTUSANGULO")
elif(a*a<(b*b + c*c)):
    print("TRIANGULO ACUTANGULO")
if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
elif(a == b or b == c):
        print("TRIANGULO ISOSCELES")
