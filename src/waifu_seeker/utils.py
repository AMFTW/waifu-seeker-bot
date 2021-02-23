"""
Utility functions for the bot.
"""
import random

import bs4


def get_rand_img_url(page: str, url_limit: int) -> str:
    """
    Returns a random image url from `page`.

    :param page: The raw HTML from a google image search webpage.
    :param url_limit: Maximum number of URLs to search for image URLs.
    :returns: A randomly selected image URL from `page`.
    """
    urls = []
    # Creating intermediate variables speeds up web scraping
    soup = bs4.BeautifulSoup(page, 'html.parser')
    for _ in range(url_limit):
        for img in soup.find_all('img'):
            url = img.get('src')
            if url:
                urls.append(url)
    return random.choice(urls)
