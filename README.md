# Dino Run - Vecna Edition

## Descrição do Projeto
Este software consiste em uma implementação de um jogo do gênero "endless runner" desenvolvido em Python, utilizando a biblioteca Pygame. O projeto apresenta uma adaptação temática baseada na série "Stranger Things", incorporando elementos visuais e sonoros característicos, como o antagonista Vecna, Demobats e o ambiente do "Mundo Invertido". O objetivo principal é percorrer a maior distância possível evitando obstáculos, com incremento progressivo de dificuldade.

## 🎮 Jogar Online

Jogue diretamente no seu navegador sem precisar instalar nada:

**[▶️ JOGAR AGORA](https://elen-c-sales.github.io/dino-run-vecna-edition/)**

O jogo é compilado para WebAssembly usando [Pygbag](https://github.com/pygame-web/pygbag) e hospedado no GitHub Pages.

## Demonstração
Um registro em vídeo das funcionalidades do software pode ser encontrado no link abaixo. O formato MP4 permite visualização direta na interface web do repositório:

*   [Demonstração em Vídeo (MP4)](demo/demo_gorgon_.mp4)

*   https://github.com/user-attachments/assets/293a495e-0e38-4212-9a97-468c082c7f01

*   https://github.com/user-attachments/assets/8e473001-e540-4752-8831-d88652cc6f77



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
*   **Efeitos Visuais**: 
    *   **Sistema de Partículas**: Simula cinzas flutuantes do Mundo Invertido.
    *   **Efeito Parallax**: Implementação de scrolling em duas camadas com velocidades diferentes (15% e 40% da velocidade do jogo), criando sensação de profundidade no cenário.
*   **Trilha Sonora**: Música temática de Stranger Things tocando em loop contínuo durante o jogo.

## Estrutura de Arquivos
*   `dino-run.py`: Código-fonte principal contendo o loop do jogo, classes e lógica de controle.
*   `assets/`: Diretório contendo os recursos gráficos e sonoros:
    *   Imagens (.png): sprites do personagem, obstáculos, e camadas de fundo para parallax (`fundo-camada1.png`, `fundo-camada2.png`).
    *   Áudio (.wav): efeitos sonoros de pulo, morte e pontuação.
    *   Música (.mp3): trilha sonora temática de Stranger Things (`stranger_things_trilha.mp3`).
*   `demo/`: Diretório contendo vídeo de demonstração do funcionamento do software.
*   `highscore.txt`: Arquivo de texto simples para armazenamento da pontuação máxima.
*   `LICENSE`: Termos de licenciamento do software.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais informações.

## Desenvolvimento e Deploy

### Execução Local (Desktop)
Use o arquivo `dino-run.py` para jogar localmente:
```bash
python dino-run.py
```

### Versão Web
O jogo está configurado para deploy automático no GitHub Pages através do arquivo `main.py` e GitHub Actions:

1. **Build Automático**: Cada push na branch `main` aciona o workflow do GitHub Actions
2. **Pygbag**: Compila o jogo Python/Pygame para WebAssembly
3. **Deploy**: Publica automaticamente no GitHub Pages

Para testar o build localmente:
```bash
pip install pygbag
pygbag main.py
# Acesse http://localhost:8000
```
