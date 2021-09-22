import requests
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter



#スクレイピングして占いの文章のみ抽出
def scraping():
    load_url = "https://voguegirl.jp/horoscope/shiitake2021-h2/contents/02taurus/"
    html  = requests.get(load_url)
    soup  = BeautifulSoup(html.content, "html.parser")
    str_list  = [n.get_text() for n in soup.select('section.textbody p')]
    sentence = ''
    for i in str_list:
        sentence += i
    return sentence


#WordCloudでテキストマイニングを生成させる
def WordCloudGenerate():
    token = Tokenizer()
    token_text = token.tokenize(scraping())

    words = ''
    word_list = []
    for i in token_text:
        pos = i.part_of_speech.split(',')[0]
        word = i.surface
        stopwords = ['こと','もの','それ','あれ','の','これ','ため','ん','自分','あなた','今年','年','下半期','上半期','牡牛座','牡牛','牡','牛','何','星座','星','座']
        if pos == '名詞' and word not in stopwords:
            words = words + ' ' + word
            word_list.append(word)

    wc = WordCloud(background_color="white", font_path=r'msyhbd.ttc', width=800, height=800)
    wc.generate(words)
    wc.to_file('sample.png')
    result_path = 'sample.png'

    counter = Counter(word_list)
    top_20 = counter.most_common(20)
    print(top_20)
    return result_path

if __name__ == '__main__':
    WordCloudGenerate()



