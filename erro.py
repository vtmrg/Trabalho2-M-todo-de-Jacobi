def erro_relativo(xAnterior, xAtual):

    max01 = np.max(xAnterior)
    max02 = np.max(xAtual)
    erro = abs(max02 - max01) / max02

    return erro