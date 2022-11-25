import requests
import time
from parsel import Selector
from bs4 import BeautifulSoup
import re
from tech_news.database import create_news


def fetch(url):
    try:
        time.sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
            )
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.ReadTimeout:
        return None


def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    title = selector.css("h2.entry-title a::attr(href)").getall()
    return title


def scrape_next_page_link(html_content):
    try:
        selector = Selector(text=html_content)
        next_page = selector.css(".next::attr(href)").get()
        return next_page
    except FileNotFoundError:
        return None


def scrape_noticia(html_content):
    REPLACE_BEFORE = '\xa0'
    REPLACE_AFTER = ''
    selector = Selector(text=html_content)
    soup = BeautifulSoup(html_content, features='lxml')

    url = soup.select_one('link[rel="canonical"]')['href']
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css(".comment-list").getall()
    summary = selector.css("div.entry-content p").get()
    tags = selector.css("section.post-tags a::text").getall()
    category = selector.css("span.label::text").get()
    removing_chars = re.compile('<.*?>')
    cleaning_text = re.sub(removing_chars, '', summary)

    return({
         "url": url,
         "title": title.replace(REPLACE_BEFORE, REPLACE_AFTER),
         "timestamp": timestamp,
         "writer": writer,
         "tags": tags,
         "summary": cleaning_text.replace(
            REPLACE_BEFORE, REPLACE_AFTER).replace(
                "Storytelling. ", "Storytelling."
                ),
         "comments_count": len(comments_count),
         "category": category
        })


def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    url_list = []
    content_list = []
    while len(url_list) < amount:
        website = fetch(url)
        data = scrape_novidades(website)
        url_list.extend(data)
        url = scrape_next_page_link(website)

    content_list = [scrape_noticia(fetch(new_url))
                    for new_url in url_list[0:amount]
                    ]

    create_news(content_list)
    return content_list
