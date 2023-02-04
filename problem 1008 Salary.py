#there are lot of ways to solve these problem but i prefer the following ways:

# 1st way which lead me to success:

num = int(input())
hr = int(input())
am = float(input())

salary = float(hr * am)

print(f'NUMBER = {num}')
print(f'SALARY = U$ {salary:.2f}')







#2nd and alternative way:

a = int(input())
b = int(input())
c = float(input())

mult = (b * c)

print(f'NUMBER = {a}')
print("SALARY = U$ %0.2f"%mult)
