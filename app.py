from flask import Flask
app = Flask(__name__)

COMPANY = "Wild Rydes"
DEVELOPER = "Rohit Kumar"
STUDENT_ID = "101002678"

@app.route("/")
def index():
    return f"<h1>{COMPANY}</h1><p>Developer: {DEVELOPER}</p><p>Student ID: {STUDENT_ID}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
