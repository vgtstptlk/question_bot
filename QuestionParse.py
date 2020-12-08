import pygsheets
from secret import secret
import os

class QuestionParse:
    def __init__(self):
        self.file = pygsheets.authorize(client_secret=os.path.join(os.getcwd(), '/secret/credit.json'))
        self.file = self.file.open_by_key(secret.file_id)
        self.table = self.file.worksheet('index', 0)

    # if flag == True, then all values are parsed,
    # if flag == False, then the function will return only new values
    def __parse(self, flag: bool):
        array = self.table.get_all_values(returnas='matrix')
        array = list(filter(
            lambda x: (x[0] != '') and ((str(x[6]).replace(" ", "") not in {'Обработан', 'обработан'}) or flag), array)
        )
        return array

    def __prepare_string(self, array):
        array = array[1::]
        result = "сообщения в количестве {} штук \n".format(len(array))
        iteration_str = "Время: {} \n" \
                        "ФИО: {} \n" \
                        "Почта: {} \n" \
                        "Курс: {} \n" \
                        "Группа: {} \n" \
                        "Вопрос: {} \n" \
                        "---------------\n"
        for val in array:
            result += iteration_str.format(
                val[0],
                val[1],
                val[2],
                val[3],
                val[4],
                val[5]
            )

        return result

    def get_new_messages(self):
        array = self.__parse(False)
        if len(array) < 2:
            return "Нет новых сообщений"
        return "Новые " + self.__prepare_string(array)

    def get_all_messages(self):
        array = self.__parse(True)
        return "Все " + self.__prepare_string(array)
