def getStudents(columns, df):
    students = []

    for row in range(df.shape[0]):
        if(row > 1):
            i = 0
            student = {}

            for col in range(df.shape[1]):
                value = str(df.iat[row, col])

                if(value.lower() != 'nan'):
                    student[columns[i]] = value
                    i += 1

            students.append(student)

    return students
