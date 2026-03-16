nome = input("Digite seu nome: ")
idade = int(float(input('digite sua idade:')))

if (idade < 18):
    autorizaçao = input('os pais autorizam a viagem?[sim/nao]')

    print("realizando embarque",nome)