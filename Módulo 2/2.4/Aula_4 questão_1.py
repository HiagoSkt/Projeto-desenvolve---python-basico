
    #"1) Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.\n",
    #\n",
    #"O terreno possui 250m2 e custa R$512,490.50\n",
    #"Comente na linha acima de cada instrução uma breve descrição da instrução.\n",
    #"\n",
    #"Fórmulas:\n",
    #"area_m2 = comprimento * largura\n",
    #"preco_total = preco_m2 * area_m2"

comprimento = int(input("Digite o comprimento"))
largura = int(input("Digite a largura"))
preco_m2 = float(input("Valor do m2"))

area_m2 = comprimento * largura 
preço_total = preco_m2 * area_m2

print (f"O terreno possui {area_m2} m2 e seu valor é de {preço_total:,.2f}R$")
 