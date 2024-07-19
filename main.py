from playwright.sync_api import sync_playwright

p = sync_playwright().start()

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://11st.co.kr/")

page.fill('input[title="통합검색"]', "김치")

page.click('button[type="submit"][class="search_button"]')


page.wait_for_timeout(5000)
page.evaluate('window.scrollBy(1000, 5000)')

page.wait_for_timeout(10000)