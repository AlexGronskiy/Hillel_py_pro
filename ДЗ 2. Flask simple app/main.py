from faker import Faker
import requests
gen_n = Faker(['en_US'])
gen_mail = Faker(['en_US'])


def return_content():
    with open("requirements/requirements.txt", encoding='utf-8') as req:
        return req.read()
# print(return_content())


def generate_users():
    # можно заменить 100 на n и при вызове функции указывать необходимое значение для большей универсальности
    for _ in range(100):
        print("name: " + gen_n.name().split(" ")[0] + '\n' + "email: " + gen_mail.ascii_email())
    return str()
# print(generate_users(n))


def number_of_astronauts():
    # не уверен правильно ли я сделал, но как я понял из json файла, 14 это и есть необходимое значение, хотя можно
    # было бы сделать через цикл - подсчёт людей в "people":, но как по мне это не удобно и нагружает прогу
    return int(list(requests.get('http://api.open-notify.org/astros.json').json().values())[0])
# print(number_of_astronauts())