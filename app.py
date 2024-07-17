from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    # Launch Browser
    browser = playwright.chromium.launch(headless=False, slow_mo=700)

    # Create a new page/tab
    page = browser.new_page()

    # Visit playwright website
    page.goto("https://playwright.dev/python/")

    # Locate link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()

    # Get URL
    print("Docs: ", page.url)

    # Close browser
    browser.close()