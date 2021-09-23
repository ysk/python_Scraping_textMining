import requests, os
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter


#星座を選択
def selectHoroscope():

    #占い結果を出す西暦と星座を質問する
    checkYear = input('西暦を指定してください\n\n')
    checkHalfPeriod = input('上半期・下半期を選択してください\n\n上半期 : 1\n下半期 : 2\n\n')
    checkHoroscope = input('星座を選択してください\n\n牡羊座 : 1\n牡牛座 : 2\n双子座 : 3\n蟹　座 : 4\n獅子座 : 5\n乙女座 : 6\n天秤座 : 7\n蠍　座 : 8\n射手座 : 9\n山羊座 : 10\n水瓶座 : 11\n魚　座 : 12\n\n')

    #URL生成    
    baseUrl = "https://voguegirl.jp/horoscope/shiitake{}-h{}/contents/".format(checkYear, checkHalfPeriod)

    if checkHoroscope == '1':
        #牡羊座
        load_url = baseUrl + "01aries"
    elif checkHoroscope == '2':
        #牡牛座
        load_url = baseUrl + "02taurus"
    elif checkHoroscope == '3':
        #双子座
        load_url = baseUrl + "03gemini"
    elif checkHoroscope == '4':
        #蟹　座
        load_url = baseUrl + "04cancer"
    elif checkHoroscope == '5':
        #獅子座
        load_url = baseUrl + "05leo"
    elif checkHoroscope == '6':
        #乙女座
        load_url = baseUrl + "06virgo"
    elif checkHoroscope == '7':
        #天秤座
        load_url = baseUrl + "07libra"
    elif checkHoroscope == '8':
        #蠍　座
        load_url = baseUrl + "08scorpio"
    elif checkHoroscope == '9':
        #射手座
        load_url = baseUrl + "09sagittarius"
    elif checkHoroscope == '10':
        #山羊座
        load_url = baseUrl + "10capricorn"
    elif checkHoroscope == '11':
        #水瓶座
        load_url = baseUrl + "11aquarius"
    elif checkHoroscope == '12':
        #魚　座
        load_url = baseUrl + "12pisces"
    else:
        print('1～12の番号で入力してください')
        exit()
    return load_url


#スクレイピングして占いの文章のみ抽出
def scraping():
    html  = requests.get(selectHoroscope())
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

