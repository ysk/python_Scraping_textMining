from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter
import requests
import tkinter as tk
import os

root = tk.Tk()
root.geometry('300x250')
root.title('星座を選択してください')

#ラジオボタンの作成
radio_value = tk.IntVar()
radio_value.set(0)

tk.Radiobutton(value=0, variable=radio_value, text='牡羊座').place(x=10, y=20)
tk.Radiobutton(value=1, variable=radio_value, text='牡牛座').place(x=10, y=40)
tk.Radiobutton(value=2, variable=radio_value, text='双子座').place(x=10, y=60)
tk.Radiobutton(value=3, variable=radio_value, text='蟹座').place(x=10, y=80)
tk.Radiobutton(value=4, variable=radio_value, text='獅子座').place(x=10, y=100)
tk.Radiobutton(value=5, variable=radio_value, text='乙女座').place(x=10, y=120)
tk.Radiobutton(value=6, variable=radio_value, text='天秤座').place(x=100, y=20)
tk.Radiobutton(value=7, variable=radio_value, text='蠍座').place(x=100, y=40)
tk.Radiobutton(value=8, variable=radio_value, text='射手座').place(x=100, y=60)
tk.Radiobutton(value=9, variable=radio_value, text='山羊座').place(x=100, y=80)
tk.Radiobutton(value=10, variable=radio_value, text='水瓶座').place(x=100, y=100)
tk.Radiobutton(value=11, variable=radio_value, text='魚座').place(x=100, y=120)

def check_value():
    check_value=radio_value.get()
    print(check_value)
    return check_value

tk.Button(text="決定",command=check_value).place(x=100, y=180)
tk.mainloop()

#スクレイピングして占いの文章のみ抽出
def scraping():
    if check_value() == 0:
        load_url = "https://voguegirl.jp/horoscope/shiitake2021-h2/contents/02taurus/"
    elif check_value() == 1:
        load_url = "https://voguegirl.jp/horoscope/shiitake2021-h2/contents/02taurus/"
    else:
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
        stopwords = ['こと','もの','それ','あれ','の','これ','ため','ん','自分','あなた','今年','年','下半期','上半期','牡牛座','牡牛','牡','牛','何','星座','星','座','みたい']
        if pos == '名詞' and word not in stopwords:
            words = words + ' ' + word
            word_list.append(word)

    wc = WordCloud(background_color="white", font_path=r'msyhbd.ttc', width=800, height=800)
    wc.generate(words)
    wc.to_file('sample.png')
    counter = Counter(word_list)
    frequent_word = counter.most_common(30)
    print(frequent_word)

if __name__ == '__main__':
    WordCloudGenerate()
