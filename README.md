# Regex Email & Phone Number Checker

A mini Python project demonstrating Regular Expression (regex) pattern matching for validating email addresses and phone numbers. Written as a companion to my Medium tutorial on regex for beginners.

---

## Project Description

The program reads a set of predefined inputs and runs each one through a regex-based validation function. It prints whether each input matches the expected format or not. Two validators are included:

- **`chkMailForm(txt)`** — validates email address format
- **`chkPhonNum(txt)`** — validates Thai-style phone number format

For a detailed explanation of the code, see my Medium post: [Regular Expression for Beginners](https://medium.com/@natakornch/regular-expression-for-beginners-d5e3e4bbeb3)

---

## Pattern Requirements

### Email

| Rule | Detail |
|------|--------|
| Local part | Any string before `@` |
| Domain | Must be `testmail` (e.g. `xxx@testmail.xxx`) |
| Extension | Only `.com` or `.net` are accepted |

**Valid examples:** `white@testmail.net`, `red@testmail.com`  
**Invalid examples:** `yellow@hotmail.com`, `brown@testmail.co`, `black@testmail.nnet`

### Phone Number

| Rule | Detail |
|------|--------|
| No letters | Alphabetic characters are not allowed |
| Starting with `02` | Must be exactly 9 digits |
| Starting with `08` | Must be exactly 10 digits |
| Other prefixes | Not accepted |

**Valid examples:** `023912483`, `0847837273`  
**Invalid examples:** `0239124834` (02 too long), `02391248` (02 too short), `084783727j` (contains letter), `0147837273` (invalid prefix)

---

## Prerequisites

- Python 3 (the `re` module is included in the standard library — no extra install needed)
- Any code editor (VS Code, PyCharm, or Jupyter Notebook)

---

## Running the Project

```bash
python regex_chk_mail_phone.py
```

No external dependencies are required.

---

## Expected Output

```
Email format is incorrect: yellow@hotmail.com
Email format is incorrect: brown@testmail.co
Email format is incorrect: orange@gmail.net
Email format is incorrect: black@testmail.nnet
Email format is correct: white@testmail.net
Email format is correct: red@testmail.com
Phone nubmer format is correct: 023912483
Phone nubmer format is incorrect: 0239124834
Phone nubmer format is incorrect: 02391248
Phone nubmer format is correct: 0847837273
Phone nubmer format is incorrect: 084783727
Phone nubmer format is incorrect: 08478372733
Phone nubmer format is incorrect: 084783727j
Phone nubmer format is incorrect: 0147837273
```
