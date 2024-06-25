class viagens:
    def __init__(self, nome: str):
        self.nome = nome

    def dizerOla(self):
        print(f"Seja bem vindo {self.nome}")

    def mostrarOpcoes(self, ):

        print("\n\n")
        print("======================================================")
        print("Essas são as nossas opções de viagens no momento \n")
        print("[0] Rio de Janeiro \n[1] São Paulo \n[2] Itália")
        print("======================================================")
        

    def opcaoSelecionada(self, opc:int):

        while True:
            try:
                opcoes = ["Rio de Janeiro", "São Paulo", "Itália"]

                print(f"Você escolheu a opção {opc} que é o {opcoes[int(opc)]}")

                break

            except(IndexError):
                print("Por favor, informe algo que esteja nas nossas opções.")
                opc = int(input("Digite o número da opção desejada: "))


