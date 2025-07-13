# 🧭 XPath Documentation

This repository is a guide and hands-on practice set for **XPath** — the language used to navigate and locate elements in HTML and XML documents. It’s especially useful for automation testing, web scraping, and XML processing.

---

## 📌 What is XPath?

**XPath (XML Path Language)** is used to locate elements in a document using tag names, attributes, text content, hierarchy and relationships.

It is heavily used in:
- ✅ Selenium / Playwright (for UI automation)
- ✅ BeautifulSoup / lxml (for scraping)
- ✅ UiPath / TestComplete (for RPA testing)

---

## 🆚 Absolute vs Relative XPath

### 📍 Absolute XPath
Starts from the root of the HTML tree and goes down the path. Can be lengthy someties or might break if page structure changes.

### 📍 Relative XPath
Starts from anywhere in the DOM using //. More flexible and preferred.

```xpaths
Absolute : /html/body/div[1]/form/input[1]
Relative : //input[@id='username']
