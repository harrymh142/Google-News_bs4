<h1 align = "center">
  <img src = "https://www.androidcentral.com/sites/androidcentral.com/files/article_images/2019/12/google-news-2019-app-icon.jpg" height = "150" width = "auto">
  <br>
  Google News
  <br>
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Made%20with&message=Python&color=red&logo=python&logoColor=white" />
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Python&message=3.7.7&color=red&logo=python&logoColor=white" />
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Use%20of&message=Web%20Scraping&color=red&logo=google-chrome&logoColor=white" />
  <img alt="GitHub Top Language" src="https://img.shields.io/static/v1?label=Made%20with&message=BeautifulSoup&color=red" />
</h1>


### What is Google News?
Simple News app built in Python using Beautiful-soup web scraping.

<br>

### How to use?
Download **GoogleNews.py** file and add into your project.

<br>

### How to get user agent?
Search **my user agent** into your chrome.

<br>

### Code Part
```python

from GoogleNews import GoogleNews
news = GoogleNews("your user agent")

```

<br>

## Methods

#### getTopStories( )
return top storie's headlines from google news.
```python

news.getTopStories()

```

#### getForYou( )
return headlines recommended based on your interests.
```python

news.getForYou()

```

#### getCoronaNews( )
return headlines of corona news.
```python

news.getCoronaNews()

```

#### getCountryNews( )
return headlines of your country.
```python

news.getCountryNews()

```

#### getWorldNews( )
return headlines of world.
```python

news.getWorldNews()

```

#### getTechnologyNews( )
return headlines of technology.
```python

news.getTechnologyNews()

```

#### getEntertainmentNews( )
return headlines of entertainment.
```python

news.getEntertainmentNews()

```

#### getSportsNews( )
return headlines of sports.
```python

news.getSportsNews()

```

#### getScienceNews( )
return headlines of science.
```python

news.getScienceNews()

```

#### getHealthNews( )
return headlines of health.
```python

news.getHealthNews()

```