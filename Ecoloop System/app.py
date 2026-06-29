from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Willkommen bei EcoLoop</h1>
    <p>Projekt erfolgreich gestartet</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
