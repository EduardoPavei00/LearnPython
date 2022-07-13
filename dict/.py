d= {'gustavo':[10,9,8], 'linguiceta':[9,9,9],'antonio':[4,2,2]}
#p=[0.3,0.3,0.4]


def boletin(alunos, pesos=[0.3, 0.3, 0.4]):
    for nome in alunos:
        notas = alunos[nome]
        media = 0
        i=0
        while i < len(notas):
            media += pesos[i]*notas[i]
            i+=1
        print("nome:", nome, "notas:", notas, "media:", int(media))

print(boletin(d))