from flask import Flask, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']

        if id is "":
            return "ID must be filled"
        else:
            if os.path.isfile('Data'):
                with open('Data') as f:
                    L = f.read()

                for i in L.split('\n'):
                    if i.split(',')[0] == id:
                        return "ID must be unique"

                file = open("Data", "a")
                data = id + "," + name + "," + quantity + "," + price + '\n'
                file.write(data)
                file.close()

                return "successfully written"

            else:
                file = open("Data", "w")
                data = id + "," + name + "," + quantity + "," + price + '\n'
                file.write(data)
                file.close()

                return "successfully written"


@app.route('/create_page', methods=['GET', 'POST'])
def create_page():
    return render_template('create.html')


if __name__ == '__main__':
    app.run()
