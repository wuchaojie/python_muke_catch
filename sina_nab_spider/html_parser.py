#coding=utf-8
from bs4 import BeautifulSoup
import re
import urlparse 


class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
#        links = soup.find_all("a",href=re.compile(r"/item/"))
        links = soup.find_all("a",href=re.compile(r"/nba/"))

        for link in links :
            new_url = link["href"]
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
            
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        #url
        res_data["url"] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        #<a href="http://sports.sina.com.cn/basketball/nba/2017-10-17/doc-ifymviyp2008306.shtml" target="_blank">人物|向现实低头!曾想做老大的他终于放弃了?</a>
        title_node = soup.find("a")
        res_data["title"] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node =soup.find("div",class_="lemma-summary")
        res_data["summary"] = summary_node.get_text()
    
        return res_data
    
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
#        soup = BeautifulSoup(html_cont,"html.parser",from_encodeing="utf-8")
        soup = BeautifulSoup(html_cont,"html.parser")

        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)        
        return new_urls,new_data



