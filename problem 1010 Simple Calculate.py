product1 = input().split(" ")
product2 = input().split(" ")

cod1, unit1, price1 = product1
cod2, unit2, price2 = product2
    
total = (int(unit1) * float(price1)) + (int(unit2) * float(price2))

print(f'VALOR A PAGAR: R$ {total:.2f}')  
