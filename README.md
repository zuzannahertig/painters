# Exploring  painters' popularity with Wikimedia REST API
Program that scrapes a list of 3470 painters from en.wikipiedia.org and a list of 262 Polish painters from pl.wikiedia.org. It makes use of Wikimedia REST API to retrieve monthly pageviews for each of the artists in 2022. 
It creates and populates SQLite database with the data, enabling easy exploration of painters' popularity via SQL queries. 


## Technologies:
* Scrapy
* BeautifulSoup
* SQlite3
* Pandas
