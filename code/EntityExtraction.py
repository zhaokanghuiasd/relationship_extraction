import pandas as pd
import en_core_web_sm
import difflib

nlp = en_core_web_sm.load()

def string_similar(s1, s2):
    return difflib.SequenceMatcher(None, s1, s2).quick_ratio()

def rule1(sentence):
    doc = nlp(sentence)
    ent_pos_list = []
    count = 0
    for ent in doc.noun_chunks:
        if count == 0:
            loc = 0
        else:
            loc = len(sentence.split(" "+str(ent))[0]) + 1
        ent_pos_list.append((ent.text, loc))
        count += 1

    return ent_pos_list

def rule2(sentence):
    doc = nlp(sentence)
    ent_pos_list = []
    for ent in doc.noun_chunks:
        FLAG = 0
        is_cc = (sentence.split(str(ent))[0].strip(" ")).split(" ")[-1]
        for word in doc:
            if str(word) == is_cc and word.dep_ == "cc":
                ent_pos_list.append((ent.text, is_cc))
                FLAG = 1

        if FLAG == 0:
            ent_pos_list.append((ent.text, ""))

    handled_ent_list = []
    count = 0
    for i in range(len(ent_pos_list)):
        if count == 0:
            loc = 0
        else:
            loc = len(sentence.split(" "+str(ent_pos_list[i][0]))[0]) + 1
        if ent_pos_list[i][1] != "":
            handled_ent_list.remove(handled_ent_list[-1])
            if i-1 == 0:
                loc = 0
            handled_ent_list.append((ent_pos_list[i-1][0] + " " + ent_pos_list[i][1] + " " + ent_pos_list[i][0], loc))
        else:
            handled_ent_list.append((ent_pos_list[i][0], loc))
        count += 1

    return handled_ent_list

def rule3(sentence):
    delete_item = ["-", "/", "_"]
    ent_list = []
    data = pd.read_csv("./processed_company_type.csv")
    company_list = list(set(data["company"].to_list()))
    type_list = data["type"].to_list()
    sentence = sentence.strip(".")
    for word in "".join(sentence.split(",")).split(" "):
        for item in delete_item:
            if item in sentence:
                new_word = "".join(word.split(item))
            else:
                new_word = word

        if word.endswith("'s") or word.endswith("'"):
            new_word = new_word.split("'")[0]
        else:
            new_word = new_word
        if new_word in company_list or new_word in type_list:
            ent_list.append((word, sentence.find(word)))
        else:
            for type in company_list + type_list:
                if string_similar(new_word, type) > 0.7:
                    ent_list.append((word, sentence.find(word)))
                    break

    while 1:
        flag = 0
        for i in range(len(ent_list)):
            if int(ent_list[i][1]) == (int(ent_list[i-1][1]) + len(ent_list[i-1][0]) + 1):
                flag = 1
                ent_list.append((ent_list[i-1][0] + " " + ent_list[i][0], ent_list[i-1][1]))
                remove_1 = ent_list[i - 1]
                remove_2 = ent_list[i]
                ent_list.remove(remove_1)
                ent_list.remove(remove_2)
                break

        if flag == 0:
            break

    ent_pos_list = []
    for ent in ent_list:
        FLAG = 0
        is_cc = (sentence.split(str(ent[0]))[0].strip(" ")).split(" ")[-1]
        doc = nlp(sentence)
        for word in doc:
            if str(word) == is_cc and word.dep_ == "cc":
                ent_pos_list.append((ent[0], is_cc))
                FLAG = 1

        if FLAG == 0:
            ent_pos_list.append((ent[0], ""))

    handled_ent_list = []
    for i in range(len(ent_pos_list)):
        if i == 0:
            loc = 0
        else:
            loc = len(sentence.split(" "+str(ent_pos_list[i][0]))[0]) + 1
        loc = sentence.find(ent_pos_list[i][0])
        if ent_pos_list[i][1] != "":
            handled_ent_list.remove(handled_ent_list[-1])
            if i-1 == 0:
                loc = 0
            handled_ent_list.append((ent_pos_list[i-1][0] + " " + ent_pos_list[i][1] + " " + ent_pos_list[i][0], loc))
        else:
            handled_ent_list.append((ent_pos_list[i][0], loc))

    return handled_ent_list

def merge(sentence):
    rule_1 = rule1(sentence)
    rule_2 = rule2(sentence)
    rule_3 = rule3(sentence)
    # print("1", rule_1)
    # print("2", rule_2)
    # print("3", rule_3)

    for i in rule_2:
        deleted_rule = []
        for j in rule_1:
            if j[0] in i[0]:
                deleted_rule.append(j)

        for k in deleted_rule:
            rule_1.remove(k)

    for i in rule_2:
        deleted_rule = []
        for j in rule_3:
            if j[0] in i[0]:
                deleted_rule.append(j)

        for k in deleted_rule:
            rule_3.remove(k)

    for i in rule_3:
        deleted_rule = []
        for j in rule_2:
            if j[0] in i[0]:
                deleted_rule.append(j)

        for k in deleted_rule:
            rule_2.remove(k)

    rule = rule_1 + rule_2 + rule_3
    rule = list(set(rule))

    loc_list = []
    for item in rule:
        loc_list.append(item[1])
    loc_list.sort()
    final_entity = []

    for loc in loc_list:
        for item in rule:
            if item[1] == loc:
                final_entity.append(item)
                break

    return final_entity

if __name__=="__main__":

    test = "Sony's slide volume is better than Panasonic's"
    # test = "Sony or Panasonic is better than Sennheiser."
    # test = "Sony's earphone is better than apple"
    # test = "Sony is better than apple"
    # test_sentence = "Sony's mdr-6 better than nwe395."
    # test = "Sony mdrv6 is better than nwe395."
    # test = "they sound better than some of the $20+ sony headphones!"
    # test = "the clarity and definition was also better on the sony, but again, i would expect it to be for the price."

    test_sentence = test.lower()
    entities = merge(test_sentence)
    print(entities)
    # print(rule1(test_sentence))