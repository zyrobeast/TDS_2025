from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

s = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for i in range(70, 80):
        page.goto(f"https://sanand0.github.io/tdsdata/js_table/?seed={i}")
        soup = BeautifulSoup(page.content(), "html.parser")

        s += sum(int(td.get_text(strip=True)) for td in soup.find_all("td"))

    browser.close()

print(s)


