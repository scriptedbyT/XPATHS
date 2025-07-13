# 🧭 XPath Common Syntax

This repository contains a quick-reference to the most **commonly used XPath expressions** for web automation and scraping.  
Perfectly works with **Selenium**, **Playwright**, **BeautifulSoup**, or **UiPath**.

---

## 📌 Basic XPath Protocols

- `//` → Selects nodes anywhere in the document (relative XPath)
- `/`  → Selects from the root (absolute XPath)
- `@`  → Refers to attributes (e.g., `@id`, `@class`)
- `*`  → Wildcard to match any tag
- `text()` → Refers to visible text inside an element

---

## 🔤 Common XPath Syntax & Usage

| Syntax Example                        | Description                                   |
|--------------------------------------|-----------------------------------------------|
| `//tagname`                          | All elements with that tag (e.g., `//div`)    |
| `//input[@id='username']`            | Element with specific ID                      |
| `//button[@name='submit']`           | Element with a specific attribute             |
| `//*[@class='btn primary']`          | Any element with class 'btn primary'          |
| `//a[@href='/login']`                | Anchor with specific href                     |

---

## 🔎 Text-Based XPath

| Syntax Example                        | Description                                  |
|--------------------------------------|----------------------------------------------|
| `//h1[text()='Welcome']`             | Element with exact text "Welcome"            |
| `//li[contains(text(), 'Apple')]`    | List item containing text "Apple"            |
| `//*[contains(@placeholder, 'Enter')]`| Placeholder contains the word "Enter"       |

---

## 🔗 Functions in XPath

| Function       | Example                                     | Purpose                          |
|----------------|---------------------------------------------|----------------------------------|
| `text()`       | `//span[text()='Logout']`                  | Match visible text exactly       |
| `contains()`   | `//div[contains(@class, 'alert')]`         | Partial match                    |
| `starts-with()`| `//input[starts-with(@name, 'user')]`      | Match beginning of attribute     |
| `last()`       | `//ul/li[last()]`                          | Last item in a list              |
| `position()`   | `//table/tr[position() < 3]`               | First two rows of a table        |

---

## 🔁 XPath with Indexing

| Syntax                        | Description                      |
|-------------------------------|----------------------------------|
| `//ul/li[1]`                  | First list item                  |
| `//ul/li[3]`                  | Third list item                  |
| `//ul/li[last()]`             | Last list item                   |
| `//div[@class='row'][2]`      | Second div with class "row"      |

---

## 🔄 XPath Axes (Optional Advanced)

| Axis            | Example                             | Description                      |
|------------------|-------------------------------------|----------------------------------|
| `parent::`        | `//span/parent::div`               | Select parent node               |
| `child::`         | `//div/child::input`               | Select direct children           |
| `ancestor::`      | `//input/ancestor::form`           | Select wrapping parent form      |
| `descendant::`    | `//ul/descendant::li`              | All nested list items            |
| `following::`     | `//label/following::input`         | Input after a label              |
| `preceding::`     | `//input/preceding::label`         | Label before an input            |

---

## 🛠️ Tips for Writing Better XPath

- ✅ Prefer **relative XPath** (`//`) over absolute
- ✅ Use `contains()` for dynamic attribute values
- ✅ Use `text()` for buttons/labels instead of relying on attributes
- ✅ Combine conditional operators for accuracy:
  ```xpath
  //button[contains(@class, 'btn') and text()='Login']

---
