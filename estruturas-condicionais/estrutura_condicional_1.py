MAIOR_IDADE = 18
IDADE_ESPECIAL = 17 

idade = int(input("Informe sua idade: ")) #Informe a idade: 17

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")
else:
    print("Ainda não pode tirar a CNH")    


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH.")     
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")