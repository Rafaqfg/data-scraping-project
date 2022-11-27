# Web Scrapping Project

## Developed by
- [@Rafaqfg](https://www.linkedin.com/in/rafaelqfg/)
## Description
- In this project I created a python script to scrap technologies news from the [Trybe's blog](https://blog.betrybe.com/) .

## Stack
Development: Python, Docker, pymongo, beautifulsoup4 and MongoDB. <br>
## How to run the application with Docker (you need have already docker-compose installed in your machine)<br>
Clone the repository
```bash
  git clone git@github.com:Rafaqfg/web-scraping-project-Python.git
```
Enter in the project folder
```bash
  cd web-scraping-project-Python
```
Create and activate the virtual environment for the project
```bash
  python3 -m venv .venv && source .venv/bin/activate
```
install the dependencies
```bash
  python3 -m pip install -r dev-requirements.txt
```
📌 Note: If during the installation you received some red error message just repeat the previous step until the error message is gone.<br>
<br>
Up the Docker containers using the compose file (door 27017 must be avaible)
```bash
  docker-compose up -d
```
Run the menu.py file
```bash
   python3 tech_news/menu.py
```
### Enjoy scrapping xD
<br>
📌 Note: All scrapped website is in portuguese, therefore you need to write your searches in portuguese.

##

## Steps of development
| description | finished |
| :--------------------------: | :----- |
| Create the fetch function  | :heavy_check_mark:
| Create the function scrape_novidades | :heavy_check_mark:
| Create the scrape_next_page_link function	| :heavy_check_mark:
| Create the scrape_noticia function | :heavy_check_mark:
| Create the get_tech_news function to get the news! | :heavy_check_mark:
| Create the function search_by_title | :heavy_check_mark:
| create the function search_by_date | :heavy_check_mark:
| Create the function search_by_tag	| :heavy_check_mark:
| Create the function search_by_category | :heavy_check_mark:
| Create the function top_5_news | :heavy_check_mark:
| Create the function top_5_categories | :heavy_check_mark:
| Create the menu function	| :heavy_check_mark:
| Implement the menu features | :heavy_check_mark:

## Gif of the application
![](https://github.com/Rafaqfg/data-scraping-project-Python/blob/main/data_scrapping.gif)
