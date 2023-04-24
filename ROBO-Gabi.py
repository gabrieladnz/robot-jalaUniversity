class Part():
    # características do robô
    def __init__(self, nome: str, nivelAtaque=0, nivelDefesa=0, energiaConsumida=0):
        self.nome = nome
        self.nivelAtaque = nivelAtaque
        self.nivelDefesa = nivelDefesa
        self.energiaConsumida = energiaConsumida

    # função que contém e retorna um dicionário com os dados do robô
    def get_dicionario(self):
        # formata a string, substituindo os espaços em branco e convertendo pra letras minúsculas
        formatar_string = self.nome.replace(" ", "_").lower()
        return {
            "{}_nome".format(formatar_string): self.nome.upper(),
            "{}_status".format(formatar_string): self.status_defesa(),
            "{}_ataque".format(formatar_string): self.nivelAtaque,
            "{}_defesa".format(formatar_string): self.nivelDefesa,
            "{}_energia_consumida".format(formatar_string): self.energiaConsumida,
        }

    # função pra reduzir a defesa a cada ataque
    def reduzir_defesa(self, nivelAtaque):
        self.nivelDefesa = self.nivelDefesa - nivelAtaque
        if self.nivelDefesa <= 0:
            self.nivelDefesa = 0

    # função para verificar se o nível de defesa
    def status_defesa(self):
        return self.nivelDefesa <= 0


class Robot:
    # a classe Robot define as características básicas do robô, interagindo com a classe Part que contém as partes do robo
    def __init__(self, nome, codigo_cor, roboSelecionado):
        self.nome = nome
        self.codigo_cor = codigo_cor
        self.energia = 100
        self.roboSelecionado = roboSelecionado
        # chama a classe Part e seus objetos, representando as partes do robô
        self.parts = [
            Part("Cabeça", nivelAtaque=10, nivelDefesa=10, energiaConsumida=5),
            Part("Arma", nivelAtaque=20,
                 nivelDefesa=0, energiaConsumida=10),
            Part("Braço esquerdo", nivelAtaque=10,
                 nivelDefesa=20, energiaConsumida=10),
            Part("Braço direito", nivelAtaque=10,
                 nivelDefesa=20, energiaConsumida=10),
            Part("Perna esquerda", nivelAtaque=8,
                 nivelDefesa=20, energiaConsumida=15),
            Part("Perna direita", nivelAtaque=12,
                 nivelDefesa=20, energiaConsumida=15),
        ]

    # imprime o status atual do robô
    def print_robo(self):
        print(self.codigo_cor)
        # representação visual do robô
        str_robot = personagens[self.roboSelecionado].format(**self.status_partes_robo())
        self.saudacao()
        self.print_energia()
        print(str_robot)
        print(cores["Branco"])

    def saudacao(self):
        print("Olá! Meu nome é ", self.nome)

    # porcentagem atual de energia
    def print_energia(self):
        print("Nós temos", self.energia, "% de energia sobrando")

    def status_partes_robo(self):
        # dicionário vazio
        part_status = {}
        # faz um loop adicionando as novas partes do robô ao dicionário
        for part in self.parts:
            status_dict = part.get_dicionario()
            part_status.update(status_dict)
        return part_status

    # verifica se o robô ainda tem partes com defesa disponível
    def parte_robo_disponivel(self):
        for part in self.parts:
            if part.status_defesa():
                return True
        return False

    # verifica se o robô está vivo ou morto com base na sua energia
    def robo_ligado(self):
        return self.energia >= 0

    # função de ataque de um robô contra outro
    def ataque(self, robo_inimigo, parte_atacante, parte_atacada):
        robo_inimigo.parts[parte_atacada].reduzir_defesa(
            self.parts[parte_atacante].nivelAtaque)
        self.energia -= self.parts[parte_atacante].energiaConsumida


cores = {
    "Preto": '\x1b[90m',
    "Azul": '\x1b[94m',
    "Ciano": '\x1b[96m',
    "Verde": '\x1b[92m',
    "Magenta": '\x1b[95m',
    "Vermelho": '\x1b[91m',
    "Branco": '\x1b[97m',
    "Amarelo": '\x1b[93m',
}

# função que permite ao usuário escolher nome e cor do robô
def criar_robo():
    robot_nome = input("\n > Nome do robô: ")
    codigo_cor = definir_cor()
    roboSelecionado = selecionarPersonagem()
    robot = Robot(robot_nome, codigo_cor, roboSelecionado)
    robot.print_robo()
    return robot


