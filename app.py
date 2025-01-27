from flask import Flask,request,render_template
import pickle as pkl

##### Load the Vectorizer and the classifier Models

app = Flask(__name__)  ## Create an application 

@app.route("/")


def main():
    welcome_text = "Welcome to our Page"
    return render_template("index.html")


with open("vectorizer.pkl","rb") as file:
    vectorizer = pkl.load(file)

model = pkl.load(open("model.pkl","rb"))


if __name__ == "__main__":
    app.run()


