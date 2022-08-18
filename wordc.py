import jieba
import numpy as np
from PIL import Image
from wordcloud import WordCloud

def _trans_word(txt):
  words = jieba.lcut(txt)
  resultxt = ''.join(words)
  return resultxt

def makewc():
    fp = open('keyword.txt','r',encoding = 'utf-8-sig')     
    txt = fp.read()
    fp.close
    txt = _trans_word(txt)
    mask = np.array(Image.open("96.png"))               
    wordcloud = WordCloud(background_color="white",\
                        width = 1440,\
                        height = 1080,\
                        max_words = 200,\
                        max_font_size = 80,\
                        mask = mask,\
                        contour_width = 4,\
                        contour_color = 'steelblue',\
                            font_path =  "msyh.ttc"
                        ).generate(txt)
    wordcloud.to_file('抖音喜欢词云图.png')

makewc()