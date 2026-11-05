try:
    idade = int (input ("Digite sua idade:"))
except:
    print ("Digite somente números inteiros:")



try:
    n1 = int(input("Digite um número:"))
    n2 = int(input("Digite um número:"))
    resultado = n1 / n2
    print("O resultado é", resultado)
except ValueError:
    print("Erro de valor! Digite só números!")
except ZeroDivisionError:
    print("Não pode dividir por zero!")
