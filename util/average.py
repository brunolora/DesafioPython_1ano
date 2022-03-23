def calcCheckpoints(checkpoints: list) -> int:
    """Recebe uma lista de 3 notas e devolve a média aritmética dos dois maiores números.

    Argumentos da função:
    checkpoints - uma lista de 3 notas. Ex: [5, 6.5, 10]
    """

    average = 0

    checkpoints.sort(reverse=True)

    for i in checkpoints[0:2]:
        average += round(i, 1)

    return average/2


def calcChallenges(challenges: list) -> int:
    """Recebe uma lista de 2 notas e devolve a média aritmética.

    Argumentos da função:
    challenges - uma lista de 2 notas. Ex: [8.5, 9]
    """

    average = 0

    for i in challenges:
        average += round(i, 1)

    return average/2


def calcMS(checkpointAverage: float, challengeAverage: float, GSValue: float):
    """Recebe a média de checkpoints, challenges e global solution e devolve a média ponderada final.

    Fórmula: ((checkpointAverage + challengeAverage) / 2 * 0.4) + (GSAverage * 0.6)

    Argumentos da função:
    checkpointAverage - a média aritmética dos checkpoints. Ex: 7,
    challengeAverage - a média aritmética dos challenges. Ex: 10,
    GSAverage - valor do Global Solution. Ex: 8.5
    """

    firstAverage = (checkpointAverage + challengeAverage)/2

    msFinal = round((firstAverage
                    * 0.4 + GSValue * 0.6), 1)

    return msFinal


def calcFinalGS(ms1: float, checkpointAverage: float, challengeAverage: float):
    """Recebe a primeira média semestral, e a média dos checkpoints e do challenge do segundo semestre. Retornando a quantidade de nota necessária para ser considerado aprovado (média acima de 6)

    Fórmula: ms1 * 0.4 + [(checkpointAverage + challengeAverage)/2 * 0.4] * 0.6 + (GSFinal * 0.6 * 0.6) >= 6

    Argumentos da função:
    ms1 - a nota final do primeiro semestre. Ex: 9,
    checkpointAverage - a média aritmética dos checkpoints do segundo semestre. Ex: 7,
    challengeAverage - a média aritmética dos challenges do segundo semestre. Ex: 10
    """

    secondMSAverage = (checkpointAverage + challengeAverage) / 2

    averageWithoutGS = 0.4 * ms1 + (secondMSAverage * 0.4 * 0.6)

    gs = round((-averageWithoutGS + 6) / 0.36, 1)

    return gs
