from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    search = search_news({
        "title": {"$regex": title, "$options": "i"}
    })
    return [(news["title"], news["url"]) for news in search]


# Requisito 7
def search_by_date(date):
    try:
        convert_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        search = search_news({
            "timestamp": {"$regex": convert_date}})
        return [(news["title"], news["url"]) for news in search]

    except Exception:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
