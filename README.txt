Jogo da Forca

# Objetivo:
- Acertar a palavra secreta, chutando letra por letra.

# Regras:
- O jogador digita 1 letra por vêz, se a letra digitada estiver contida na "palavra secreta", o jogo mostra a letra na posição exata da letra na palavra.
(Ex. "HELLO", jogo mostra _ _ _ _ _ _, letra digitada = L, jogo mostra _ _ L L _)

- Se a letra que o jogador digitar não estiver contida na "palavra secreta", o jogo mostra uma mensagem de erro.

- O jogador tem 3 chances de errar.

- Letras com acentos, til ou cedilha, serão substituidas automaticamente por letras simples. (Ex. ã, ç, é, ó = a, c, e, o)

- O jogo acaba quando o jogador errar 3x, ele perde o jogo.

- O jogo acaba quando ele acertar todas as letras contida na palavra.

===== Versão 1.0.0 =====
# Features
- Sem login individual
- Exibir Intrução
- Exibir Regra do jogo
- Exibir a palavra secreta apenas com _ _ _ _ _ _
- A cada tentativa atualizar os _ _ _ _ _ _
- Ao jogador errar 3x, encerrar o jogo com uma mensagem de erro
- Ao jogador acertar todas as palavras, encerrar o jogo com uma mensagem de sucesso
- Jogo em visual cmd

** Caracteristicas internas
- Lista de palavras importadas de uma csv ou txt
- Palavras escolhidas aleatórias
- Permitir o jogador digitar apenas 1 letra
- Mensagem de erro ao digitar letra já digitada
- tratar as letras com acentos e cedilha