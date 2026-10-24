# 🐍 Jogo da Cobrinha

Implementação do clássico **jogo da cobrinha** em **Python** com a biblioteca **Pygame**.

Projeto desenvolvido pelo **Grupo 05** na disciplina **Programação de Computadores** (Projeto A2).

**Integrantes:** 
Cauê Norberto da Silva — RGM 48009661
Cauê Soares — RGM 47207094
Christian Badolato Santos — RGM 47224011
Davi Barros Correia — RGM 47204885
Denzel de Oliveira Odilichukwu — RGM 47198711
Derik Arcanjo — RGM 47993944
Heitor Tureck De Oliveira — RGM 47104503
Jonatas do Nascimento Lima — RGM 46929720
Kaiky Macedo — RGM 47114061
Lucas Praxedes da Silva — RGM 47832550

## Como jogar

- Use as **setas do teclado** para controlar a cobrinha.
- Coma os **blocos vermelhos** para ganhar pontos e aumentar de tamanho.
- O jogo termina se a cobrinha **bater na parede** ou **no próprio corpo**.
- A pontuação aparece no canto superior esquerdo da tela.

## Como executar

### Requisitos

- Python 3.12 (desenvolvido e testado com a versão 3.12.10)
- Pygame

### Passo a passo

1. Clone o repositório e entre na pasta:

   ```bash
   git clone https://github.com/SEU-USUARIO/jogo-da-cobrinha.git
   cd jogo-da-cobrinha
   ```

2. Instale a dependência:

   ```bash
   pip install -r requirements.txt
   ```

   (ou, diretamente: `pip install pygame`)

3. Execute o jogo:

   ```bash
   python jogo_cobrinha.py
   ```

   Em alguns sistemas (Linux/macOS), use `python3` no lugar de `python`.

## Como o código funciona

| Parte | O que faz |
|-------|-----------|
| Configuração inicial | Janela de 600 × 400 px, blocos de 20 × 20 px (grade), jogo a 10 FPS |
| Cores (RGB) | Preto `(0,0,0)` para o fundo, verde `(0,255,0)` para cobra e textos, vermelho `(255,0,0)` para a comida |
| `mostrar_tela_inicial()` | Exibe título e instruções; espera uma tecla para começar |
| Loop principal | A cada ciclo: captura eventos, move a cobra, verifica colisões e redesenha a tela |
| `gerar_comida()` | Sorteia uma posição alinhada à grade, sem cair em cima da cobra |
| `bateu_na_parede()` | Verifica se a cabeça saiu dos limites da janela |
| `bateu_no_corpo()` | Verifica se a cabeça coincide com algum bloco do corpo |
| `desenhar_cobra()`, `desenhar_comida()`, `mostrar_pontuacao()` | Desenham os elementos na tela |
| `mostrar_mensagem_fim()` | Mostra o motivo do fim de jogo e a pontuação final |

**Controle de direção:** a cobra não pode inverter o sentido de uma vez. Por exemplo,
a seta para a esquerda só funciona se a cobra não estiver se movendo na horizontal
(`velocidade_x == 0`), evitando uma colisão imediata com o próprio corpo.

**Movimento:** o corpo é uma lista de posições `[x, y]`. A cada ciclo, a nova posição da
cabeça entra no fim da lista e, se a cobra não cresceu, a posição mais antiga é removida.

## Estrutura do repositório

```
jogo-da-cobrinha/
├── jogo_cobrinha.py   # código-fonte do jogo
├── requirements.txt   # dependências (pygame)
├── README.md
└── .gitignore
```

## Possíveis melhorias

- Opção de reiniciar a partida sem fechar o jogo
- Recorde (maior pontuação) salvo em arquivo
- Aumento gradual da velocidade conforme a pontuação
- Impedir que a primeira comida apareça sobre a cobra

## Autores

Grupo 05 — Programação de Computadores.

<!-- Adicionem aqui o nome (e, se quiserem, o GitHub) de cada integrante. -->
