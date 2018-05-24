import xlrd
from VNAnalysis.Analyzer import *

#Load
__file_location = os.path.join(os.path.dirname(__file__), "data/VnEmoLex.xlsx")
__PosWords = {}
__NegWords = {}
__Anger = {}
__Anticipation = {}
__Disgust = {}
__Fear = {}
__Joy = {}
__Sadness = {}
__Surprise = {}
__Trust = {}

__wb = xlrd.open_workbook(__file_location)
__sheet = __wb.sheet_by_index(0)
__WordsScore = {}

for rows in range(1, __sheet.nrows):
    try:
        __PosWords[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 2))
    except:
        __PosWords[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __NegWords[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 3))
    except:
        __NegWords[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __Anger[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 4))
    except:
        __Anger[str(__sheet.cell_value(rows, 1))] =0
    try:
        __Anticipation[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 5))
    except:
        __Anticipation[str(__sheet.cell_value(rows, 1))] =0
    try:
        __Disgust[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 6))
    except:
        __Disgust[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __Fear[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 7))
    except:
        __Fear[str(__sheet.cell_value(rows, 1))] =0
    try:
        __Joy[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 8))
    except:
        __Joy[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __Sadness[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 9))
    except:
        __Sadness[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __Surprise[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 10))
    except:
        __Surprise[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __Trust[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 11))
    except:
        __Trust[str(__sheet.cell_value(rows, 1))] = 0
    try:
        __WordsScore[str(__sheet.cell_value(rows, 1))] = int(__sheet.cell_value(rows, 12))
    except:
        __WordsScore[str(__sheet.cell_value(rows, 1))] = 0

def getScore(string):
    tmp = tokenize(string)
    print(tmp)
    #print(ViPosTagger.postagging_tokens(tmp))
    #words = tokenize(string)
    #print(words)
    scr_pos = 0
    scr_neg = 0
    scr_ang = 0
    scr_anti = 0
    scr_disg = 0
    scr_fear = 0
    scr_joy = 0
    scr_sad = 0
    scr_surp = 0
    scr_trust = 0
    scr_sum = 0
    #l = len(words)
    #for count in range(8):
       # if l >= count+1:
            #for i in range(l-count):
               # tmp.append(joinWords(words[i:i+count+1]))
    for i in tmp:
        if __WordsScore.get(i) != None:
            scr_pos += __PosWords[i]
            scr_neg += __NegWords[i]
            scr_ang += __Anger[i]
            scr_anti += __Anticipation[i]
            scr_disg += __Disgust[i]
            scr_fear += __Fear[i]
            scr_joy += __Joy[i]
            scr_sad += __Sadness[i]
            scr_surp += __Surprise[i]
            scr_trust += __Trust[i]
            scr_sum += __WordsScore[i]
    return {"Positive":scr_pos, "Negative": scr_neg, "Anger":scr_ang,"Anticipation": scr_anti,"Disgust": scr_disg,"Fear": scr_fear,"Joy": scr_joy,"Sadness": scr_sad,"Surprise": scr_surp,"Trust" :scr_trust,"Sum":scr_sum}
