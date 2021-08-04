import random

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuestionsStorage:
    def get_questions(self):
        questions = [Question('Сколько будет два плюс два умноженное на два?', 6),
                     Question('Бревно нужно распилить на 10 частей, сколько надо сделать распилов?', 9),
                     Question('На двух руках 10 пальцев. Сколько пальцев на 5 руках?', 25),
                     Question('Укол делают каждые полчас, сколько нужно минут для трех уколов?', 60),
                     Question('Пять свечей горело, две потухло. Сколько свечей осталось?', 2)]
        return questions

class User:
    def __init__(self, name, answer, result):
        self.name = name
        self.answer = answer
        self.result = result
    def accept_right_answer(self):
        self.right_answer +=1

    def set_rank(self, rank):
        self.rank = rank    

class UsersResultStorage:
    def safe(self, user):
        file = 'result.txt'
        data = f'{user.name}^{user.answer}^{user.result}\n'
        file_provider = FileProvider()
        file_provider.append(file, data)        

    def print_result(self):
        file = 'result.txt'
        file_provider = FileProvider()
        data = file_provider.get(file).strip('\n')
        data = data.split('\n')
        users = []

        print(f'{"Имя":15}{"Правильные ответы":25}{"Результат":15}')
        for line in data:
            values = line.split('^')
            print(f'{values[0]:15}{values[1]:25}{values[2]:15}')
        
class FileProvider:
    def get(self, path):
        file = open(path, 'r')
        data = file.read()
        file.close()
        return data

    def append(self, path, data):
        file = open(path, 'a')
        data = file.write(data)
        file.close

print('Добрый день. Введите своё имя:')
name_user = input()

def calculate_result(count_rigth_answers, count_questions):
    result = ['Идиот', 'Кретин', 'Дурак', 'Нормальный', 'Талант', 'Гений']
    right_answers_percent = count_rigth_answers * 100 // count_questions
    index = right_answers_percent // 20
    return result[index]

def input_validation():
    while True:
        user_answer = input()
        if user_answer.isdigit():
            return user_answer
        else:
            print('Пожалуйста, введите число!')

def print_query(questions):
    count_right_answer = 0
    count_question = len(questions)
    i = 1
    while count_question != 0:
        random_index = random.randint(0, count_question - 1)
        print('№', i, ') ', questions[random_index].text, sep='')
        user_answer = input_validation()
        right_answer = questions[random_index].answer
        if user_answer == str(right_answer):
            count_right_answer += 1
        del questions[random_index]
        count_question -= 1
        i += 1
    return count_right_answer

def My_Tester():
    qs = QuestionsStorage()
    questions = []
    questions = qs.get_questions()
    
    len_question = len(questions)
    count_right_answer = print_query(questions)
    result = calculate_result(count_right_answer, len_question)

    user = User(name_user, count_right_answer, result)

    print(user.name, ', Ваш результат: ', user.result, sep='')
    UsersResultS = UsersResultStorage()
    UsersResultS.safe(user)

    print('Хотите просмотреть результаты предыдущих игр My-Tester? (Да/Нет)')
    answer_user_result = input()
    if answer_user_result.upper() == 'ДА':
        UsersResultS.print_result()

    print('Хотите пройти My-Tester заново? (Да/Нет)')
    answer_user_game = input()

    if answer_user_game.upper() == 'ДА':
        My_Tester()
    else:
        print('До новых встреч!')

My_Tester()
