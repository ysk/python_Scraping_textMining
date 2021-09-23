## アプリ説明
占いサイトをスクレイピングして、<br>
結果をテキストマイニングするツール

## 概要
占いたい西暦、上半期下半期、星座を入力すると、<br>
テキストマイニングされ、画像が生成される。

## 機能
生成された画像は自動でLINEに通知が来るように設定した。<br>

## 実装
メインプログラム<br>
https://github.com/ysk/python_Scraping_textMining/blob/main/main.py

## 画像のイメージ
![sample](https://user-images.githubusercontent.com/187446/134494234-3cbd9ae3-2012-4602-b252-1a37ba2a5838.png)

## 使用ライブラリ

Word Cloud ワードクラウドの生成<br>
Janome 形態素解析エンジン<br>
BeautifulSoup　スクレイピングツール<br>
python-dotenv　.envファイル読み込みに使用
