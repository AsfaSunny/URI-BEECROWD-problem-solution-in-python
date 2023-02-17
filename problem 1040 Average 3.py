N1, N2, N3, N4 = list(map(float,input().split()))

a = (((N1*2)+(N2*3)+(N3*4)+(N4*1))/10);
print("Media: %.1lf"%a)

if(a>=7.0):
	print("Aluno aprovado.")
elif(a<5.0):
	print("Aluno reprovado.")
elif(a>=5.0 and a<=6.9):
	print("Aluno em exame.")
	
	Exam_score = float(input())
	print("Nota do exame: %.1lf"%Exam_score)
	b = (a+Exam_score) / 2
	if(b >= 5.0):
		print("Aluno aprovado.")
	if (b <= 4.9):
		print("Aluno reprovado.")
	print("Media final: %.1lf"%b)
