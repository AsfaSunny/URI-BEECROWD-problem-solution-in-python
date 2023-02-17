X, Y = list(map(int,input().split()))

if(X == 1):
    total_price  = (float) (4.00 * Y)
elif(X == 2):
    total_price  = (float) (4.50 * Y)
elif(X == 3):
    total_price  = (float) (5.00 * Y)
elif (X == 4):
    total_price  = (float) (2.00 * Y);
elif (X == 5):
    total_price  = (float) (1.50 * Y)
    
print("Total: R$ %.2f"%total_price)
