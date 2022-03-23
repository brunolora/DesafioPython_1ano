import pandas as pd

import util.average as avg
from util.getColumns import getColumns
from util.getSubject import getSubject
from util.getStudents import getStudents

df = pd.read_excel('./samples/notas_planilha_sample.xlsx')


def relatorio2(students):
    for student in students:
        listCheckpoints = [float(student['checkpoint1']), float(
            student['checkpoint2']), float(student['checkpoint3'])]
        checkpointAverage = float(
            avg.calcCheckpoints(checkpoints=listCheckpoints))

        listChallenges = [float(student['Challenge Sprint 3']), float(
            student['Challenge Sprint 4'])]
        challengeAverage = float(avg.calcChallenges(challenges=listChallenges))

        MS1Value = float(student['Semestre_1'])

        finalGCS = avg.calcFinalGS(
            ms1=MS1Value, checkpointAverage=checkpointAverage, challengeAverage=challengeAverage)

        if (finalGCS > 10):
            print(" RM: %g" %
                  float(student['RM']) + ", " + student['Nome'] + "\n")


subject = getSubject(df)
columns = getColumns(df)
students = getStudents(columns, df)

print("\n===================================================")
print("Alunos que não possuem chance de aprovação na disciplina:")
relatorio2(students)
print("===================================================")
