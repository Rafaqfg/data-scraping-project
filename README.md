# Data Scrapping Project

## Developed by
- [@Rafaqfg](https://www.linkedin.com/in/rafaelqfg/)
## Description
- In this project I created a python script to scrap technologies news from the [Trybe's blog](https://blog.betrybe.com/) .

## Stack
Development: Python, Docker, pymongo, beautifulsoup4 and MongoDB. <br>
## How to run the application with Docker (you need have already docker-compose installed in your machine)<br>
Clone the repository
```bash
  git@github.com:Rafaqfg/data-scraping-project.git
```
Enter in the project folder
```bash
  cd data-scraping-project
```
Create and activate the virtual environment for the project
```bash
  python3 -m venv .venv && source .venv/bin/activate
```
install the dependencies
```bash
  python3 -m pip install -r dev-requirements.txt
```
📌 Note: If during the installation you received some red error message just repeat the previous step until the error message is gone.
Up the Docker containers using the compose file (door 27017 must be avaible)
```bash
  docker-compose up -d
```
Run the menu.py file
```bash
   python3 tech_news/menu.py
```
```bash
   Enjoy scrapping xD
```
📌 Note: All scrapped website is in portuguese, therefore you need to write your searches in portuguese.
