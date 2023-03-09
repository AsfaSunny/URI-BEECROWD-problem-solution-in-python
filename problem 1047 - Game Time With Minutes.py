a, b, c, d = list(map(int,input().split()))

duration = ((c*60)+d) - ((a*60)+b)
if(duration <= 0):
    duration += 24*60
    
time = duration // 60
minute = duration % 60

print(f"O JOGO DUROU {time} HORA(S) E {minute} MINUTO(S)")
