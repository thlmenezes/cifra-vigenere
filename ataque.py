#!/usr/bin/env python3
"""Quebrando a Cifra de Vigenère
1. contar frequência de cada letra no texto
2. comparar com frequência das letras em cada língua (pt_BR, en_US)
    1. https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras
4. descobrir keystream
5. extrair key
6. apresentar chave e texto decifrado
"""
from cifra import cifrador, decifrador
import string
from collections import Counter
import itertools

pt_BR_freq = {
    "a": 0.1463,
    "b": 0.0104,
    "c": 0.0388,
    "d": 0.0499,
    "e": 0.1257,
    "f": 0.0102,
    "g": 0.0130,
    "h": 0.0128,
    "i": 0.0618,
    "j": 0.0040,
    "k": 0.0002,
    "l": 0.0278,
    "m": 0.0474,
    "n": 0.0505,
    "o": 0.1073,
    "p": 0.0252,
    "q": 0.0120,
    "r": 0.0653,
    "s": 0.0781,
    "t": 0.0434,
    "u": 0.0463,
    "v": 0.0167,
    "w": 0.0001,
    "x": 0.0021,
    "y": 0.0001,
    "z": 0.0047,
}

en_US_freq = {
    "a": 0.0749,
    "b": 0.0129,
    "c": 0.0354,
    "d": 0.0362,
    "e": 0.1400,
    "f": 0.0218,
    "g": 0.0174,
    "h": 0.0422,
    "i": 0.0665,
    "j": 0.0027,
    "k": 0.0047,
    "l": 0.0357,
    "m": 0.0339,
    "n": 0.0674,
    "o": 0.0737,
    "p": 0.0243,
    "q": 0.0026,
    "r": 0.0614,
    "s": 0.0695,
    "t": 0.0985,
    "u": 0.0300,
    "v": 0.0116,
    "w": 0.0169,
    "x": 0.0028,
    "y": 0.0164,
    "z": 0.0004,
}


def extrair_subtexto_repetido(texto: str) -> str:
    """Busca o menor subtexto que quando repetido constrói
    o texto original, sem quaisquer caracteres sobrando.

    Fonte: https://codereview.stackexchange.com/questions/161361/use-python-to-determine-the-repeating-pattern-in-a-string#answer-161408

    Args:
        texto (str): texto contendo repetições

    Returns:
        str: subtexto que se repete

    Examples:
        >>> extrair_subtexto_repetido("abcdeabcde")
        'abcde'
        >>> extrair_subtexto_repetido("abcdeabcdef")
        ''
        >>> extrair_subtexto_repetido("aaaaa")
        'a'
    """
    comprimento = len(texto)
    for i in range(1, comprimento // 2 + 1):
        repeticoes_esperadas, resto = divmod(comprimento, i)
        # Valida que não haja resto
        if resto > 0:
            continue
        # Subtexto, quando repetido, deve ser igual ao original
        if texto == texto[:i] * repeticoes_esperadas:
            return texto[:i]
    return ""


def compara_frequencia(criptograma: str, lingua: dict) -> float:
    """Gera um delta do quão próximo está o texto cifrado da língua.

    Compara a frequência das palavras no criptograma com as frequências da
    palavras na língua, menor é melhor

    Args:
        criptograma (str): texto cifrado
        lingua (dict): contém a frequência esperada de todas as letras minusculas

    Returns:
        float: delta da comparação de frequências
    """
    if not criptograma:
        return float("inf")
    criptograma = [c for c in criptograma.lower() if c in string.ascii_lowercase]
    comprimento = float(len(criptograma))
    frequencia = {
        char: freq / comprimento for char, freq in Counter(criptograma).most_common()
    }
    absolute = sum(abs(frequencia[letra] - lingua[letra]) for letra in frequencia)
    return absolute


def freq_decifra(
    criptograma: str,
    lingua: dict,
    min_tamanho_chave: int = None,
    max_tamanho_chave: int = None,
):
    cifrado = [c for c in criptograma.lower() if c in string.ascii_lowercase]
    max_tamanho_chave = max_tamanho_chave or 20
    min_tamanho_chave = min_tamanho_chave or 1
    chaves = []

    for comprimento in range(min_tamanho_chave, max_tamanho_chave):
        # testa todos os comprimentos de chaves dentro do intervalo selecionado
        chave = comprimento * [None]
        for posicao_da_senha in range(comprimento):
            proximidade = []
            # seleciona do criptograma as letras da mensagem que foram cifradas
            # com a letra atual da chave (top_key[i])
            # comprimento 1 -> [100%]
            # comprimento 2 -> [50%,50%] ...
            # usa itertools para evitar a instanciação do slice como lista
            alfabeto = "".join(
                itertools.islice(cifrado, posicao_da_senha, None, comprimento)
            )
            for letra in string.ascii_lowercase:
                # Calcula o grau de proximidade com a lingua inglesa para o resultado
                # da decifração utilizando cada uma das letras do alfabeto
                proximidade.append(
                    (
                        compara_frequencia(decifrador(letra, alfabeto), lingua),
                        letra,
                    )
                )
            # a melhor escolha é a que possui o menor delta em relação a lingua inglesa
            # ou seja, gerou o melhor texto decifrado
            chave[posicao_da_senha] = min(proximidade, key=lambda z: z[0])[1]
        # salva a chave gerada da iteração atual
        chaves.append("".join(chave))
    # ordena todas as chaves geradas pela capacidade de
    # gerar mensagens próximas a lingua
    chaves.sort(
        key=lambda senha: compara_frequencia(decifrador(senha, criptograma), lingua)
    )
    # cria uma cópia do primeiro da lista
    return chaves[:1]


if __name__ == "__main__":
    pt_BR = cifrador(
        "manuel",
        """
    A cifra de Vigenère é um método de criptografia que
    usa uma série de diferentes cifras de César baseadas
    em letras de uma senha. A invenção da cifra de Vigenère
    é erradamente atribuída a Blaise de Vigenère encontra-se
    originalmente descrita por Giovan Battista Bellaso no
    seu livro datado de 1553 com o título La Cifra del Sig.
    Giovan Battista Bellaso. Esta cifra é muito conhecida
    porque é fácil de perceber e de pôr em prática,
    parecendo, a quem tem pouca prática, que é inquebrável
    (indecifrável). Consequentemente, muitos programadores
    implementaram esquemas de criptografia nas suas aplicações
    que são no essencial cifras de Vigenère, e que são
    facilmente quebradas por qualquer criptoanalista.
        """,
    )

    for k in reversed(freq_decifra(pt_BR, pt_BR_freq)):
        print("")
        print("Decypted key: {!r}".format(k))
        print("Decypted Message:", decifrador(k, pt_BR))

    en_US = cifrador(
        "manual",
        """
    The Vigenère cipher is a method of encrypting alphabetic
    text by using a series of interwoven Caesar ciphers,
    based on the letters of a keyword. It employs a form of
    polyalphabetic substitution.
    First described by Giovan Battista Bellaso in 1553,
    the cipher is easy to understand and implement, but it
    resisted all attempts to break it until 1863, three
    centuries later.
        """,
    )

    for k in reversed(freq_decifra(en_US, en_US_freq)):
        print("")
        print("Decypted key: {!r}".format(k))
        print("Decypted Message:", decifrador(k, en_US))
