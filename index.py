import random

def calcular_pontuacao_de_amor(nome1, nome2):
   
    combinado = nome1.lower() + nome2.lower()
    

    random.seed(sum(ord(char) for char in combinado))
    pontuacao = random.randint(0, 100)
    
    return pontuacao

def main():
    print("Bem-vindo à Calculadora de Amor!")

    nome1 = input("Digite o primeiro nome: ")
    nome2 = input("Digite o segundo nome: ")
    
 
    pontuacao = calcular_pontuacao_de_amor(nome1, nome2)

    print(f"\nA pontuação de amor entre {nome1} e {nome2} é: {pontuacao}%")

if __name__ == "__main__":
    main()
