import pickle


def write_to_binary(dataframe, filename):
    """
    Функция для сохранения в двоичный формат
    Параметры: dataframe - сохраняемый объект, filename - путь
    Автор: Хусаенов Т.И.
    """
    outfile = open(filename, 'wb')
    pickle.dump(dataframe, outfile)
    outfile.close()


def read_from_binary(filename):
    """
    Функция для чтения из двоичного формата
    Параметры: filename - путь
    Автор: Милосердов А.В.
    """
    infile = open(filename, 'rb')
    dataframe = pickle.load(infile)
    infile.close()
    return dataframe
