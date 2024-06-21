
comprimento = int(input("Digite o comprimento"))
largura = int(input("Digite a largura"))
preco_m2 = float(input("Valor do m2"))

area_m2 = comprimento * largura 
preço_total = preco_m2 * area_m2

print (f"O terreno possui {area_m2} m2 e seu valor é de {preço_total:,.2f}R$")
 