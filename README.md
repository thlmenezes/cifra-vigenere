# Cifra de Vigenère

O cifrador recebe uma senha e uma mensagem que é cifrada segundo a cifra de Vigenère, gerando um criptograma, enquanto o decifrador recebe uma senha e um criptograma que é decifrado segundo a cifra de Vigenère, recuperando uma mensagem.

Dependências:

- Python 3.10.4

## Cifrador/Decifrador

Implementado no arquivo cifra.py

Para instruções na execução do arquivo basta executar uma das opções:

```
>>> ./cifra.py
>>> ./cifra.py -h
>>> ./cifra.py --help
```

Para executar os testes, basta executar uma das opções:

```
>>> make test
```

## Quebrando a Cifra

Serão fornecidas duas mensagens cifradas (uma em português e outra em inglês) com senhas diferentes. Cada uma das mensagens deve ser utilizada para recuperar a senha geradora do keystream (senha extendida ao tamanho da mensagem) usado na cifração e então decifradas.

Para as frequências das letras foi usado: https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras