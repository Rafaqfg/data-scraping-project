from tech_news.scraper import get_tech_news
from tech_news.analyzer import search_engine
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys


def menu_options():
    print(
        "Choose one option:"
        "\n 0 - Fill the database with scrapped news;"
        "\n 1 - Find news by title;"
        "\n 2 - Find news by date;"
        "\n 3 - Find news by tag;"
        "\n 4 - Find news by category;"
        "\n 5 - List top 5 news;"
        "\n 6 - List top 5 categories;"
        "\n 7 - exit."
        "\n ",
        end="",
    )


def get_news():
    inserted_data = None
    while not isinstance(inserted_data, int):
        try:
            inserted_data = int(input("How many news to be scrapped:"))
        except ValueError:
            print("Must be an integer.")

    scrapped_news = get_tech_news(inserted_data)
    print(scrapped_news)
    menu()


def get_news_by_title():
    inserted_data = input("Title:")
    news_by_title = search_engine.search_by_title(inserted_data)
    print(news_by_title)
    menu()


def get_news_by_date():
    inserted_data = input("Date(aaaa-mm-dd):")
    news_by_date = search_engine.search_by_date(inserted_data)
    print(news_by_date)
    menu()


def get_news_by_tag():
    inserted_data = input("Tag:")
    news_by_tag = search_engine.search_by_tag(inserted_data)
    print(news_by_tag)
    menu()


def get_news_by_category():
    inserted_data = input("Category:")
    news_by_category = search_engine.search_by_category(inserted_data)
    print(news_by_category)
    menu()


def get_top_5_news():
    print(top_5_news())
    menu()


def get_top_5_categories():
    print(top_5_categories())
    menu()


def end():
    print("Closing... See you soon, bye!\n")
    exit()


def menu():
    options = {
        "0": get_news,
        "1": get_news_by_title,
        "2": get_news_by_date,
        "3": get_news_by_tag,
        "4": get_news_by_category,
        "5": get_top_5_news,
        "6": get_top_5_categories,
        "7": end,
    }
    menu_options()
    try:
        start = input()
        options[start]()
    except KeyError:
        print("Invalid option", file=sys.stderr)
    menu()


input(menu())
