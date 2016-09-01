'''This file retrieves the data from
a website for the Markov Chain application.
This text will be used to generate a 
Markov Chain by utilizing the run.py
and the Markov Chain module provided by
Codecademy.

Written by: Kathy Musiak
'''

import urllib2
from bs4 import BeautifulSoup
from bs4 import Tag
#from HTMLParser import HTMLParser
import lxml
from lxml.html.clean import Cleaner
from lxml import etree
from bs4 import NavigableString
from urllib2 import HTTPError, URLError
from sys import exit
#import html2text

'''
class MLStripper(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.reset()
		self.fed = []
	def handle_data(self, d):
		self.fed.append(d)
	def get_data(self):
		return ''.join(self.fed)
'''		
	
def fetch(url):
    
    request = urllib2.Request(url)
    try: html = urllib2.urlopen(request)
    except ValueError, e:
	    print 'Value error: %s' % e
	    exit()
    except urllib2.HTTPError, e:
		print 'There is an HTTP problem.'
		print 'Error: %s' % e
		exit()
    except urllib2.URLError, e:
		print 'There is a problem with the URL'
		print 'URL error: %s' % e
		exit()
		
		#if hasattr(e, 'reason'):
		#	print 'We failed to reach the server.'
		#	print 'Reason: ', e.reason
		#elif hasattr(e, 'code'):
		#	print 'The server could not fulfill the \'.'
		#	print 'Error code: ', e.code
    else:

        html = html.read()
	    #Pass website data to Beautiful Soup4 for parsing.
	soup = BeautifulSoup(html, "lxml")
	    #strip script and style tags
	    #for script in soup(["script", "style"]):
        for script in soup(["script", "style"]):
            script.extract()
    	
	    # get text from the soup
	    text = soup.get_text()

	    # break into lines and remove leading and trailing space on each
	    lines = (line.strip() for line in text.splitlines())
	    # break multi-headlines into a line each
	    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	    # drop blank lines
	    text = '\n'.join(chunk for chunk in chunks if chunk)
	
	    #change the encoding so that this will print to the screen
	    #and write to the file
	    text = text.encode('utf-8')
	
	    '''open the file fetch_data2 for writing to write
	    data that is stripped of HTML and other code'''
	
	    file1 = open('fetch_data2.txt', 'w')
	    data = str(text)
	    file1.write(data)
	    file1.close()
	
'''
def strip_tags(soup):
	parsed=MLStripper()
	parsed.feed(soup)
	return parsed.get_data()
'''