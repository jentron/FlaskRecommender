from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/recommender")
def recommender():
    return render_template('layout.html')

if __name__ == "__main__":
    app.run()
