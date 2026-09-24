from flask import Flask, render_template, request
from monitor import detect_anomaly

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    log_input = ""

    if request.method == "POST":
        log_input = request.form["log"]
        result = detect_anomaly(log_input)

    return render_template("index.html", result=result, log=log_input)

if __name__ == "__main__":
    app.run(debug=True)