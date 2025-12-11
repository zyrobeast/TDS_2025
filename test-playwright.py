from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

# s = 0

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=True)
#     page = browser.new_page()

#     for i in range(70, 80):
#         page.goto(f"https://sanand0.github.io/tdsdata/js_table/?seed={i}")
#         soup = BeautifulSoup(page.content(), "html.parser")

#         s += sum(int(td.get_text(strip=True)) for td in soup.find_all("td"))

#     browser.close()

# print(s)

###################################################################################################

html = """
<div id="result"></div>
<script>
  document.querySelector("#result").innerHTML = atob(`
UTgzNC4gRG93bmxvYWQgPGEgaHJlZj0iaHR0cHM6Ly9leGFtcGxlLmNvbS9kYXRhLXE4MzQucGRmIj5
maWxlPC9hPi4KV2hhdCBpcyB0aGUgc3VtIG9mIHRoZSAidmFsdWUiIGNvbHVtbiBpbiB0aGUgdGFibG
Ugb24gcGFnZSAyPwoKUG9zdCB5b3VyIGFuc3dlciB0byBodHRwczovL2V4YW1wbGUuY29tL3N1Ym1pd
CB3aXRoIHRoaXMgSlNPTiBwYXlsb2FkOgoKPHByZT4KewogICJlbWFpbCI6ICJ5b3VyLWVtYWlsIiwK
ICAic2VjcmV0IjogInlvdXIgc2VjcmV0IiwKICAidXJsIjogImh0dHBzOi8vZXhhbXBsZS5jb20vcXV
pei04MzQiLAogICJhbnN3ZXIiOiAxMjM0NSAgLy8gdGhlIGNvcnJlY3QgYW5zd2VyCn0KPC9wcmU+`);
</script>
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.set_content(html)

    result = page.inner_html("#result")
    print(result)

    browser.close()



