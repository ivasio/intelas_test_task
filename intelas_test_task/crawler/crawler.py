from dataclasses import dataclass
from typing import List, Optional
from functools import lru_cache

from bs4 import BeautifulSoup
import requests


@dataclass
class CrawledPage:
    url: str
    nested_pages: Optional[List['CrawledPage']]


@lru_cache(1024)
def get_links_on_page(url: str) -> List[str]:
    try:
        response = requests.get(url, timeout=2)
    except requests.RequestException:
        return []

    data = response.text
    soup = BeautifulSoup(data, 'lxml')

    links = []
    for link in soup.find_all('a'):
        link_url = link.get('href')

        if link_url is not None and link_url.startswith('http'):
            links.append(link_url + '\n')

    return links


def crawl_link(url: str, depth: int) -> Optional[CrawledPage]:
    if depth == 3:
        return None

    links_on_page = get_links_on_page(url)
    crawled_pages = [crawl_link(link, depth + 1) for link in links_on_page]
    return CrawledPage(
        url=url,
        nested_pages=crawled_pages if any(crawled_pages) else None
    )


def crawl(start_url: str) -> CrawledPage:
    return crawl_link(start_url, 0)
