import requests
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter

#占いサイトのURL
load_url = "https://voguegirl.jp/horoscope/shiitake2021-h2/contents/02taurus/"

html = requests.get(load_url)

soup = BeautifulSoup(html.content, "html.parser")
token_text = [n.get_text() for n in soup.select('section.textbody p')]


token = Tokenizer()

for i in token_text:
    print(i)
    # for token in token.tokenize(i):
    #     print("    " + str(token))

# words = ''
# word_list = []
# for i in token_text:
#     pos = i.part_of_speech.split(',')[0]
#     print(pos)
    # word = i.surface
    # stopwords = ['こと','もの','それ','あれ','の','これ','ため','ん']
    # if pos == '名詞' and word not in stopwords:
    #     words = words + ' ' + word
    #     word_list.append(word)

# wc = WordCloud(background_color="white",
#                 font_path=r'msyhbd.ttc',
#                 width=800, height=800)

# print(wc)

#print(el)


# HTML全体を表示する
# title_text = soup.find('body').get_text()
# print(title_text)
# print(soup)