import sys
import os
import codecs
import re
import unicodedata as ud

# read
__bi_grams = set()
__tri_grams = set()
__qua_grams = set()
__pen_grams = set()
__hex_grams = set()
__hep_grams = set()
__oct_grams = set()
__set_grams = set()

with codecs.open(os.path.join(os.path.dirname(__file__), 'data/words.txt'), 'r', encoding='utf-8') as fin:
    for token in fin.read().split('\r\n'):
        tmp = token.split(' ')
        if len(tmp) == 2:
            __bi_grams.add(token)
        elif len(tmp) == 3:
            __tri_grams.add(token)
        elif len(tmp) == 4:
            __qua_grams.add(token)
        elif len(tmp) == 5:
            __pen_grams.add(token)
        elif len(tmp) == 6:
            __hex_grams.add(token)
        elif len(tmp) == 7:
            __hep_grams.add(token)
        elif len(tmp) == 8:
            __oct_grams.add(token)
        __set_grams.add(token)
#print(__set_grams)


def __sylabelize(text):
    text = ud.normalize('NFC', text)
    specials = ["==>", "->", "\.\.\.", ">>"]
    digit = "\d+([\.,_]\d+)+"
    email = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    web = "^(http[s]?://)?(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+$"
    datetime = [
        "\d{1,2}\/\d{1,2}(\/\d+)?",
        "\d{1,2}-\d{1,2}(-\d+)?",
    ]
    word = "\w+"
    non_word = "[^\w\s]"
    abbreviations = [
        "[A-ZĐ]+\.",
        "Tp\.",
        "Mr\.", "Mrs\.", "Ms\.",
        "Dr\.", "ThS\."
    ]

    patterns = []
    patterns.extend(abbreviations)
    patterns.extend(specials)
    patterns.extend([web, email])
    patterns.extend(datetime)
    patterns.extend([digit, non_word, word])

    patterns = "(" + "|".join(patterns) + ")"
    if sys.version_info < (3, 0):
        patterns = patterns.encode('utf-8')
    try:
        tokens = re.findall(patterns, text, re.UNICODE)
    except:
        return []
    return [token[0] for token in tokens]


def __joinWords(word_list):
    result = ""
    l = len(word_list)
    for i in range(l):
        if i != l - 1:
            result += word_list[i] + " "
        else:
            result += word_list[i]
    return result


def __get(list):
    result = {}
    for string in list:
        result[string[2:]] = int(string[0])
    return result


__grams_alalyze_list = {}
for words in __set_grams:
    tmp = __sylabelize(words)
    l = len(tmp)
    for ix in range(1, l):
        i = tmp[ix]
        if ix == l - 1:
            str_tmp = "1_" + __joinWords(tmp[:ix])
        else:
            str_tmp = "0_" + __joinWords(tmp[:ix])
        if __grams_alalyze_list.get(i) == None:
            __grams_alalyze_list[i] = [str_tmp]
        else:
            if str_tmp not in __grams_alalyze_list.get(i):
                if str_tmp[0] == '1':
                    if '0_' + str_tmp[2:] in __grams_alalyze_list.get(i):
                        __grams_alalyze_list[i].remove('0_' + str_tmp[2:])
                    __grams_alalyze_list[i].append(str_tmp)
                else:
                    if '1_' + str_tmp[2:] not in __grams_alalyze_list.get(i):
                        __grams_alalyze_list[i].append(str_tmp)

def tokenize(text):
    #print(sylabelize(ViTokenizer.tokenize(text)))
    tmp = __sylabelize(text.lower())
    #for i in range(len(tmp)):
        #tmp[i] = tmp[i].replace('_',' ')
    #print(tmp)
    if tmp == []:
        return []
    result = []
    correct_words = tmp[0]
    not_sure_words = tmp[0]
    last_pos = 1
    count = 1
    while count < len(tmp):
        tmp_list = __grams_alalyze_list.get(tmp[count])
       # print(tmp_list,tmp[count], count, last_pos, correct_words, result)
        if tmp_list != None:
            tmp_direct = __get(tmp_list)
            if tmp_direct.get(not_sure_words) != None:
                if tmp_direct.get(not_sure_words) == 1:
                    not_sure_words += " " + tmp[count]
                    correct_words = not_sure_words
                    last_pos = count+1
                    if count == len(tmp) - 1:
                        result.append(correct_words)
                    count += 1
                else:
                    if count == len(tmp) - 1:
                        result.append(correct_words)
                        correct_words = tmp[last_pos]
                        not_sure_words = tmp[last_pos]
                        if last_pos == len(tmp) - 1:
                            result.append(tmp[count])
                        count = last_pos + 1
                    else:
                        not_sure_words += " " + tmp[count]
                        count += 1
            else:
                result.append(correct_words)
                correct_words = tmp[last_pos]
                not_sure_words = tmp[last_pos]
                if last_pos == len(tmp) - 1:
                    result.append(tmp[count])
                last_pos += 1
                count = last_pos
        else:
            result.append(correct_words)
            correct_words = tmp[last_pos]
            not_sure_words = tmp[last_pos]
            if last_pos == len(tmp) - 1:
                result.append(tmp[count])
            last_pos += 1
            count = last_pos
    return result

def sylabelize(string):
    #print("ác mộng" in __set_grams)
    return __sylabelize(string)