#!/usr/bin/env python3
"""Cifra de Vigenère
>>> decifrador("lem", cifrador("lem", "att"))
'att'
>>> decifrador("LIMAO", cifrador("LIMAO", "ATACARBASESUL"))
'ATACARBASESUL'
>>> # inverter a chave também decifra
    decifrador("LIMAO", "lbf") == cifrador("PSOAM", "lbf")
True
"""
import itertools


def cifrador(senha: str, mensagem: str) -> str:
    """(senha,mensagem) -> criptograma

    Args:
        senha (str): senha de cifração, caso seja mais curta que a mensagem, os caracteres serão repetidos mantendo a ordem até que se alcançe o tamanho adequado
        mensagem (str): mensagem a ser cifrada, todos os espaços serão removidos

    Returns:
        str: criptograma

    Examples:
        >>> # manter maiúsculas e minúsculas
        ... cifrador("lem", "att")
        'lxf'
        >>> # remover espaços
        ... cifrador("lem", "ATT")
        'LXF'
        >>> cifrador("lem", "ATT ATT") == cifrador("lem", "ATTATT")
        True
        >>> # repetição da senha para formar keystream
        ... cifrador("LIMAO", "ATACARBASESUL")
        'LBMCOCJMSSDCX'
        >>> cifrador("LIMAO", "ATACARBASESUL") == \
            cifrador("LIMAOLIMAOLIM", "ATACARBASESUL")
        True
    """
    ### Remover espaços entre letras
    mensagem = "".join(mensagem.split())
    ### Garantir o mesmo comprimento entre senha e mensagem
    keystream = itertools.cycle(map(ord, senha.lower()))
    """
    Para todo par de letras s,m da senha e mensagem, respectivamente:
    1. s [a-zA-Z] ->|lower| s[a-z] ->|\-ord("a")| s[0-26]
    2. repete procedimento para m
    3. resolve (s+m)%26 para descobrir a letra do criptograma
    4. soma ord("a") para ter o equivalente ascii
    """
    criptograma = (
        chr(((next(keystream) + ord(m.lower()) - 2 * ord("a")) % 26) + ord("a"))
        for m in mensagem
    )
    ### Mantém as letras maiúsculas e minusculas no criptograma conforme a mensagem
    criptograma = "".join(
        c if m.islower() else c.upper() for c, m in zip(criptograma, mensagem)
    )
    return criptograma


def decifrador(senha: str, criptograma: str) -> str:
    """(senha,criptograma) -> mensagem

    Args:
        senha (str): senha de cifração, caso seja mais curta que a mensagem, os caracteres serão repetidos mantendo a ordem até que se alcançe o tamanho adequado
        criptograma (str): mensagem cifrada

    Returns:
        str: mensagem
    """
    senha = senha.lower()
    senha_invertida = "".join(
        chr(ord("a") + (26 - (ord(letra) - ord("a")) % 26)) for letra in senha
    )
    return cifrador(senha_invertida, criptograma)


if __name__ == "__main__":
    import sys

    def __devo_mostra_ajuda__(args: [str]) -> bool:
        """Avalia se deve mostrar mensagem de ajuda"""
        if args.count("-h"):
            return True
        if args.count("--help"):
            return True
        if len(args) == 1:
            return True
        return False

    if __devo_mostra_ajuda__(sys.argv):
        print(
            """
Cifra de Vigenère
    use PASSWORD from env to cipher a message passed to script
    >>> ./cifra message [-h|--help] [-d]
    
EXAMPLE:
    >>> PASSWORD=lem ./cifra.py ATT
    LXF
    >>> PASSWORD=lem ./cifra.py LXF -d
    ATT

OPTIONS:
    -h, --help
        Output this message, default when no args were passed
    -d
        Decipher message
            """
        )
        exit(0)

    import os

    funct = decifrador if sys.argv.count("-d") else cifrador
    print(funct(os.getenv("PASSWORD"), sys.argv[1]))
