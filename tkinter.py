# from bs4 import BeautifulSoup
# from janome.tokenizer import Tokenizer
# from wordcloud import WordCloud
# from collections import Counter
# import requests
# import tkinter as tk
# import os

# root = tk.Tk()
# root.geometry('300x250')
# root.title('星座を選択してください')

# #ラジオボタンの作成
# radio_value = tk.IntVar()
# radio_value.set(0)

# tk.Radiobutton(value=0, variable=radio_value, text='牡羊座').place(x=10, y=20)
# tk.Radiobutton(value=1, variable=radio_value, text='牡牛座').place(x=10, y=40)
# tk.Radiobutton(value=2, variable=radio_value, text='双子座').place(x=10, y=60)
# tk.Radiobutton(value=3, variable=radio_value, text='蟹座').place(x=10, y=80)
# tk.Radiobutton(value=4, variable=radio_value, text='獅子座').place(x=10, y=100)
# tk.Radiobutton(value=5, variable=radio_value, text='乙女座').place(x=10, y=120)
# tk.Radiobutton(value=6, variable=radio_value, text='天秤座').place(x=100, y=20)
# tk.Radiobutton(value=7, variable=radio_value, text='蠍座').place(x=100, y=40)
# tk.Radiobutton(value=8, variable=radio_value, text='射手座').place(x=100, y=60)
# tk.Radiobutton(value=9, variable=radio_value, text='山羊座').place(x=100, y=80)
# tk.Radiobutton(value=10, variable=radio_value, text='水瓶座').place(x=100, y=100)
# tk.Radiobutton(value=11, variable=radio_value, text='魚座').place(x=100, y=120)

# def check_value():
#     check_value=radio_value.get()
#     print(check_value)
#     return check_value

# tk.Button(text="決定",command=check_value).place(x=100, y=180)
# tk.mainloop()



