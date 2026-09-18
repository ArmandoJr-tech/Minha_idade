idade=int(input("Introduza a idade:"))
preco= [10, 20, 30]
if idade<=10:
    print(f"Crianca com {idade} anos,\n paga {preco[0]} Meticais")
elif idade>10 and idade<=17:
    print(f"Adolescente com {idade} anos,\n paga {preco[1]} Meticais")
else:
    print(f"Adulto com {idade} anos,\n paga {preco[2]} Meticais")