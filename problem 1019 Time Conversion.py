seconds = int(input());

minutes = int(seconds/60);
seconds %= 60;
hours = int(minutes/60);
minutes %= 60;

print(f'{hours}:{minutes}:{seconds}')
