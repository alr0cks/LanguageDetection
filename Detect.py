import numpy
import string
import re
import pickle
def lang_detect(text):
    translate_table = dict((ord(char), None) for char in string.punctuation)
    
    global lrLangDetectModel
    lrLangDetectFile = open('LRModel.pck1','rb')
    lrLangDetectModel = pickle.load(lrLangDetectFile)
    lrLangDetectFile.close()
    texttext = text.lower()
    text = re.sub(r"\d+","",text)
    text = text.translate(translate_table)
    
    pred = lrLangDetectModel.predict([text])
    prob = lrLangDetectModel.predict_proba([text])
    
    return pred[0]

text = input()
print(lang_detect(text))