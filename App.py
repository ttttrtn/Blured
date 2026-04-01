from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    # Get domain automatically for Twitch parent
    host = request.host.split(":")[0]  # removes port if any
    return render_template("index.html", parent=host)

if __name__ == "__main__":
    app.run(debug=True)
