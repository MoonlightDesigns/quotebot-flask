import random, json
from flask import Flask, render_template
# from flask_cors import CORS


file_json = open('quotes.json')

data_json = json.load(file_json)

# print(f"{data_dict['author']}: \n{data_dict['text']}")

app = Flask(__name__)

# cors = CORS(app)

@app.route('/')
def index():

    data_dict = random.choice(list(data_json))
    author = data_dict['author']
    quote = data_dict['text']


    try:
        return render_template('index.html', author=author, quote=quote)
    except:
        return 'Erro !', 404

file_json.close()