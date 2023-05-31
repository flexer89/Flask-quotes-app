from flask import Flask, render_template, request, redirect
import random
import requests
import csv

app = Flask(__name__)


@app.route("/")
def index():
    # Read the sentences from the CSV file.
    with open("quotes.csv", "r", encoding='UTF8') as f:
        sentences = csv.reader(f)
        next(sentences)
        sentences = list(sentences)

    # Randomly select a sentence.
    selected_sentence = random.choice(sentences)
    sentence = selected_sentence[1]
    author = selected_sentence[0]

    # Render the template with the random sentence.
    return render_template("index.html", sentence=sentence, author=author)


@app.route("/add_quote", methods=['GET', 'POST'])
def add_quote():
    if request.method == 'POST':
        # Pobierz dane wejściowe
        author = request.form['author']
        quote = request.form['quote'] + ''

        # Dodaj dane do pliku CSV
        with open('quotes.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([author, quote])

        return redirect('/')
    else:
        return render_template("add_quote.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
