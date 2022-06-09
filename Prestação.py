def valorPagamento(Prestacao,Dias):
    if (Dias == 0):
        return Prestacao
    else:
        multa = (Prestacao/100) * 3
        juros = (Prestacao + multa)+(0.1 + Dias)
        return juros
quantidade = 0
total = 0
print("-------------------------------------------------------------")
print("Para finalizar o programa, digite '0' no valor da Prestação!!")
print("-------------------------------------------------------------")
valorPrestacao = float(input("Digite o valor da Prestação: "))
atrasoDias = int(input("Digite os Dias de Atraso: "))
print("O valor a ser pago é: ", valorPagamento(valorPrestacao, atrasoDias))
total = total + valorPagamento(valorPrestacao, atrasoDias)
    

while valorPrestacao != 0:
    print("")
    valorPrestacao = float(input("Digite o valor da Prestação: "))
    atrasoDias = int(input("Digite os Dias de Atraso: "))
    print("O valor a ser pago é: ", valorPagamento(valorPrestacao, atrasoDias))
    total = total + valorPagamento(valorPrestacao, atrasoDias)
    print("")
    quantidade = quantidade + 1   
print("")
print("Relatório do Dia!") 
print("A quantidade de prestaçoes pagas foi: ", quantidade)
print("O valor total é: ", total)