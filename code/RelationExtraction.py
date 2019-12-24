from spacy.matcher import Matcher
import en_core_web_sm
nlp = en_core_web_sm.load()

def get_relation1(sentence):
    doc = nlp(sentence)
    # for ent in doc:
    #     print(ent, ent.dep_)

    matcher = Matcher(nlp.vocab)

    pattern1 = [{'DEP':'ROOT'}]

    matcher.add("matching_1", None, pattern1)
    matches = matcher(doc)
    for match_id, start, end in matches:
        return str(doc[start:end])

def get_relation2(sentence):
    doc = nlp(sentence)
    matcher = Matcher(nlp.vocab)

    pattern1 = [{'DEP':'ROOT'},
                {"DEP": "advmod", "OP": "?"},
                {"DEP": "acomp"},
                {"DEP": "prep"}]

    matcher.add("matching_1", None, pattern1)
    matches = matcher(doc)
    for match_id, start, end in matches:
        return str(doc[start:end])

def get_relation3(sentence):
    doc = nlp(sentence)
    matcher = Matcher(nlp.vocab)

    pattern1 = [{'DEP':'ROOT'},
                {"DEP": "agent"}]

    matcher.add("matching_1", None, pattern1)
    matches = matcher(doc)
    for match_id, start, end in matches:
        return str(doc[start:end])

def merge_relation(sentence):
    str_list = []
    str_list.append(get_relation1(sentence))
    str_list.append(get_relation2(sentence))
    str_list.append(get_relation3(sentence))

    str_len = 0
    use_relation = str_list[0]
    for str in str_list:
        if str is not None:
            if len(str) > str_len:
                str_len = len(str)
                use_relation = str

    return use_relation

if __name__ == "__main__":
    # test = "Sony's slide volume is better than Panasonic's"
    # test = "sound is good and the slide volume is a good feature since turning the volume up or down"
    # test = "bluetooth is great, but when a call, earbuds are better since there is no interruptions of sound.  "
    # test = "Sony or Panasonic is better than Sennheiser."
    # test = "Sony's earphone is better than apple"
    # test = "Sony is better than apple"
    # test = "Sony's mdr-6 better than nwe395."
    # test = "Sony mdrv6 is also better than nwe395."
    # test = "they sound better than some of the $20+ sony headphones!"
    test = "mdrv6 is invited by Sony."
    # test = "the price is $16."

    print(merge_relation(test))