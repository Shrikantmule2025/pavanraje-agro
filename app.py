<<<<<<< HEAD
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Website is working ✅"

if __name__ == "__main__":
    app.run()
=======
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
>>>>>>> 502e15e (Added requirements.txt)
