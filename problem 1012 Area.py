

A, B, C = list(map(float,input().split()))

triangle=0.5*A*C

circle=3.14159*C*C

trapezium=(A+B)/2.0*C

square=B*B

rectangle=A*B

print("TRIANGULO: %.3lf"%triangle)
print("CIRCULO: %.3f"%circle)
print("TRAPEZIO: %.3f"%trapezium)
print("QUADRADO: %.3f"%square)
print("RETANGULO: %.3f"%rectangle)
