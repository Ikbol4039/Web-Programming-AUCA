from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def book_list():
    books = [
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
    ]
    return render_template("index.html", books=books, title="Book List")


if __name__ == "__main__":
    app.run(debug=True)