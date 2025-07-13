from playwright.sync_api import sync_playwright
import os

file_path = f"file://{os.getcwd()}/sample_pages/sample1.html"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(file_path)

    # XPath examples
    page.locator("//input[@id='username']").fill("Taneshka")
    page.locator("//input[@type='password']").fill("secret")
    page.locator("//button[contains(@class, 'login')]").click()

    mango = page.locator("//li[text()='Mango']").inner_text()
    print("Mango item found:", mango)

    browser.close()