from contextlib import suppress
from dataclasses import dataclass
from typing import List, Self
from selectolax.parser import HTMLParser
from playwright.sync_api import sync_playwright


@dataclass
class GoogleSearchResult:
    url: str
    title: str
    description: str


class Google:
    BASE_URL = "https://www.google.com/search?q="

    def __init__(self) -> None:
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    @staticmethod
    def get_googlesearch_result(html: str) -> List[str]:
        parser = HTMLParser(html)
        result_block = parser.css("div.g")
        for result in result_block:
            with suppress(Exception):
                url = result.css_first("a[href]").attrs["href"]
                title = result.css_first("h3").text()
                description_box = result.css_first(
                    'div[style="-webkit-line-clamp:2"]'
                ).text()
                yield GoogleSearchResult(url, title, description_box)

    def search(self, query: str) -> List[GoogleSearchResult]:
        url = f"{self.BASE_URL}{query}"
        self.page.goto(url)
        content = self.page.content()
        return self.get_googlesearch_result(content)

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        print("exit")
        self.context.close()
        self.browser.close()
        self.playwright.stop()
