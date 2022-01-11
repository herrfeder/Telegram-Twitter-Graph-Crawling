# Telegram Twitter Graph Crawling


## How to run

  * in either `telegram_crawl` or `twitter_crawl` move `template.env` to `secrets.env` and fill with necessary information
  * now execute `./run <script-to-run>`

## Telegram Crawl

  1. it's intended that you run `01_search_telegram.py` with a own search query for accessible PeerGroups on this location

```python
search = 'Crypto'
result = await client(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))
```

  2. After crawling some initial Groups run `02_crawl_telegram.py` to gather and crawl all links and forwarded groups that could be found in step 1
