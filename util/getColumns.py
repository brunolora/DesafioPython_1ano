import unidecode


def getColumns(df):
    columns = []

    for col in range(df.shape[1]):
        value = str(df.iat[1, col])
        if (value != 'nan'):
            columns.append(unidecode.unidecode(value))

    return columns
