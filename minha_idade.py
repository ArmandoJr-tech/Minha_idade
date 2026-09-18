idade=int(input("Introduza a idade:"))
if idade<=10:
    print(f"Crianca com {idade} anos")
elif idade>10 and idade<=17:
    print(f"Adolescente com {idade} anos")
else:
    print(f"Adulto com {idade} anos")