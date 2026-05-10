#calculadora de loja

print("Bem-vindo à calculadora de loja!")
nome_produto = "trufa_de_chocolate"
preço_do_produto = 5.00
quantidade_comprada = 4

valor_total = preço_do_produto * quantidade_comprada
valor_com_desconto = valor_total * 0.10 

print("produto: " + nome_produto)
print("quantia: " + str(quantidade_comprada))
print("preço: " + str(preço_do_produto))
print("total: " + str(valor_total))
print("valor com desconto de: " + str(valor_com_desconto))
print("valor final:" + str(valor_total - valor_com_desconto))

#senha = 1538
##input(print("insira a senha para finalizar a compra: " (print("digite a senha: "))))
#if senha == 1538:
 # print("compra finalizada com sucesso!")
#else:    print("senha incorreta, tente novamente.")

#input(print("vamos tentar denovo, certo: y/n "))
#resposta = input(print("digite sua senha: "))

#if resposta == "y":
 #   senha = 1538
  #  input(print("insira a senha para finalizar a compra: "))

   # else:    print("compra cancelada, obrigado por visitar nossa loja!")
#elif resposta == "n":
#print("compra cancelada, obrigado por visitar nossa loja!")