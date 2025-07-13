# 🔍 XPath Examples

## 🎯 Basics
- `//input` → All input fields
- `//input[@id='username']` → Username input field
- `//button[contains(@class, 'login')]` → Login button
- `//li[text()='Mango']` → List item with exact text 'Mango'

## 🧠 Advanced
- `//ul/li[last()]` → Last list item
- `//input[@placeholder='Enter Username']` → Placeholder attribute matching
- `//h1 | //button` → Select all h1 and button elements
- `//*[@*='login']` → Any element with any attribute containing 'login'