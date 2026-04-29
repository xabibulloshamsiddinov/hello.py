from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "here is hello world"

if __name__ == "__main__":
    # Render o'zi port tayinlaydi, bo'lmasa 10000 ishlatiladi
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
