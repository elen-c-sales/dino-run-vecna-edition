# Dino Run - Vecna Edition

## Descrição do Projeto
Este software consiste em uma implementação de um jogo do gênero "endless runner" desenvolvido em Python, utilizando a biblioteca Pygame. O projeto apresenta uma adaptação temática baseada na série "Stranger Things", incorporando elementos visuais e sonoros característicos, como o antagonista Vecna, Demobats e o ambiente do "Mundo Invertido". O objetivo principal é percorrer a maior distância possível evitando obstáculos, com incremento progressivo de dificuldade.

## Demonstração
Um registro em vídeo das funcionalidades do software pode ser encontrado no link abaixo. O formato MP4 permite visualização direta na interface web do repositório:

*   [Demonstração em Vídeo (MP4)](demo/demo_gorgon_.mp4)

*   https://github.com/user-attachments/assets/293a495e-0e38-4212-9a97-468c082c7f01



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
*   `demo/`: Diretório contendo vídeo de demonstração do funcionamento do software.
*   `highscore.txt`: Arquivo de texto simples para armazenamento da pontuação máxima.
*   `LICENSE`: Termos de licenciamento do software.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.
