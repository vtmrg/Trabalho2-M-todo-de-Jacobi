import numpy as np
from menu import log, func

opcao = 1
while opcao != 0:
    opcao = log()
    func(opcao)