def definir_cor():
    cores_disponiveis = cores
    print("\n Cores disponíveis:")
    for key, value in cores_disponiveis.items():
        print(value, key)
    print(cores["Branco"])
    # .capitalize() permite que a entrada seja minúscula/maiúscula
    cor_escolhida = input("\n > Escolha uma cor: ").capitalize()
    # solução para cor inserida fora das opções e quebra de código.
    if cor_escolhida not in cores_disponiveis:
        print("\n Condição inválida! Insira uma cor que esteja disponível. \n")
        return definir_cor()
    else:
        return cores_disponiveis[cor_escolhida]
    
def selecionarPersonagem():
    print("\nSelecione um personagem:")
    # Faz um loop pelos itens do dicionário personagens e exibe na tela cada opção disponível para o usuário selecionar
    for opcao, personagem in personagens.items():
        print(f"{opcao} - {personagem}")

    # Inicia um loop infinito, para que o usuário possa tentar selecionar um personagem até escolher uma opção válida
    while True:
        # tentativa de converter a entrada do usuário pra um número inteiro
        try:
            opcaoSelecionada = int(input("=> "))
            # Se a opção selecionada pelo usuário não estiver disponível no dicionário personagens, levanta um erro do tipo ValueError
            if opcaoSelecionada not in personagens.keys():
                raise ValueError
            # se a opção selecionada pelo usuário estiver disponível, retorna o número correspondente
            return opcaoSelecionada
        # se o usuário inserir uma opção inválida, exibe a mensagem de erro até o usuário inserir uma opção válida
        except ValueError:
            print("\nOpção inválida! Insira uma das opções disponíveis.")

# função que inicia o jogo
def play():
    playing = True
    print("==========================================================")
    print("Bem-vindo(a) ao jogo! Uma intensa batalha espera por você! \n")
    print("> Jogador 1, escolha com quem deseja batalhar:")
    robo_um = criar_robo()
    print("> Jogador 2, escolha com quem deseja batalhar:")
    robo_dois = criar_robo()
    robo_atual = robo_um
    robo_inimigo = robo_dois
    rodada = 0

    while playing:
        if rodada % 2 == 0:
            robo_atual = robo_um
            robo_inimigo = robo_dois
        else:
            robo_atual = robo_dois
            robo_inimigo = robo_um
        robo_atual.print_robo()
        print("Qual parte devo usar para atacar?")
        parte_atacante = input("Escolha um número:")
        parte_atacante = int(parte_atacante)

        robo_inimigo.print_robo()
        print("Qual parte do inimigo devemos atacar?")
        parte_atacada = input("Escolha um número para atacar o inimigo: ")
        parte_atacada = int(parte_atacada)

        robo_atual.ataque(robo_inimigo, parte_atacante, parte_atacada)
        rodada += 1
        if not robo_inimigo.robo_ligado() or robo_inimigo.parte_robo_disponivel() == False:
            playing = False
            print("Parabéns, você ganhou!")


