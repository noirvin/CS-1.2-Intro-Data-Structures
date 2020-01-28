from flask import Flask
from sample import generate_random_word

app = Flask(__name__)

@app.route('/')
def index():

    random_word = generate_random_word('../Code/Nietsche.txt')

    return random_word
if __name__ == '__main__':

    app.run(debug=True)
