# Email & SMS Spam Detection System
## Overview

This project implements an **NLP-based spam detection system** that classifies emails and SMS messages as **Spam** or **Ham (Not Spam)** using traditional machine learning techniques.
The system demonstrates an **end-to-end Natural Language Processing (NLP) pipeline**, including text preprocessing, feature extraction, model training, evaluation, and inference. It is designed to showcase practical NLP skills relevant to real-world text classification problems.

## Problem Statement
Spam messages pose significant challenges such as:
* Security threats
* Phishing attacks
* Reduced productivity
* Poor user experience

Manual filtering is inefficient and error-prone. This project automates spam detection using **machine learning and NLP**, enabling fast, scalable, and accurate message classification.

## Solution Approach
The system follows a standard NLP workflow:

1. **Text Preprocessing**
   * Lowercasing
   * Tokenization
   * Stop-word removal
   * Stemming / Lemmatization

2. **Feature Extraction**
   * Text vectorization using **TF-IDF**
   * Conversion of unstructured text into numerical features

3. **Model Training**
   * Trained machine learning classifiers on labeled spam datasets
   * Optimized for accuracy and generalization

4. **Evaluation**
   * Evaluated model performance using classification metrics
   * Ensured reliable spam detection on unseen data

5. **Prediction**
   * New messages are transformed and classified as **Spam** or **Not Spam**

## Tech Stack

### Programming Language
* **Python**

### NLP & Machine Learning
* Scikit-learn
* NLTK
* TF-IDF Vectorization
* Classification Algorithms (e.g., Naive Bayes / Logistic Regression)

### Data Processing & Visualization
* Pandas
* NumPy

### Model Persistence
* Pickle (for saving trained models and vectorizers)
## 📂 Project Structure

```
Email_SMS_Spam_Detection/
│
├── spam_classifier.pkl        # Trained ML model
├── tfidf_vectorizer.pkl       # Saved TF-IDF vectorizer
├── spam_detection.py          # Main inference script
├── training.ipynb             # Model training & evaluation notebook
├── dataset.csv                # Labeled spam dataset
└── README.md                  # Project documentation
```

## 🚀 How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/lalchhabi/Email_SMS_Spam_Detection.git
cd Email_SMS_Spam_Detection
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

*(If `requirements.txt` is not available, install manually:)*

```bash
pip install numpy pandas scikit-learn nltk
```

### Run Spam Detection

```bash
python spam_detection.py
```
You can modify the input message inside the script to test different texts.

## Model Output

The system predicts:

* **Spam**
* **Not Spam (Ham)**

Example:

```
Input: "Congratulations! You have won a free prize."
Prediction: Spam
```

## 👤 Author
**Chhabi Lal Tamang**
Machine Learning Engineer | AI & NLP Enthusiast
GitHub: [https://github.com/lalchhabi](https://github.com/lalchhabi)
