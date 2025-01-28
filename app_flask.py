from flask import Flask, request, jsonify, render_template
import pickle as pkl
from text_preprocess import text_preprocessing

app = Flask(__name__)  # Create an application

# Load the Vectorizer and the classifier Models
model_file = pkl.load(open("model.pkl", 'rb'))
vectorizer_file = pkl.load(open("vectorizer.pkl", 'rb'))


@app.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():
    try:
        # Get the SMS input from the request
        input_sms = request.json.get('smsInput', '')
        
        if not input_sms.strip():
            return jsonify({'error': 'No SMS text provided'}), 400
        
        # Text Preprocessing
        preprocessed_text = text_preprocessing(input_sms)

        # Text Vectorization
        vectorized_text = vectorizer_file.transform([preprocessed_text])

        # Predict and display the result
        result = model_file.predict(vectorized_text)

        display_result = "Spam" if result == 1 else "Not Spam"
        return jsonify({'result': display_result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
