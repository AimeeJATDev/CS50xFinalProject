from waitress import serve
from CS50xFinalProject import app

if __name__ == "__main__":
    serve(app, host='127.0.0.1', port='5000')