import requests #lib to send HTTP requests
import feedparser
from plyer import notification

#fetch headlines from google news

def fetch(max_words=8):
	url = 'http://news.google.com/rss'
	feed = feedparser.parse(url) #parse rss feed from google
	headlines = []
	for entry in feed.entries[:3]: #get top 3
		title_words = entry.title.split()
		shorten = ' '.join(title_words[:max_words]) + '...'
		source = entry.source.title if hasattr(entry, 'source') else 'Unknown Source'
		formatted = f"{shorten} ({source})"
		headlines.append(formatted)
	return headlines

def notify(headlines):
	summary = "\n".join(headlines) #max len is 256 char
	message = f"{summary}\n\n For more news, visit: https://news.google.com"
	if len(message) > 256:
		message=message[:253] +'...'

	notification.notify(
		title="News of the Day",
		message=message,
		timeout=10
	)

if __name__== "__main__":
	headlines = fetch(max_words=8)
	notify(headlines)


#used a batch script to automate a notification every day windows