# ==================================== Opções de batalha ============================================
personagens = {
    1: r"""
	
      ___       ___
     [___] /~\ [___]
     |ooo|.\_/.|ooo|
     |888||   ||888|
    /|888||   ||888|\
  /_,|   ||___||   |._\
 /~\  ~~~ /[_]\ ~~~  /~\
(O_O) /~~[_____]~~\ (O_O)
     (  |       |  )
    [~` ]       [ '~]
    |~~|         |~~|
    |  |         |  |
   _<\/>_       _<\/>_
  /_====_\     /_====_\
 """,
  2: r"""
                        /[-])//  ___
                    __ --\ `_/~--|  / \
                  /_-/~~--~~ /~~~\\_\ /\
                  |  |___|===|_-- | \ \ \
_/~~~~~~~~|~~\,   ---|---\___/----|  \/\-\
~\________|__/   / // \__ |  ||  / | |   | |
         ,~-|~~~~~\--, | \|--|/~|||  |   | |
          [-|____---~~ _--'==;/ _,   |   |_|
                     /   /\__|_/  \  \__/--/
                    /---/_\  -___/ |  /,--|
                    /  /\/~--|   | |  \///
                   /  / |-__ \    |/
                  |--/ /      |-- | \
                 \^~~\\/\      \   \/- _
                  \    |  \     |~~\~~| \
                   \    \  \     \   \  | \
                     \    \ |     \   \    \
                      |~~|\/\|     \   \   |
                     |   |/         \_--_- |\
                     |  /            /   |/\/
                      ~~             /  /
                                    |__/
 """,
3: r"""
 ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠟⠛⠛⠻⠶⠶⣶⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⠋⣡⣴⣾⣿⣿⣿⣶⣶⣦⣤⣉⣉⠛⠛⠷⢶⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢉⣤⣾⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠛⠿⢷⣶⣤⣄⣉⠙⠛⠷⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⢁⣴⣿⣿⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⡟⠿⢶⣤⣄⠉⠻⣶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⢁⣴⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⣀⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠙⠓⠦⢄⣈⣻⣷⣄⠈⠻⣷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠟⢁⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⣠⣾⣿⣛⠛⠛⠻⣿⣇⠀⠀⠀⠀⣤⣄⣀⠀⠈⠉⠛⠻⠃⠀⠈⠻⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⢁⣴⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⢠⣾⡿⠋⠉⠛⠻⠶⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⣸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⠁⣰⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⢀⣴⡿⠿⠿⢷⣶⣤⣀⣀⠀⢹⣿⡄⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⣠⡾⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⣼⣿⣿⣿⠟⠁⠀⠀⠀⠀⢀⣴⣿⣿⣀⡀⠀⠀⠀⠉⠙⠛⠻⢿⣿⣇⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣇⣴⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⣸⣿⣿⣿⠋⠀⠀⠀⠀⠀⢠⣾⡟⠉⠉⠛⠛⠿⢷⣶⣤⣄⣀⠀⠀⢸⣿⡄⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⢠⣿⣯⣀⣀⡀⠀⠀⠀⠀⠀⠈⠉⠙⠛⢿⣿⡿⢁⣀⠀⠀⠹⣿⣿⠟⠋⣹⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⢹⣿⣿⣇⠀⠀⠀⠀⠀⣿⡟⠉⠛⠛⠻⠿⠷⣶⣦⣤⣄⣀⣀⢀⣾⡟⣰⠟⠉⠳⣆⠀⠀⠀⣀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⢻⣿⣿⡄⠀⠀⠀⠀⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⣿⡿⢰⡏⠀⠀⠀⠈⠛⠶⠾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⢻⣿⣿⡀⠀⠀⠀⢹⣿⣦⣤⣤⣤⣤⣀⣀⣀⣀⣀⡀⢀⣿⡇⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣄⠀⢻⣿⣷⡀⠀⠀⠀⢿⣿⠉⠉⠉⠉⠙⠛⠛⠛⠛⠛⠻⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⢻⣿⣷⡀⠀⠀⠈⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⢻⣿⣿⡄⠀⠀⠘⣿⣦⣤⣤⣤⣤⣤⣤⣤⣤⣴⣿⡇⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣦⠀⢻⣿⣿⡄⠀⠀⠘⣿⣏⠉⠉⠉⠉⠉⠀⠀⠀⢻⣿⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠻⣿⣿⡄⠀⠀⠹⣿⡄⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠹⣿⣿⡄⠀⠀⠹⣿⣄⣤⣤⣤⣤⣤⣶⣾⣿⣧⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠹⣿⣿⡄⠀⠀⢹⣿⡉⠉⠁⠀⠀⠀⠀⢸⣿⡌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠹⣿⣿⡄⠀⠀⢻⣷⡀⠀⠀⠀⠀⠀⠀⣿⣇⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡄⠹⣿⣿⡄⠀⠀⢿⣷⣤⣤⣴⣶⠶⠿⠿⣿⡌⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠹⣿⣿⡆⠀⠈⢿⣯⠀⠀⠀⠀⠀⠀⢿⣧⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠹⣿⣿⣄⠀⠘⣿⣧⠀⠀⢀⣀⣀⣼⣿⡄⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠹⣿⣿⡄⠀⠘⣿⣿⠟⠛⠋⠉⠉⢻⣷⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠹⣿⣿⡄⠀⠘⣿⣆⠀⠀⠀⠀⣸⣿⡇⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠹⣿⣿⡄⠀⠸⣿⣶⡶⠿⠛⠋⢻⣿⡘⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⢹⣿⣿⡀⠀⠹⣿⡄⠀⠀⠀⣀⣿⣧⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⢻⣿⣷⡀⠀⢹⣿⣶⠶⠟⠛⠻⣿⡄⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⢿⡄⢻⣿⣧⠀⠀⢻⣿⠀⠀⠀⣀⣿⣧⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠒⠛⠛⠛⠒⠦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⠈⢿⣿⣇⠀⠈⢿⣷⡶⠟⠛⠻⣿⡄⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠁⢀⣀⠀⢶⣶⣶⣤⡈⠙⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠘⣿⣿⡆⠀⠘⣿⡆⠀⠀⣀⣿⣧⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⢀⣠⣾⡿⢿⣷⡄⠻⣿⣿⣿⣷⣄⡉⠳⣄⠀⠀⠀⠀⠀⠀⠀⣿⡀⢻⣿⣿⡀⠀⢻⣿⡾⠟⠋⢹⣿⡈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⠞⠁⢀⣴⣿⠟⠉⠀⠀⠙⣿⣦⡈⠻⣿⣿⣿⣿⣦⡈⠻⣦⡀⠀⠀⠀⠀⢹⡇⠸⣿⣿⣇⠀⠘⣿⣆⣀⣤⣼⣿⡇⠻⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⠁⢀⣴⡿⠋⠁⠀⠀⠀⢀⣴⠟⠻⣿⣦⡈⠻⣿⣿⣿⣿⣷⣄⠙⢦⡀⠀⠀⢸⣷⠀⣿⣿⣿⠀⠀⣿⣿⠋⠉⠀⣿⡇⢠⣄⡉⠛⢶⣄⠀⠀⠀⠀⠀
⠀⠀⠀⢰⠋⠀⠀⠿⣿⣦⣄⡀⠀⢀⣴⡿⠁⠀⠀⢈⣿⢿⣶⣄⡙⠻⢿⣿⣿⣷⣦⡙⢷⣤⣸⣿⠀⣿⣿⣿⡇⠀⣿⣿⣤⣶⢾⣿⡇⢸⣿⣿⣷⣤⡈⠻⢦⡀⠀⠀
⠀⠀⠀⠘⣧⠀⠀⠀⠈⠙⠻⢿⣷⣿⣏⡀⠀⠀⣠⡿⠃⠀⠉⢻⣿⣷⣦⣬⣙⣛⠻⠿⠶⠈⠻⠏⢠⣿⣿⣿⡇⠀⣿⡟⠉⠀⣸⣿⠃⢸⣿⣿⣿⡿⠟⢀⡀⠹⣦⠀
⠀⠀⣀⡴⠋⠀⣠⣤⣄⠀⠀⠀⠈⠉⠛⠿⣷⣶⣿⣀⡀⠀⢠⡿⠁⠀⠉⣹⡿⠛⠿⠿⣿⣿⠂⠀⣼⣿⣿⣿⠁⢠⣿⣷⡾⢿⣿⠏⠀⠉⠉⠉⢁⣀⣴⣿⣿⣆⠘⣧
⣠⠞⠋⠀⠴⣾⣿⣿⣿⣿⣦⣄⡀⠀⠀⠀⠀⠈⠙⠛⠿⢿⣿⣷⣤⣤⣤⣿⣥⣤⣴⣿⠟⠁⢀⣼⣿⣿⣿⠏⢀⣾⡟⢁⣴⣿⠏⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
⠻⠦⣤⣀⡀⠀⠈⠉⠛⠻⠿⢿⣿⣷⣶⣤⣀⠘⠻⠶⣦⣤⣀⣉⠉⠙⠛⠛⠛⠉⠉⠀⣀⣴⣿⣿⣿⡿⠋⣠⣾⣿⣷⡿⠟⠁⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⣰⠏
⠀⠀⠀⠈⠉⠛⠓⠶⠦⣤⣄⣀⣀⡈⠉⠉⠛⠛⠷⠦⠀⠈⠉⠛⠛⠿⠿⠷⣾⣿⣿⣿⡿⠿⠿⠛⠁⠀⠀⠙⠛⠋⠁⠀⠀⠺⠿⠿⠿⠿⠟⠛⠛⣉⣁⣤⠶⠛⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠛⠲⠶⠶⠶⠤⠤⢤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⠤⠤⠶⠶⠶⠒⠛⠛⠛⠛⠛⠛⠓⠚⠚⠛⠛⠛⠋⠉⠁⠀⠀⠀⠀⠀
 """
}
play()