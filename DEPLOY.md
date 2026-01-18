# Guia de Deploy - Dino Run Vecna Edition

Este guia explica como compilar e fazer deploy da versão web do Dino Run usando Pygbag e GitHub Pages.

## Pré-requisitos

```bash
pip install pygbag
```

## Build da Versão Web

### 1. Compilar com Pygbag

```bash
# Compilar (cria automaticamente em build/web)
pygbag --build .

# Mover para docs/ (para GitHub Pages)
xcopy /E /I /Y build\web docs
```

**Importante**: O pygbag cria automaticamente o build em `build/web`. Depois copiamos para `docs/` para o GitHub Pages usar.

Este processo irá:
- Compilar o código Python para WebAssembly
- Copiar todos os assets necessários (imagens, sons)
- Gerar `index.html` e arquivos JS/WASM
- Salvar tudo no diretório `docs/`

### 2. Testar Localmente

Antes de fazer deploy, teste localmente:

```bash
python -m http.server 8000 --directory docs
```

Acesse `http://localhost:8000` no navegador para testar o jogo.

### 3. Commit e Push

```bash
git add docs/
git commit -m "Build: Versão web compilada com Pygbag"
git push origin main
```

### 4. Configurar GitHub Pages (Apenas na Primeira Vez)

1. Vá para **Settings** do repositório no GitHub
2. Navegue até **Pages** (menu lateral)
3. Em **Source**, selecione:
   - Branch: `main`
   - Folder: `/docs`
4. Clique em **Save**

### 5. Aguardar Deploy

GitHub Pages pode levar 2-5 minutos para fazer o primeiro deploy.

Seu jogo estará disponível em:
```
https://<seu-usuario>.github.io/<nome-do-repositorio>/
```

Substitua `<seu-usuario>` pelo seu username do GitHub e `<nome-do-repositorio>` pelo nome do repositório.

## Atualizações Futuras

Sempre que modificar o código:

1. Recompilar:
   ```bash
   pygbag --build .
   xcopy /E /I /Y build\web docs
   ```

2. Commit e Push:
   ```bash
   git add docs/
   git commit -m "Update: [descrição da mudança]"
   git push
   ```

3. GitHub Pages atualizará automaticamente em ~2 minutos

## Solução de Problemas

### Erro: "Module not found"
Certifique-se de que todos os assets estão no caminho correto em `assets/`.

### Sons não funcionam
Navegadores têm restrições de audio autoplay. O usuário pode precisar clicar na tela primeiro para ativar o áudio.

### Performance baixa
WebAssembly tem ~50-70% da performance nativa. Isso é normal.

### Página em branco
Verifique o console do navegador (F12) para erros. Geralmente é problema de path nos assets.

## Diferenças: Desktop vs Web

### Desktop (dino-run.py)
- ✅ Performance total
- ✅ Sem limitações de audio
- ⚠️ Requer instalação: `pip install pygame`

### Web (main.py compilado)
- ✅ Roda no navegador (sem instalação)
- ✅ Acessível em qualquer dispositivo
- ⚠️ Performance ligeiramente inferior
- ⚠️ Possíveis limitações de audio (primeiro clique necessário)

## Estrutura de Arquivos após Build

```
docs/
├── index.html          # Página principal
├── main.js             # JavaScript gerado
├── pygame.wasm         # Python compilado
├── python.wasm         # Runtime Python
├── assets/             # Recursos copiados
│   ├── *.png          # Sprites
│   ├── *.wav          # Sons
│   └── *.mp3          # Música
└── [outros arquivos do Pygbag]
```

## Recursos Adicionais

- [Documentação Pygbag](https://pygame-web.github.io/)
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Pygame na Web](https://pygame-web.github.io/showroom/)
