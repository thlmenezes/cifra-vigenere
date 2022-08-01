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

pt_BR_freq = {
    "a": 14.63,
    "b": 1.04,
    "c": 3.88,
    "d": 4.99,
    "e": 12.57,
    "f": 1.02,
    "g": 1.30,
    "h": 1.28,
    "i": 6.18,
    "j": 0.40,
    "k": 0.02,
    "l": 2.78,
    "m": 4.74,
    "n": 5.05,
    "o": 10.73,
    "p": 2.52,
    "q": 1.20,
    "r": 6.53,
    "s": 7.81,
    "t": 4.34,
    "u": 4.63,
    "v": 1.67,
    "w": 0.01,
    "x": 0.21,
    "y": 0.01,
    "z": 0.47,
}

en_US_freq = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074,
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


if __name__ == "__main__":
    pt_BR = cifrador(
        "manuel",
        """
    A cifra de Vigenère é um método de criptografia que
    usa uma série de diferentes cifras de César baseadas
    em letras de uma senha. Originalmente descrita
    por Giovan Battista Bellaso no seu livro datado de 1553,
    trata-se de uma versão simplificada de uma mais geral
    cifra de substituição polialfabética, inventada por
    Leon Battista Alberti cerca de 1465.
        """,
    )

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
