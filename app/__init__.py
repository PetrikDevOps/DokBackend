from flask import Flask
import app.msauth

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
