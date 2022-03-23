import pandas as pd
import util.average as avg
from util.getColumns import getColumns
from util.getSubject import getSubject
from util.getStudents import getStudents

df = pd.read_excel('./samples/notas_planilha_sample.xlsx')


def printStudents(students, subject):
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

        if (finalGCS <= 0):
            finalGCS = "Aluno já alcançou a nota necessária."

        if (isinstance(finalGCS, float) and finalGCS > 10):
            finalGCS = "Exame"

        print("\n\n===================================================")
        print(" Disciplina: " + subject + "\n")
        print(" RM: %g" % float(student['RM']) + ", " + student['Nome'] + "\n")

        print(" Semestre 1: " + str(round(MS1Value, 1)) + "\n")

        print(" \tSemestre 2:")

        print(" Checkpoints (média): " + str(round(checkpointAverage, 1)))
        print(" Challenge (média): " + str(round(challengeAverage, 1)) + "\n")
        print("---------------------------------------------------")
        print(" Nota mínima na Global Solution para aprovação: " +
              str(finalGCS))
        print("===================================================")


subject = getSubject(df)
columns = getColumns(df)
students = getStudents(columns, df)

printStudents(students, subject)
