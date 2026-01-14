# Dino Run - Vecna Edition

## Descrição do Projeto
Este software consiste em uma implementação de um jogo do gênero "endless runner" desenvolvido em Python, utilizando a biblioteca Pygame. O projeto apresenta uma adaptação temática baseada na série "Stranger Things", incorporando elementos visuais e sonoros característicos, como o antagonista Vecna, Demobats e o ambiente do "Mundo Invertido". O objetivo principal é percorrer a maior distância possível evitando obstáculos, com incremento progressivo de dificuldade.

## Requisitos do Sistema
Para a execução correta deste software, são necessários:
*   Python 3.x instalado.
*   Biblioteca `pygame`.

## Instalação
1.  Verifique se o Python está instalado no sistema operacional.
2.  Instale a dependência necessária executando o seguinte comando no terminal:
    ```bash
    pip install pygame
    ```

## Execução
Para iniciar a aplicação, execute o arquivo principal a partir do diretório raiz do projeto:
```bash
python dino-run.py
```

## Controles
A interação com o software é realizada através do teclado:

*   **Barra de Espaço** ou **Seta para Cima**: Realiza a ação de pulo.
*   **Seta para Baixo**: Realiza a ação de agachar (utilizada para esquivar de obstáculos aéreos).
*   **Barra de Espaço** ou **Tecla R**: Reinicia o jogo após a condição de "Game Over".

## Mecânicas e Funcionalidades
*   **Geração Procedural de Obstáculos**: O jogo instancia aleatoriamente obstáculos do tipo "vinha", "relógio" e "demobat".
*   **Sistema de Pontuação**: A pontuação é incrementada conforme a progressão do jogador. O recorde (High Score) é persistido localmente no arquivo `highscore.txt`.
*   **Colisão**: Implementação de hitboxes ajustadas para detecção precisa de impacto entre o personagem e os obstáculos.
*   **Efeitos Visuais**: Inclui sistema de partículas para simular as cinzas do ambiente e efeito de parallax no plano de fundo.

## Estrutura de Arquivos
*   `dino-run.py`: Código-fonte principal contendo o loop do jogo, classes e lógica de controle.
*   `assets/`: Diretório contendo os recursos gráficos (.png) e sonoros (.wav).
*   `highscore.txt`: Arquivo de texto simples para armazenamento da pontuação máxima.
