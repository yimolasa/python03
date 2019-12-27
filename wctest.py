
import jieba
import pandas as pd
from wordcloud import WordCloud
import numpy as np
import csv


def wc(csvfile):
    df = pd.read_csv(csvfile)
    df = df[df['Reported for'] != ' System Center Operations Manager']

    # df = pd.read_csv(csvfile, usecols=['Shorttext'])

    text = " ".join(str(description) for description in df.Shorttext)
    text = " ".join(text.split())
    text = text.upper()
    stopwords = ['SERVER','RE','AW','TO','IN','FW','FOR','AND','WG','HELP TO','ACCESSIBLE','AGENTWATCHERSGROUP','HEALTHSERVICEWATCHER','HEALTHSERVICEWATCHER AGENTWATCHERSGROUP', 'ACCESSIBLE AT','ACCESSIBLE HEALTHSERVICEWATCHER','IS RUNNING','SIG', 'WAS','PLEASE','CHECK','NOT','DETECTED','AUTOMATIC','SYSTEMCENTER','DOM','MICROSOFT','THE','COMPUTER','ISSUE','BY','EVENT','NAME','ON']

    # wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(text)
    wordcloud = WordCloud(width=2000, height=1800, max_words=100, stopwords=stopwords,
                          background_color='white', contour_width=3, contour_color='steelblue')
    wordcloud.generate(text)
    wordcloud.to_file('m6b.png')



if __name__ == '__main__':
    wc('ts.csv')
