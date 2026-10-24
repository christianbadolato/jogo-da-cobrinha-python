# Projeto: Jogo da Cobrinha

# Disciplina: Programação de Computadores

# Grupo: 05
# Cauê Norberto da Silva — RGM 48009661
#Cauê Soares — RGM 47207094
#Christian Badolato Santos — RGM 47224011
#Davi Barros Correia — RGM 47204885
#Denzel de Oliveira Odilichukwu — RGM 47198711
#Derik Arcanjo — RGM 47993944
#Heitor Tureck De Oliveira — RGM 47104503
#Jonatas do Nascimento Lima — RGM 46929720
#Kaiky Macedo — RGM 47114061
#Lucas Praxedes da Silva — RGM 47832550

# Descrição:
# Este programa implementa o clássico jogo da cobrinha utilizando Python e Pygame.
# O jogador controla a cobra com as setas do teclado, deve comer os blocos vermelhos
# para ganhar pontos e aumentar de tamanho. O jogo termina quando a cobra bate na
# parede ou no próprio corpo.




# Importa a biblioteca Pygame, usada para criar a janela, desenhar elementos
# na tela e capturar eventos do teclado.
import pygame

# Importa a biblioteca random, usada para gerar posições aleatórias para a comida.
import random




# inicializa todos os módulos necessários para o Pygame.
pygame.init()





# Define as dimensões da janela do jogo em pixels.
largura = 600
altura = 400

# Cria a janela principal do jogo com a largura e altura definidas.
tela = pygame.display.set_mode((largura, altura))

# Define o título que aparece na janela do jogo.
pygame.display.set_caption("Jogo da Cobrinha")

# Cria um relógio para controlar a velocidade de atualização do jogo.
relogio = pygame.time.Clock()





# Define as cores utilizadas no jogo no formato RGB.
# Cada cor é representada por uma tupla com três valores: vermelho, verde e azul.
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)





# Define a fonte usada para exibir a pontuação e textos menores na tela.
fonte_pontuacao = pygame.font.SysFont("Arial", 25)





# Definee uma fonte maior, usada em títulos como a tela inicial e a tela final.
fonte_fim = pygame.font.SysFont("Arial", 35)




# Define o tamanho de cada bloco da cobra e da comida.
# A cobra se movimenta em uma grade de 20 em 20 pixels.
tamanho_bloco = 20 

# Define a posição inicial da cabeça da cobra no centro da tela.
cobra_x = largura // 2 
cobra_y = altura // 2 

# Define a direção inicial da cobra.
# Neste caso, ela começa andando para a direita.
velocidade_x = tamanho_bloco
velocidade_y = 0





# Define a posição inicial da comida em uma posição aleatória da tela.
# O random.randrange usa o tamanho do bloco para manter a comida alinhada à grade.
comida_x = random.randrange(0, largura, tamanho_bloco)
comida_y = random.randrange(0, altura, tamanho_bloco)





# Armazena a pontuação atual do jogador.
pontuacao = 0





# Lista que armazena as posições dos blocos que formam o corpo da cobra.
# Cada item da lista é uma posição no formato [x, y].
corpo_cobra = []

# Define o tamanho inicial da cobra. 
# No início, ela possui apenas um bloco.
tamanho_cobra = 1 





# Controla se o loop principal do jogo deve continuar executando. 
rodando = True 

# Indica se o jogo terminou por uma colisão.
fim_de_jogo = False

# Armazena o motivo do fim do jogo, como colisão com a parede ou com o próprio corpo.
motivo_fim = ""





def mostrar_mensagem_fim(mensagem, pontuacao):
  # Limpa a tela antes de exibir a mensagem final.

  tela.fill(preto)



  # Cria textos que serão exibidos na tela final.
  texto_fim = fonte_fim.render("Fim de jogo!", True, vermelho)
  texto_motivo = fonte_pontuacao.render(mensagem, True, verde)
  texto_pontos = fonte_pontuacao.render("Pontuação final: " + str(pontuacao), True, verde)
  texto_sair = fonte_pontuacao.render("Pressione qualquer tecla para sair", True,verde)



  # posiciona os textos na tela.
  tela.blit(texto_fim, [200, 120])
  tela.blit(texto_motivo, [130, 180])
  tela.blit(texto_pontos, [190, 220])
  tela.blit(texto_sair, [130, 260])



  # Atualiza a tela para mostrar os textos renderizados.
  pygame.display.update()



  # Mantém a tela final aberta até o jogador apertar uma tecla
  # ou fechar a janela.
  esperando = True
  while esperando:
     for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
           esperando = False




        if evento.type == pygame.KEYDOWN:
           esperando = False




def mostrar_pontuacao(pontuacao):
   # Renderiza o texto da pontuação atual.

   texto_pontuacao = fonte_pontuacao.render("Pontuação: " + str(pontuacao), True, verde)
   
   # Exibe a pontuação no canto superior esquerdo da tela.
   tela.blit(texto_pontuacao, [10, 10])




def desenhar_cobra(corpo_cobra):
   # Percorre todos os blocos do corpo da cobra.
   
   for pedaco in corpo_cobra:
      
      # Desenha cada pedaço da cobra como um retângulo verde.
      pygame.draw.rect(tela, verde, [pedaco[0], pedaco[1], tamanho_bloco, tamanho_bloco])




