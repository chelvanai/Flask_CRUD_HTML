from flask import Flask, request, render_template, jsonify
import os
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/create', methods=['GET', 'POST'])
@cross_origin()
def create():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        quantity = request.form['quantity']
        price = request.form['price']

        if id is "":
            return "ID must be filled"
        else:
            if os.path.isfile('product_list.txt'):
                with open('product_list.txt') as f:
                    L = f.read()

                for i in L.split('\n'):
                    if i.split(',')[0] == id:
                        return "ID must be unique"

                file = open("product_list.txt", "a")
                data = id + "," + name + "," + quantity + "," + price + '\n'
                file.write(data)
                file.close()

                return "successfully written"

            else:
                file = open("product_list.txt", "w")
                data = id + "," + name + "," + quantity + "," + price + '\n'
                file.write(data)
                file.close()

                return "successfully written"


@app.route('/create_page', methods=['GET', 'POST'])
def create_page():
    return render_template('create.html')


@app.route('/view', methods=['GET', 'POST'])
def view():
    return render_template('index.html')


@app.route('/search_page', methods=['GET', 'POST'])
def search_page():
    return render_template('search.html')


@app.route('/get_table', methods=['GET', 'POST'])
@cross_origin()
def get_table():
    if request.method == 'GET':
        if os.path.isfile('product_list.txt'):
            with open('product_list.txt') as f:
                data = f.read()

            data = data.split('\n')
            final_data = []

            for i in data:
                if i is not '':
                    data_dict = {'id': i.split(',')[0], 'name': i.split(',')[1], 'quantity': i.split(',')[2],
                                 'price': i.split(',')[3]}
                    final_data.append(data_dict)

            return jsonify(final_data)

        else:
            return "No data"


@app.route('/search', methods=['POST', 'GET'])
@cross_origin()
def edit():
    if request.method == 'POST':
        name = request.form['name']
        with open('product_list.txt') as f:
            L = f.read()

        search_final_data = []

        for i in L.split('\n'):
            if i is not '':
                if i.split(',')[1] == name:
                    search_data_dict = {'id': i.split(',')[0], 'name': i.split(',')[1], 'quantity': i.split(',')[2],
                                      'price': i.split(',')[3]}
                    search_final_data.append(search_data_dict)

        return jsonify(search_final_data)


if __name__ == '__main__':
    app.run()
