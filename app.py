from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:

    # Launch Browser
    browser = playwright.chromium.launch(headless=False, slow_mo=700)

    # Playwright Tracing
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    # Create a new page/tab
    page = context.new_page()

    # Visit playwright website
    page.goto("https://playwright.dev/python/")

    # Locate link element with "Docs" text
    docs_button = page.get_by_role('link', name="Docs")
    docs_button.click()

    # Get URL
    print("Docs: ", page.url)

    # Closes Tracing
    context.tracing.stop(path = "trace.zip")

    # Close browser
    browser.close()