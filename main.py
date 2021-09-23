import requests, os
from bs4 import BeautifulSoup
from janome.tokenizer import Tokenizer
from wordcloud import WordCloud
from collections import Counter
from dotenv import load_dotenv

#envファイルの読み込み
load_dotenv()


class Application:

    def __init__(self):
        self.__LINE_NOTIFY_API_KEY = os.environ['LINE_NOTIFY_API_KEY']
        self.__signDict = {
            '1'  : '牡羊座',
            '2'  : '牡牛座',
            '3'  : '双子座',
            '4'  : '蟹座',
            '5'  : '獅子座',
            '7'  : '乙女座',
            '8'  : '蠍座',
            '9'  : '射手座',
            '10' : '山羊座',
            '11' : '水瓶座',
            '12' : '魚座'
        }
        self.__periodDict = {
            '0'  : '一年',
            '1'  : '上半期',
            '2'  : '下半期'
        }
        #占い結果を出す西暦と星座を質問する
        self.__input_year   = input('西暦を指定してください\n\n')
        self.__input_Period = input('上半期・下半期を選択してください\n\n上半期 : 1\n下半期 : 2\n\n')
        self.__input_sign   = input('星座を選択してください\n\n牡羊座 : 1\n牡牛座 : 2\n双子座 : 3\n蟹　座 : 4\n獅子座 : 5\n乙女座 : 6\n天秤座 : 7\n蠍　座 : 8\n射手座 : 9\n山羊座 : 10\n水瓶座 : 11\n魚　座 : 12\n\n')



    #星座を選択
    def __selectSign(self):
        #URL生成    
        baseUrl = "https://voguegirl.jp/horoscope/shiitake{}-h{}/contents/".format(self.__input_year, self.__input_Period)
        print(self.__periodDict[self.__input_Period])

        if self.__input_sign == '1':
            #牡羊座
            load_url = baseUrl + "01aries"
        elif self.__input_sign == '2':
            #牡牛座
            load_url = baseUrl + "02taurus"
        elif self.__input_sign == '3':
            #双子座
            load_url = baseUrl + "03gemini"
        elif self.__input_sign == '4':
            #蟹　座
            load_url = baseUrl + "04cancer"
        elif self.__input_sign == '5':
            #獅子座
            load_url = baseUrl + "05leo"
        elif self.__input_sign == '6':
            #乙女座
            load_url = baseUrl + "06virgo"
        elif self.__input_sign == '7':
            #天秤座
            load_url = baseUrl + "07libra"
        elif self.__input_sign == '8':
            #蠍　座
            load_url = baseUrl + "08scorpio"
        elif self.__input_sign == '9':
            #射手座
            load_url = baseUrl + "09sagittarius"
        elif self.__input_sign == '10':
            #山羊座
            load_url = baseUrl + "10capricorn"
        elif self.__input_sign == '11':
            #水瓶座
            load_url = baseUrl + "11aquarius"
        elif self.__input_sign == '12':
            #魚　座
            load_url = baseUrl + "12pisces"
        else:
            print('1～12の番号で入力してください')
            exit()
        return load_url



    #スクレイピングして占いの文章のみ抽出
    def __scraping(self):
        html  = requests.get(self.__selectSign())
        soup  = BeautifulSoup(html.content, "html.parser")
        str_list  = [n.get_text() for n in soup.select('section.textbody p')]
        sentence = ''
        for i in str_list:
            sentence += i
        return sentence



    #LINEに結果を通知する関数
    def __sendLineBot(self):
        url   = "https://notify-api.line.me/api/notify"
        token = self.__LINE_NOTIFY_API_KEY
        headers = {"Authorization" : "Bearer "+ token}
        message = self.__input_year + "年" + self.__periodDict[self.__input_Period] + "。" + self.__signDict[self.__input_sign] + "の占い結果を圧縮しました！"
        payload = {"message"   :  message}
        files   = {"imageFile" : open('./sample.png','rb')}
        post    = requests.post(url, headers=headers, params=payload, files=files)



    #WordCloudでテキストマイニングを生成させる
    def mian(self):
        token      = Tokenizer()
        token_text = token.tokenize(self.__scraping())

        words = ''
        word_list = []
        for i in token_text:
            pos = i.part_of_speech.split(',')[0]
            word = i.surface
            stopwords = [
            'こと','もの','それ','あれ','の','これ','ため','ん','何','みたい',
            '自分','あなた','今年','年','下半期','上半期','星座','星','座',
            '牡羊座','牡羊','羊',
            '牡牛座','牡牛','牡','牛',
            '双子座','双子',
            '蟹座','蟹',
            '獅子座','獅子',
            '獅子座','獅子',
            '乙女座','乙女',
            '天秤座','天秤',
            '蠍座','蠍',
            '射手座','射手',
            '山羊座','山羊',
            '水瓶座','水瓶',
            '魚座','魚'
            ]
            if pos == '名詞' and word not in stopwords:
                words = words + ' ' + word
                word_list.append(word)

        wc = WordCloud(background_color="white", font_path=r'msyhbd.ttc', width=800, height=800)
        wc.generate(words)
        wc.to_file('sample.png')
        counter = Counter(word_list)
        frequent_word = counter.most_common(30)
        print(frequent_word)

        self.__sendLineBot()

if __name__ == '__main__':
    app = Application()
    app.mian()

