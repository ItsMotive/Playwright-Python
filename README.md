# Using Playwright with Python

## Description
- A small project to help recall setting up Playwright using Python with some examples.

## Table Of Contents
- [Asynchronous vs Synchronous](#async-vs-sync)
- [Initial Install](#initial-install)
- [Setting up Basic Synchronous Project](#Setting-up-Basic-Synchronous-Project)
- [REPL](#Using-REPL)
- [Locators](#locators)

## Async vs Sync
Choosing Between Sync and Async
- Use Sync if:
   - You prefer a simpler, more linear code flow.
   - Your tests do not require concurrent operations and the performance impact is minimal.
     
- Use Async if:
   - You need to perform operations concurrently to speed up test execution.
   - You are comfortable with handling Promise chains and async/await patterns.
     
- Comparison Table:
  | Aspect | Synchronous | Asynchronous |
  | ---- | ---- | ---- |
  | Execution Flow | Blocking, Step by Step | Non-Blocking, Concurrent Operations |
  | Code Complexity | Simpler, more linear | More Complex, Requires async/await |
  | Error Handling | Standard Try-Catch Blocks | Requires handling Promises and Async error |
  | Performance | Generally slower, as each step waits for the previous one to complete | Potentially faster due to parallel execution |
  | Use Case | Preferred for simpler scripts and linear tasks | Ideal for complex tasks that benefit from concurrency |
  | Readability | Easier to read and write | Requires understanding of asynchronous programming |
  | Learning Curve | Lower, suitable for beginners | Higher, requires familiarity with async patterns |
  | Examples | from playwright.sync_api import sync_playwright | from playwright.async_api import async_playwright |
  | Function Example | def run_sync() | async def run_async() |
  | Execution Example | run_sync() | asyncio.run(run_async()) |

## Initial Install
1. (Optional) Create Virtual Environment
   - Using Visual Studio Code, you can run this command in the terminal:
   ```
   python -m venv venv
   ```
   - You can then run this command to start the virtual environment:
   ```
   .\venv\Scripts\activate
   ```
   
2. Install Playwright
   ```
   pip install playwright
   ```
   
3. Install Playwright Drivers
   ```
   playwright install
   ```

## Setting up Basic Synchronous Project
- Libraries to Import:
  ``` python
  from playwright.sync_api import sync_playwright
  ```

- Main Code:
  ``` python
  with sync_playwright() as playwright:
    # Launch Browser
    browser = playwright.chromium.launch(headless=False)
    # Create a new page/tab
    page = browser.new_page()
    # Visit playwright website
    page.goto("https://playwright.dev/python/")
    # Close browser
    browser.close()
  ```

## Using REPL
- REPL is basically an interactive tester. With this, you will be able to locate and highlight elements realtime.
- Getting Started
  1. Open Terminal and Navigate to Project Directory
  2. Activate the Virtual Environment
  3. Run command to start python
     ```
     python
     ```
     or
     ```
     ptpython
     ```
  4. Start Coding:
     ```
     from playwright.sync_api import sync_playwright
     playwright = sync_playwright().start()
     browser = playwright.chromium.launch(headless=False, slow_mo=700)
     page = browser.new_page()
     page.goto("https://playwright.dev/python/")
        ```

## Locators
- 
