from flask import Flask,request,render_template
import pickle as pkl

##### Load the Vectorizer and the classifier Models

app = Flask(__name__)  ## Create an application 

@app.route("/")


def main():
    welcome_text = "Welcome to our Page"
    return render_template("index.html")


vectorizer = pkl.load("vectorizer.pkl","rb")
model = pkl.safe_load("model.pkl","rb")

# print("Vectorizer",vectorizer)
# print("Model",model)

if __name__ == "__main__":
    app.run()


