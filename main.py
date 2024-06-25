from viagens import viagens

def main():
    print("======================================================")
    print("Seja bem vindo ao nosso aplicativo de Viagens")
    print("======================================================")
    print("\n\n")

    nome = input("Insira seu nome para continuar: \n")

    viagem = viagens(nome)

    viagem.dizerOla()

    viagem.mostrarOpcoes()

    opc = input("Insira o número de qual lugar você deseja ir: \n")

    viagem.opcaoSelecionada(opc)

    


main()