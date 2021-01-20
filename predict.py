from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import nltk
import joblib 

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

def filter(article): 
        lemmatizer=WordNetLemmatizer()
    
        filter_sentence = ''

        sentence = article
        sentence = re.sub(r'[^\w\s]','',sentence) #cleaning

        words = nltk.word_tokenize(sentence) #tokenization

        words = [w for w in words if not w in stop_words]  #stopwords removal

        for word in words:
            filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()

        return filter_sentence
    
stop_words = stopwords.words('english')
lemmatizer=WordNetLemmatizer()
model = joblib.load('Model.sav') 
vector = joblib.load('vec.sav')
input_text =  vector.transform([filter(input(""))])
y_pred = model.predict(input_text)
prob = model.predict_proba(input_text)[0][y_pred][0] * 100

print("{},{}".format(y_pred[0], prob))
#if y_pred == 1: 
#    print("The article is real with " + str(prob) + "% confidence")
#else: 
#    print("The article is fake with " + str(prob) + "% confidence")
