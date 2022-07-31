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
"""


def cifrador(senha: str, mensagem: str) -> str:
    """(senha,mensagem) -> criptograma

    Args:
        senha (str): senha de cifração, caso seja mais curta que a mensagem, os caracteres serão repetidos mantendo a ordem até que se alcançe o tamanho adequado
        mensagem (str): mensagem a ser cifrada

    Returns:
        str: criptograma
    """
    pass


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
