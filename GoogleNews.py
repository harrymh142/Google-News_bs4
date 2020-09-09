import requests
from bs4 import BeautifulSoup

class GoogleNews:

  def __init__(self, userAgent):
    '''
    ### GoogleNews
    Create new instance of google news.
    '''
    self.header = {"User-Agent" : userAgent}

  def getTopStories(self):
    '''
    ### getTopStories( )
    return top storie's headlines from google news.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topstories?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getForYou(self):
    '''
    ### getTopStories( )
    return headlines recommended based on your interests.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvTkwyY3ZNVEZpWXpVNGJIcHdheElGWlc0dFIwSW9BQVAB?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getCoronaNews(self):
    '''
    ### getCoronaNews( )
    return headlines of corona news.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqIggKIhxDQkFTRHdvSkwyMHZNREZqY0hsNUVnSmxiaWdBUAE?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getCountryNews(self):
    '''
    ### getCountryNews( )
    return headlines of your country.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/search?q=deutschland&hl=de&gl=DE&ceid=DE%3Ade', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getWorldNews(self):
    '''
    ### getWorldNews( )
    return headlines of world.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList
  
  def getTechnologyNews(self):
    '''
    ### getTechnologyNews( )
    return headlines of technology.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtVnVHZ0pKVGlnQVAB?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getEntertainmentNews(self):
    '''
    ### getEntertainmentNews( )
    return headlines of entertainment.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getSportsNews(self):
    '''
    ### getSportsNews( )
    return headlines of sports.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getScienceNews(self):
    '''
    ### getScienceNews( )
    return headlines of science.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtVnVHZ0pKVGlnQVAB?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList

  def getHealthNews(self):
    '''
    ### getHealthNews( )
    return headlines of health.
    #### Return Type : `list()`
    '''
    content = requests.get('https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNR3QwTlRFU0FtVnVLQUFQAQ?hl=de&gl=DE&ceid=DE:de', headers= self.header).content
    pageSource = BeautifulSoup(content , "html.parser")
    newsList = []
    for i in pageSource.find_all(class_ = 'DY5T1d'):
      newsList.append(i.get_text())
    return newsList
