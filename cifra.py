#!/usr/bin/env python3
"""Cifra de Vigenère
>>> cifrador("lem", "att")
'lxf'
>>> cifrador("lem", "ATT")
'LXF'
>>> cifrador("LIMAO", "ATACARBASESUL")
'LBMCOCJMSSDCX'
>>> cifrador("LIMAOLIMAOLIM", "ATACARBASESUL")
'LBMCOCJMSSDCX'
>>> decifrador("lem", cifrador("lem", "att"))
'att'
>>> decifrador("LIMAO", cifrador("LIMAO", "ATACARBASESUL"))
'ATACARBASESUL'
"""


def cifrador(senha: str, mensagem: str) -> str:
    """(senha,mensagem) -> criptograma

    Args:
        senha (str): senha de cifração, caso seja mais curta que a mensagem, os caracteres serão repetidos mantendo a ordem até que se alcançe o tamanho adequado
        mensagem (str): mensagem a ser cifrada

    Returns:
        str: criptograma
    """
    ### Garantir o mesmo comprimento entre senha e mensagem
    if len(senha) < len(mensagem):
        senha = senha * (len(mensagem) // len(senha) + 1)
        senha = senha[0 : len(mensagem)]
    """
    Para todo par de letras s,m da senha e mensagem, respectivamente:
    1. s [a-zA-Z] ->|lower| s[a-z] ->|\-ord("a")| s[0-26]
    2. repete procedimento para m
    3. resolve (s+m)%26 para descobrir a letra do criptograma
    4. soma ord("a") para ter o equivalente ascii
    """
    criptograma = [
        chr(((ord(s.lower()) + ord(m.lower()) - 2 * ord("a")) % 26) + ord("a"))
        for s, m in zip(senha, mensagem)
    ]
    ### Mantém as letras maiúsculas e minusculas no criptograma conforme a mensagem
    criptograma = [
        c if m.islower() else c.upper() for c, m in zip(criptograma, mensagem)
    ]
    return "".join(criptograma)


def decifrador(senha: str, criptograma: str) -> str:
    """(senha,criptograma) -> mensagem

    Args:
        senha (str): senha de cifração, caso seja mais curta que a mensagem, os caracteres serão repetidos mantendo a ordem até que se alcançe o tamanho adequado
        criptograma (str): mensagem cifrada

    Returns:
        str: mensagem
    """
    ### Garantir o mesmo comprimento entre senha e mensagem
    if len(senha) < len(criptograma):
        senha = senha * (len(criptograma) // len(senha) + 1)
        senha = senha[0 : len(criptograma)]
    """
    Para todo par de letras s,c da senha e criptograma, respectivamente:
    1. s [a-zA-Z] ->|lower| s[a-z] ->|\-ord("a")| s[0-26]
    2. repete procedimento para m
    3. resolve (s+m)%26 para descobrir a letra do criptograma
    4. soma ord("a") para ter o equivalente ascii
    """
    mensagem = [
        chr(((ord(c.lower()) - ord("a")) - (ord(s.lower()) - ord("a"))) % 26 + ord("a"))
        for c, s in zip(criptograma, senha)
    ]
    ### Mantém as letras maiúsculas e minusculas na mensagem conforme o criptograma
    mensagem = [m if c.islower() else m.upper() for m, c in zip(mensagem, criptograma)]
    return "".join(mensagem)


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
          >>> ./cifra [message]
          """
        )
        exit(0)

    import os

    print(cifrador(os.getenv("PASSWORD"), sys.argv[1]))
