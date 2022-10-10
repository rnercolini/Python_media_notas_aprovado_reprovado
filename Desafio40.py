# Verifica se o aluno foi aprovado ou reprovado conforme média de notas.
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
print('\033[33m-+-\033[m' * 20)
print('A média foi de {}.'.format(media))
if media < 5.0:
    print('\033[31mO aluno foi REPROVADO.\033[m')
elif media >= 5.0 and media < 6.9:
    print('\033[35mO aluno está em RECUPERAÇÃO.\033[m')
else:
    print('\033[32mO aluno está APROVADO!\033[m')
