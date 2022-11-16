from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    db = get_collection()

    news = (
        db.find()
        .sort(
            [
                ('comments_count', -1),
                ('title', 1)
            ]
        )
        .limit(5)
    )
    return [tuple([new["title"], new["url"]]) for new in news]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
