def calcular_media():
    print("=== Calculadora de Média Escolar ===")
    
    try:
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota (0 a 10): "))
        nota2 = float(input("Digite a segunda nota (0 a 10): "))
        nota3 = float(input("Digite a terceira nota (0 a 10): "))

        media = (nota1 + nota2 + nota3) / 3

        print(f"\nAluno: {nome}")
        print(f"Média final: {media:.2f}")

        if media >= 7.0:
            print("Status: Aprovado(a)!")
        elif media >= 5.0:
            print("Status: Em Recuperação.")
        else:
            print("Status: Reprovado(a).")

    except ValueError:
        print("\nErro: Por favor, insira apenas números válidos para as notas.")

if __name__ == "__main__":
    calcular_media()

