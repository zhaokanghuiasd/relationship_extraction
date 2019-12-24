import pandas as pd
import en_core_web_sm

file = './data/'
data = pd.read_csv(file + "test.csv")

nlp = en_core_web_sm.load()

sentence_list = []
count = 0
for info in data["review"].to_list():
    sentence_list += list(nlp(info).sents)

count = 0
new_sentence_list = []
delete_list = ["@", "\n", "#"]
for sentence in sentence_list:
    sentence = str(sentence)
    for sign in delete_list:
        if sign in sentence:
            sentence = " ".join(sentence.split(sign))

    sentence = sentence.lower()
    new_sentence_list.append(sentence)

df = pd.DataFrame()
df["sentence"] = new_sentence_list
df.to_csv("./data/preprocess_data/test_sentence.csv", index=False)