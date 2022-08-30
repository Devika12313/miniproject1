import pickle
import pandas as pd
import numpy as np
import nltk
import re
import itertools
import time
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
lem = WordNetLemmatizer()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
class placement:

        # comprehensive cleaning
        def cleaning(self, text):
            txt = str(text)
            txt = re.sub(r"http\S+", "", txt)
            if len(txt) == 0:
                return 'no text'
            else:
                txt = txt.split()
                index = 0
                for j in range(len(txt)):
                    if txt[j][0] == '@':
                        index = j
                txt = np.delete(txt, index)
                if len(txt) == 0:
                    return 'no text'
                else:
                    words = txt[0]
                    for k in range(len(txt) - 1):
                        words += " " + txt[k + 1]
                    txt = words
                    txt = re.sub(r'[^\w]', ' ', txt)
                    if len(txt) == 0:
                        return 'no text'
                    else:
                        txt = ''.join(''.join(s)[:2] for _, s in itertools.groupby(txt))
                        txt = txt.replace("'", "")
                        txt = nltk.tokenize.word_tokenize(txt)
                        # data.content[i] = [w for w in data.content[i] if not w in stopset]
                        for j in range(len(txt)):
                            txt[j] = lem.lemmatize(txt[j], "v")
                        if len(txt) == 0:
                            return 'no text'
                        else:
                            return txt

        def pred(self, msg):
            data = pd.read_excel('C:\\Users\\Devika\\PycharmProjects\\PlacementManagementSystem\\Static\\BCLsDataSet.xlsx')

            data = data.iloc[:700, :]

            data['Questions'] = data['Questions'].map(lambda x: self.cleaning(x))

            data = data.reset_index(drop=True)
            for i in range(len(data)):
                words = data.LEVEL[i][0]
                for j in range(len(data.Questions[i]) - 1):
                    words += ' ' + data.Questions[i][j + 1]
                data.Questions[i] = words

            x = int(np.round(len(data) * 0.75))
            train = data.iloc[:x, :].reset_index(drop=True)
            test = data.iloc[x:, :].reset_index(drop=True)
            from sklearn.ensemble import RandomForestClassifier
            qn = data.values[:, 0]
            label = data.values[:, 1]
            xtrain, xtest, ytrain, ytest = train_test_split(qn, label, test_size=0.2, random_state=0)
            vector = TfidfVectorizer(stop_words='english')

            xtrain_vector = vector.fit_transform(xtrain)

            with open("vector.pkl", "rb") as handle:
                vector = pickle.load(handle)

            xtest_vector = vector.transform(xtest)
            xtrain_vector = vector.transform(xtrain)

            rf = RandomForestClassifier()
            rf.fit(xtrain_vector, ytrain)
            msg=[msg]
            msgvector = vector.transform(msg)

            predicted = rf.predict(msgvector)
            print(predicted)
            return predicted[0]

