from tech_news.scraper import get_tech_news


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


def menu():
    ...