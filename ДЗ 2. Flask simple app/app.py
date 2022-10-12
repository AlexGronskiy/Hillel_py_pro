from faker import Faker
from flask import Flask, render_template, request
from string import digits, ascii_letters, punctuation
import requests
gen_n = Faker(['en_US'])
gen_mail = Faker(['en_US'])
app = Flask(__name__)
PWD_ALPHABET = f"{digits}{ascii_letters}{punctuation}"


@app.route('/', methods=['get'])
def return_content():
    with open("requirements/requirements.txt", encoding='utf-8') as req:
        return req.read()


@app.route('/users', methods=['get', 'post'])
def generate_users():
    context = {'users': []}
    if request.method == 'POST':
        amount = int(request.form['amount'])
        context['amount'] = amount
        for i in range(amount):
            context['users'].append({
                'number': i + 1,
                'name': gen_n.name().split(" ")[0],
                'email': gen_mail.ascii_email()
            })
    return render_template('generate_users.html', **context)


@app.route('/astronauts', methods=['get'])
def number_of_astronauts():
    context = {'amount_of_asters': int(list(requests.get('http://api.open-notify.org/astros.json').json().values())[0])}
    return render_template('astors.html', **context)


if __name__ == '__main__':
    app.run(debug=True)