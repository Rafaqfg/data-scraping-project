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
    db = get_collection()

    get_categories = list(db.aggregate([
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}}, ]
    ))

    return [category["_id"] for category in get_categories[0:5]]

# https://www.mongodb.com/docs/manual/reference/method/db.collection.aggregate/
# https://www.mongodb.com/docs/manual/core/aggregation-pipeline/