def gerar_comida(corpo_cobra):
   # Gera uma posição aleatória para a comida
   # e garante que ela não apareça em cima da cobra.




   while True:
      x = random.randrange(0, largura, tamanho_bloco)
      y = random.randrange(0, altura, tamanho_bloco)



      # Se a posição gerada não estiver ocupada pela cobra, 
      # retorna nessa posição para ser usada como nova comida.
      if [x, y] not in corpo_cobra:
         return x, y




def bateu_na_parede(cobra_x, cobra_y):
   
   
   # Verifica se a cabeça da cobra ultrapassou os limites da tela
   if cobra_x < 0 or cobra_x >= largura or cobra_y < 0 or cobra_y >= altura:
      return True
   else:
      return False




def bateu_no_corpo(cabeca, corpo_cobra):
   # Percorre o corpo da cobra, ignorando a última posição,
   # que representa a cabeça atual.



   for pedaco in corpo_cobra[:-1]:
     # Se a cabeça estiver na mesma posição que algum pedaço do corpo,
     # significa que houve colisão.
      
      if pedaco == cabeca:
         return True

   return False




def desenhar_comida(comida_x, comida_y):
   
   #Desenha a comida como um retãngulo vermelho na posição atual.
   pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_bloco, tamanho_bloco])




def mostrar_tela_inicial():
    
    # Limpa a tela antes de exibir as intruções iniciais.
    tela.fill(preto)



    # Cria os textos da tela inicial.
    texto_titulo = fonte_fim.render("Jogo da Cobrinha", True, verde)
    texto_controles = fonte_pontuacao.render("Use as setas para controlar a cobrinha", True, verde)
    texto_objetivo = fonte_pontuacao.render("Coma os blocos vermelhos para ganhar pontos", True, verde)
    texto_inicio = fonte_pontuacao.render("Pressione qualquer tecla para começar", True, vermelho)




    # Posiciona os textos na tela.
    tela.blit(texto_titulo, [160, 90])
    tela.blit(texto_controles, [100, 160])
    tela.blit(texto_objetivo, [75, 200])
    tela.blit(texto_inicio, [120, 260])



    # Atualiza a tela para exibir a tela inicial.
    pygame.display.update()




    # Mantém a tela inicial aberta até o jogador pressionar uma tecla.
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()





            if evento.type == pygame.KEYDOWN:
                esperando = False



# Exibe a tela inicial antes do começo da partida.
mostrar_tela_inicial()



# Loop principal do jogo.
# Enquanto rodando for True, o jogo captura eventos,
# atualiza a posição da cobra, verifica colisões e redesenha a tela.
while rodando: 
  # Captura os eventos do Pygame, como fechar a janela ou pressionar teclas.
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
        rodando = False




    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_LEFT and velocidade_x == 0:
            velocidade_x = -tamanho_bloco
            velocidade_y = 0




        elif evento.key == pygame.K_RIGHT and velocidade_x == 0:
            velocidade_x = tamanho_bloco
            velocidade_y = 0




        elif evento.key == pygame.K_UP and velocidade_y == 0:
            velocidade_x = 0 
            velocidade_y = -tamanho_bloco




        elif evento.key == pygame.K_DOWN and velocidade_y == 0:
            velocidade_x = 0 
            velocidade_y = tamanho_bloco



  # Atualiza a posição da cobra somando a velocidade atual.
  cobra_x += velocidade_x
  cobra_y += velocidade_y



  # verifica se a cobra bateu em alguma parede.
  if bateu_na_parede(cobra_x, cobra_y):
    fim_de_jogo = True
    motivo_fim = "A cobrinha bateu na parede."
    rodando = False



  # Verifica se a cabeça da cobra chegou na mesma posição da comida.
  if cobra_x == comida_x and cobra_y == comida_y:
    pontuacao += 1
    tamanho_cobra += 1
    print("Pontuação:", pontuacao)

    comida_x, comida_y = gerar_comida(corpo_cobra)



  # Cria a nova posição da cabeça e adiciona corpo a cobra.
  cabeca = [cobra_x, cobra_y]
  corpo_cobra.append(cabeca)



  # Remove o pedaço mais antigo caso a cobra não tenha aumentado de tamanho.
  if len(corpo_cobra) > tamanho_cobra:
    del corpo_cobra[0]



  # Verifica se a cobra bateu no próprio corpo. 
  if bateu_no_corpo(cabeca, corpo_cobra):
    fim_de_jogo = True
    motivo_fim = "A cobrinha bateu no próprio corpo."
    rodando = False



  # Limpa a tela e desenha todos os elementos novamente.
  tela.fill(preto)




  mostrar_pontuacao(pontuacao)




  desenhar_comida(comida_x, comida_y)




  desenhar_cobra(corpo_cobra)



  # Atualiza a tela com os elementos desenhados.
  pygame.display.update()
  
  
  # Controla a velocidade do jogo.
  relogio.tick(10)




# Se o jogo terminou por colisão, a tela final mostra as informações no terminal.
if fim_de_jogo:
    mostrar_mensagem_fim(motivo_fim, pontuacao)
    print("Fim de jogo!")
    print(motivo_fim)
    print("Pontuação final:", pontuacao)



# Encerra o Pygame após o fim da execução.
pygame.quit()


