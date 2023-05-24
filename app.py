from flask import Flask, render_template
import random
import csv

app = Flask(__name__)


@app.route("/")
def index():
    # Read the sentences from the CSV file.
    with open("quotes.csv", "r", encoding='UTF8') as f:
        sentences = csv.reader(f)
        sentences = list(sentences)

    # Randomly select a sentence.
    selected_sentence = random.choice(sentences)
    sentence = selected_sentence[0]
    author = selected_sentence[1]

    # Render the template with the random sentence.
    return render_template("index.html", sentence=sentence, author=author)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
