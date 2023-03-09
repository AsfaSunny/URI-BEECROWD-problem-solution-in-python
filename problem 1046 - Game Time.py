x, y = list(map(int,input().split()))
if(x < y):
    time = y - x
else:
    time = 24 + y - x
print(f"O JOGO DUROU {time} HORA(S)")
