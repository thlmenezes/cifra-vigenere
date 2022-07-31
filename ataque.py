#!/usr/bin/env python3
"""Quebrando a Cifra de Vigenère
1. contar frequência de cada letra no texto
2. comparar com frequência das letras em cada língua (pt_BR, en_US)
    1. https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_de_letras
3. ...
4. descobrir keystream
5. extrair key
6. apresentar chave e texto decifrado
"""
from cifra import cifrador, decifrador

pt_BR_freq = (
    14.63,
    1.04,
    3.88,
    4.99,
    12.57,
    1.02,
    1.30,
    1.28,
    6.18,
    0.40,
    0.02,
    2.78,
    4.74,
    5.05,
    10.73,
    2.52,
    1.20,
    6.53,
    7.81,
    4.34,
    4.63,
    1.67,
    0.01,
    0.21,
    0.01,
    0.47,
)

en_US_freq = (
    8.167,
    1.492,
    2.782,
    4.253,
    12.702,
    2.228,
    2.015,
    6.094,
    6.966,
    0.153,
    0.772,
    4.025,
    2.406,
    6.749,
    7.507,
    1.929,
    0.095,
    5.987,
    6.327,
    9.056,
    2.758,
    0.978,
    2.360,
    0.150,
    1.974,
    0.074,
)


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
