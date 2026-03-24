from __future__ import annotations

RSS_SOURCES: dict[str, list[str]] = {
    "Technology": [
        "https://feeds.feedburner.com/TechCrunch",
        "https://www.wired.com/feed/rss",
        "https://feeds.arstechnica.com/arstechnica/index",
        "https://www.theverge.com/rss/index.xml",
    ],
    "Business": [
        "https://feeds.bloomberg.com/markets/news.rss",
        "https://feeds.reuters.com/reuters/businessNews",
        "https://feeds.a.dj.com/rss/RSSMarketsMain.xml",
    ],
    "Science": [
        "https://www.sciencedaily.com/rss/all.xml",
        "https://feeds.nature.com/nature/rss/current",
        "https://rss.nytimes.com/services/xml/rss/nyt/Science.xml",
    ],
    "Health": [
        "https://rss.nytimes.com/services/xml/rss/nyt/Health.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/Well.xml",
    ],
    "World": [
        "https://feeds.bbci.co.uk/news/world/rss.xml",
        "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "https://www.aljazeera.com/xml/rss/all.xml",
    ],
    "Sports": [
        "https://www.espn.com/espn/rss/news",
        "https://feeds.bbci.co.uk/sport/rss.xml",
    ],
    "Entertainment": [
        "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml",
        "https://variety.com/feed/",
    ],
}
