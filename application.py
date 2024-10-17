from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

loaded_model = None
with open('basic_classifier.pkl', 'rb') as fid:
    loaded_model = pickle.load(fid)
    
vectorizer = None
with open('count_vectorizer.pkl', 'rb') as vd:
    vectorizer = pickle.load(vd)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the input text from the form
        user_input = request.form["input_text"]
        
        prediction = loaded_model.predict(vectorizer.transform([user_input]))[0]
        
        return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run()




    

