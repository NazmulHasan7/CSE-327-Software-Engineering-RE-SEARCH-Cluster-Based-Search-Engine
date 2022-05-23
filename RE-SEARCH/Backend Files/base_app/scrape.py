

# Import libraries
from urllib.request import urljoin
from bs4 import BeautifulSoup
from bs4.builder import TreeBuilder
import requests
from urllib.request import urlparse
from elasticsearch import Elasticsearch
import time
import PyPDF2
import os
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import textract
import unicodedata
import re
import itertools
import sys
from itertools import chain


# Method for crawling a url at next level
def level_crawler(input_url, depth, type, cluster_id):

    links_extern = set()
    control_chars = ''.join(
        map(chr, chain(range(0, 9), range(11, 32), range(127, 160))))

    CONTROL_CHAR_RE = re.compile('[%s]' % re.escape(control_chars))
    text = ''
    links_intern = set()
    temp_urls = set()

    current_url_domain = urlparse(input_url).netloc

    # Creates beautiful soup object to extract html tags
    beautiful_soup_object = BeautifulSoup(
        requests.get(input_url).content, "lxml")

    if(type == 'html'):
        for script in beautiful_soup_object(['style', 'script', '[document]', 'head', 'title']):
            script.extract()
        text = beautiful_soup_object.get_text(strip=True)
        elastic_indexer(text, depth, input_url, cluster_id)

    # handle other file type scraping
    else:
        # If there is no such folder, the script will create one automatically
        folder_location = r"D:\Test folder (2)"
        if not os.path.exists(folder_location):
            os.mkdir(folder_location)

        response = requests.get(input_url)
        

        soup = BeautifulSoup(response.text, "html.parser")
        test = ''
        # Downloading the files
        # download by extension from the given url
        i = 0
        extension = '.' + type

        

        for link in soup.find_all('a',href=True):
            
            if(link['href'].endswith(extension)):
                print(link['href'])
                filename = os.path.join(
                    folder_location, link['href'].split('/')[-1])
                l = urljoin(input_url, link['href'])
               
                with open(filename, 'wb') as f:
                    f.write(requests.get(
                        urljoin(input_url, link['href'])).content)

                
                read = textract.process(filename, encoding='unicode_escape')
                text = read.decode('utf-8')
                
                # test = test + read.decode('utf-8')
                os.remove(filename)
                text = CONTROL_CHAR_RE.sub('', text)
                print("goto indexing")
                elastic_indexer(text, depth, l, cluster_id)
                print("indexed")
        # test = CONTROL_CHAR_RE.sub('', test)
        

        # print(text)

        # test = test.encode()
        # test file to check whether data is scraped or not
        # with open("demo.txt", 'wb') as f:
        # 	f.write(test)
        # 	f.close()
        # print("other file type finished")

    

    # Access all anchor tags from input
    # url page and divide them into internal
    # and external categories
    for anchor in beautiful_soup_object.findAll("a"):
        href = anchor.attrs.get("href")
        if(href != "" or href != None):
            href = urljoin(input_url, href)
            href_parsed = urlparse(href)
            href = href_parsed.scheme
            href += "://"
            href += href_parsed.netloc
            href += href_parsed.path
            final_parsed_href = urlparse(href)
            is_valid = bool(final_parsed_href.scheme) and bool(
                final_parsed_href.netloc)
            if is_valid:
                if current_url_domain not in href and href not in links_extern:
                    
                    links_extern.add(href)
                if current_url_domain in href and href not in links_intern:
                    
                    links_intern.add(href)
                    temp_urls.add(href)
    return temp_urls


def crawl(input_url, depth, type, cluster_id):

    try:
        # Set for storing urls with different domain

        if(depth == 1):
            print("level crawl")
            level_crawler(input_url, depth, type, cluster_id)
            print("scraped!")

        else:
            # BFS tree to crawl all link

            queue = []
            queue.append(input_url)
            for j in range(depth):
                for count in range(len(queue)):
                    url = queue.pop(0)
                    urls = level_crawler(url, j, type, cluster_id)
                    for i in urls:
                        queue.append(i)

        return True

    except Exception as e:
        print('Caught exception while crawling ' + str(input_url))

        return False


def elastic_indexer(text, depth, url, cluster_id):
    
    es_client = Elasticsearch(['http://127.0.0.1:9200'])
    doc = {
        "date": time.strftime("%Y-%m-%d"),
        "currnet_url": url,
        "depth": depth,
        "content": text
    }
    res = es_client.index(index= str(cluster_id), doc_type="_doc", body=doc)
    print("elastic search?:", res["result"])
