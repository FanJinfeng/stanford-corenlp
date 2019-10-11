# _*_coding:utf-8_*_

from __future__ import print_function

import logging

from stanfordcorenlp import StanfordCoreNLP

# local_corenlp_path = r'G:/JavaLibraries/stanford-corenlp-full-2016-10-31/'
# local_corenlp_path = r'G:\JavaLibraries\stanford-corenlp-full-2017-06-09'
# local_corenlp_path = r'G:\JavaLibraries\stanford-corenlp-full-2018-01-31'
# local_corenlp_path = r'/home/gld/JavaLibs/stanford-corenlp-full-2016-10-31'
local_corenlp_path = r'/home/brant/workspace/tools/stanford-corenlp-full-2018-10-05'

# Simple usage
nlp = StanfordCoreNLP(local_corenlp_path, quiet=False, logging_level=logging.DEBUG)

sentence = 'Guangdong University of Foreign Studies (GDUFS) is located in Guangzhou.'
print('Tokenize:', nlp.word_tokenize(sentence))
print('Part of Speech:', nlp.pos_tag(sentence))
print('Named Entities:', nlp.ner(sentence))
print('Constituency Parsing:', nlp.parse(sentence))
print('Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()

# Other human languages support, e.g. Chinese
# sentence = '清华大学位于北京。北京是中华人民共和国的首都。'
# sentence = '他说：“喂！“路明非”！你给我站住！”叔叔追了出来，在走廊尽头冲他低吼。路明非实在没时间让他兴师问罪了，只好说：“叔叔我真有事得先走，什么事以后再说！”叔叔可不听他说，跑过来一把抓住他的手：“你小子给我说老实话？是不是在外面惹事了？我看外面都是警车还有流氓，他们都是冲你来的？”“没……没有……”路明非想辩解。“你小子真不是骗我们说上学其实跑日本来混黑道了吧？”叔叔瞪着他。“真不是，这事儿一时没法解释……”叔叔从屁股后面摸出金利来的钱包，打开来夹层里有几张日圆钞票，大概一万多的样子。他把那张万圆大钞塞进路明非手里：“叔叔不知道你惹了什么麻烦，你们年轻人见的世面大，有些事不愿告诉我们大人，我问也没用。我以前也惹过事跑过路，跑路身上千万得有现金！银行卡信用卡跑车都没用！”'

# with StanfordCoreNLP(local_corenlp_path, lang='zh', quiet=False) as nlp:
    # print(nlp.word_tokenize(sentence))
    # print(nlp.sent_split(sentence))
    # print(nlp.pos_tag(sentence))
    # print(nlp.ner(sentence))
    # print(nlp.parse(sentence))
    # print(nlp.dependency_parse(sentence))

# General Stanford CoreNLP API
# nlp = StanfordCoreNLP(local_corenlp_path, memory='8g', lang='zh')
# print(nlp.annotate(sentence))
# nlp.close()

# nlp = StanfordCoreNLP(local_corenlp_path)
# text = 'Guangdong University of Foreign Studies is located in Guangzhou. ' \
       # 'GDUFS is active in a full range of international cooperation and exchanges in education. '
# pros = {'annotators': 'tokenize,ssplit,pos', 'pinelineLanguage': 'en', 'outputFormat': 'xml'}
# print(nlp.annotate(text, properties=pros))
# nlp.close()

# Use an existing server
# nlp = StanfordCoreNLP('http://corenlp.run', port=80)
