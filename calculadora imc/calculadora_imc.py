#1.receber a variável peso [float]
peso = float(input('Digite o seu peso: '))
#2.receber a variável altura [float]
altura = float(input('Digite a sua altura: '))
#3. realizar o calculo de imc = (peso / altura²)
imc = (peso / (altura ** 2))
#4. imprimir o resultado do imc
print(f'O seu indicie de massa corporea: {imc:.2f}')
#Operações usadas : divisão (/) e potência (**)

