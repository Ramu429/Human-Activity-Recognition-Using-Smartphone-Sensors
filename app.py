from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Human Activity Recognition System"

if __name__ == '__main__':
    app.run(debug=True)
