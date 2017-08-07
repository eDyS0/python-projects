import feedparser
import html2text
import sys

"""
RSSFeedCreator.py - takes a RSS link in paramater and returns the title, link and content of that RSS.
"""

if len(sys.argv) > 1:
	feed = feedparser.parse(sys.argv[1])
	if len(feed['entries']) <= 0:
		print('Either the RSS is empty or your RSS link is incorrect.')
	else:
		for post in feed['entries']:
			print(post['title'] + ":  " + (post['link']))
			print(html2text.html2text(post['content'][0]['value']))
			print('*' * 50)
else:
	print("Usage: python feedparser.py <RSS link>", file=sys.stderr)
