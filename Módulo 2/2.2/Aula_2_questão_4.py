#4) Uma conta poupança foi aberta com um depósito de R$500,00. Esta conta é remunerada em 1% de juros ao mês. O código a seguir apresenta uma forma de implementação para calcular três meses de acúmulo de juros. Reescreva esse código usando apenas duas variáveis. \n",
   # "\n",
   # "juros = 1.01\n",
   # "saldo = 500.0\n",
   # "rendimento1 = saldo * juros\n",
   # "rendimento2 = rendimento1 * juros\n",
   # "rendimento3 = rendimento2 * juros\n",
   # "print(\"Após 3 meses meu novo saldo é\")\n",
   # print(rendimento3)

juros = 1.01
saldo = 500

saldo = saldo*juros #1
saldo = saldo*juros #2
saldo = saldo*juros #3
print('Após 3 meses meu saldo é: ',saldo)
