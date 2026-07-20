# 🐍 Python Projects

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Projects](https://img.shields.io/badge/Projects-50%2B-brightgreen)](#-featured-projects)
[![Topics](https://img.shields.io/badge/Topics-Core%20%7C%20GUI%20%7C%20APIs%20%7C%20Scraping%20%7C%20Automation%20%7C%20Flask-orange)](#-projects-by-topic)

This repository documents my Python learning journey through hands-on projects and exercises. It contains the projects I completed while building my Python fundamentals before transitioning into AI engineering, backend development, and larger real-world applications.

---

## 👤 About

A curated collection of Python projects built progressively — starting from core language fundamentals and advancing through GUI development, API integration, web scraping, browser automation, and Flask web development. Each project was built to reinforce a specific concept through practical application.

---

## 🧠 Skills Learned

- **Python Core** — Variables, control flow, functions, OOP, decorators, scope, error handling
- **GUI Development** — Tkinter widgets, Canvas, event-driven programming, Turtle graphics
- **Data Handling** — Pandas, CSV, JSON, file I/O, list/dictionary comprehensions
- **API Integration** — REST APIs, authentication, environment variables, smtplib, multiple third-party services
- **Web Scraping** — BeautifulSoup 4, requests, CSS selectors, regex, ethics & `robots.txt`
- **Browser Automation** — Selenium WebDriver, WebDriverWait, expected conditions, multi-window handling
- **Flask Web Development** — Routing, `render_template`, Jinja2 templating, static files, dynamic URLs
- **Security** — `.env` files, `python-dotenv`, environment-based credential management

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| **Language** | Python 3 |
| **IDE** | PyCharm, VS Code |
| **GUI** | Tkinter, Turtle Graphics |
| **Data** | Pandas, CSV, JSON |
| **APIs** | OpenWeatherMap, Twilio, Pixela, Nutritionix, Sheety, Tequila/Amadeus, Open Trivia DB, ISS API, Kanye REST, YouTube Music (ytmusicapi) |
| **Email** | smtplib, SMTP |
| **Web / Scraping** | HTML, CSS, BeautifulSoup 4, requests |
| **Browser Automation** | Selenium WebDriver, ChromeDriver, speedtest |
| **Web Framework** | Flask, Jinja2 |
| **Version Control** | Git & GitHub |

---

## ⭐ Featured Projects

| Project | Description | Tech |
|---------|-------------|------|
| [Music Time Machine](Music%20Time%20Machine/) | Scrapes Billboard Hot 100 for a given date and builds a YouTube Music playlist | ytmusicapi, BeautifulSoup |
| [Flight Deal Finder](flight-deals/) | Monitors flight prices and sends SMS/email alerts when prices drop below a target | Tequila API, Twilio, Sheety |
| [Gym Booking Automation](Gym-Booking-Automation/) | Selenium bot that auto-books gym classes, handles waitlists, and verifies bookings | Selenium, WebDriverWait |
| [Amazon Price Tracker](Amazon%20Price%20Tracker/) | Monitors Amazon product prices and emails an alert when the price drops | BeautifulSoup, smtplib |
| [X Internet Speed Complaint Bot](X-Complaint-Bot/) | Measures real internet speed and auto-tweets at the ISP if speeds are below promised | speedtest, Selenium |
| [Property Listing Bot](Property-Listing-Bot/) | Scrapes a Zillow-style listing page and auto-fills a Google Form for each result | BeautifulSoup, Selenium |
| [Blog Capstone](blog-page/) | Flask app with dynamic Jinja2 templates pulling posts from an external JSON API | Flask, Jinja2 |
| [Blackjack Game](Blackjack%20Game/) | Complete Blackjack card game with ace handling, OOP structure, and ASCII art | Python, OOP |

---

## 📂 Repository Structure

```
Python-Learning-Journey/
│
├── Core Python/                       # Variables → OOP → Decorators
│   ├── brandNameGenerator.py
│   ├── TipCalculator.py
│   ├── TreasureIslandGame.py
│   ├── rockPaperScissor.py
│   ├── passwordGenerator.py
│   ├── Hangman game/
│   ├── Caeser Cipher/
│   ├── Secret Auction/
│   ├── Simple Calculator/
│   ├── Blackjack Game/
│   ├── Number Gussing Game/
│   └── Higher Lower game/
│
├── GUI & Graphics/                    # Tkinter + Turtle
│   ├── CoffeeMachine.py
│   ├── Coffee Machine (OOPs)/
│   ├── Quiz Game(OOPs)/
│   ├── RandomWalk/
│   ├── spirograph.py
│   ├── spotpainting/
│   ├── TurtleRace/
│   ├── SnakeGame/
│   ├── SnakeGame V0.2/
│   ├── Pong/
│   ├── turtle-crossing/
│   ├── intro_to_tkinter/
│   ├── miles_to_km_converter/
│   ├── pomodoro-app/
│   ├── password_manager/
│   └── flash-card-project/
│
├── APIs & Automation/                 # REST, Email, Notifications
│   ├── MailMerge/
│   ├── NYC_Squirrel_Census_2018/
│   ├── us_states_game/
│   ├── NATO-alphabet/
│   ├── monday_quotes/
│   ├── birthday-wisher/
│   ├── ISS_overhead_notifier/
│   ├── kanye_quotes/
│   ├── quizzler-app/
│   ├── rain_alert/
│   ├── stock-news-notifier/
│   ├── habit-tracker/
│   ├── exercise_tracker/
│   └── flight-deals/
│
├── Web Foundations/                   # HTML & CSS
│   └── web-foundations/
│
├── Web Scraping/                      # BeautifulSoup, requests
│   ├── web-intermediate/
│   ├── Music Time Machine/
│   └── Amazon Price Tracker/
│
├── Browser Automation/                # Selenium bots
│   ├── SeleniumFundamentals/
│   ├── automated-cookie-clicker/
│   ├── Gym-Booking-Automation/
│   ├── Tinder-swipe-bot/
│   ├── X-Complaint-Bot/
│   ├── Social_Media-Follower-Bot/
│   └── Property-Listing-Bot/
│
└── Flask Web Apps/                    # Flask, Jinja2, HTML/CSS
    ├── FlaskFundamentals/
    ├── higher-lower-flask-game/
    ├── my-personal-site/
    ├── Name-Card-Website/
    ├── jinja-fundamentals/
    └── blog-page/
```

---

## 📁 Projects by Topic

<details>
<summary><strong>🟢 Core Python — Variables, Control Flow, Functions, Loops, OOP</strong></summary>

<br>

### Working with Variables
**What I Learnt:** `print()`, string concatenation, variables, `input()`, debugging basics

**What I Built:**
- 🎸 [Band Name Generator](brandNameGenerator.py) — Generates a fun band name by combining user's city and pet name

---

### Data Types & String Manipulation
**What I Learnt:** Strings, integers, floats, booleans, type casting, f-strings, `round()`

**What I Built:**
- 💰 [Tip Calculator](TipCalculator.py) — Splits a restaurant bill among friends with a custom tip percentage

---

### Control Flow & Logical Operators
**What I Learnt:** `if`/`elif`/`else`, comparison operators, logical operators, nested conditions

**What I Built:**
- 🏝️ [Treasure Island Game](TreasureIslandGame.py) — Text-based choose-your-own-adventure game with ASCII art
- 💕 [Love Calculator](loveCalculator.py) — Calculates a "love score" based on letter matching

---

### Randomisation & Python Lists
**What I Learnt:** `random` module, lists, nested lists, index errors

**What I Built:**
- ✊✋✌️ [Rock Paper Scissors](rockPaperScissor.py) — Classic game against the computer with ASCII art visuals

---

### Python Loops
**What I Learnt:** `for` loops, `range()`, `while` loops, accumulation patterns

**What I Built:**
- 🔐 [Password Generator](passwordGenerator.py) — Generates strong random passwords with customizable character counts

---

### Functions & Modules
**What I Learnt:** Defining and calling functions, parameters vs arguments, multiple return values, `import`, ASCII art

**What I Built:**
- 🪓 [Hangman Game](Hangman%20game/) — Full Hangman game with word list, ASCII art stages, and lives tracking
- 🔒 [Caesar Cipher](Caeser%20Cipher/) — Encrypt and decrypt messages using the Caesar Cipher shift algorithm
- 🔨 [Secret Auction](Secret%20Auction/) — A blind auction program where the highest bidder wins
- 🧮 [Simple Calculator](Simple%20Calculator/) — Fully functional calculator with chaining operations

---

### Scope, OOP & Capstone Projects
**What I Learnt:** Local vs. global scope, `global` keyword, OOP (`__init__`, `self`, inheritance), recursion, game state

**What I Built:**
- 🃏 [Blackjack Game](Blackjack%20Game/) — Complete Blackjack card game with proper game rules and ace handling
- 🔢 [Number Guessing Game](Number%20Gussing%20Game/) — Guess the number with Easy/Hard difficulty modes
- 📊 [Higher Lower Game](Higher%20Lower%20game/) — Compare follower counts and guess who has more

</details>

---

<details>
<summary><strong>🟡 GUI Development — Tkinter & Turtle Graphics</strong></summary>

<br>

### Turtle Graphics & Animations
**What I Learnt:** `turtle` module, RGB colors, `colormode(255)`, screen events, `onkey()`, animation with `tracer()`/`update()`

**What I Built:**
- 🐢 [Random Walk](RandomWalk/) — Draws random colorful paths with turtle graphics
- 🌀 [Spirograph](spirograph.py) — Draws beautiful spirograph patterns using turtle graphics
- 🎨 [Spot Painting](spotpainting/) — Recreates a Damien Hirst-style spot painting
- 🐢 [Turtle Race](TurtleRace/) — Colorful turtle racing game with event listeners and random movement

---

### Classic Games with OOP
**What I Learnt:** Multi-class architecture, collision detection, scoring, inheritance, list slicing, game loops

**What I Built:**
- 🐍 [Snake Game V1](SnakeGame/) — Classic Snake with smooth movement, food spawning, and collision detection
- 🐍 [Snake Game V2](SnakeGame%20V0.2/) — Complete Snake with high score tracking, tail collisions, and polished gameplay
- 🏓 [Pong Game](Pong/) — Classic 2-player Pong with ball physics and a scoreboard
- 🚗 [Turtle Crossing Game](turtle-crossing/) — Frogger-style game with increasing difficulty levels

---

### Tkinter Desktop GUIs
**What I Learnt:** Tkinter widgets (Entry, Button, Label, Canvas), `grid()`/`pack()`, `after()`, `messagebox`, `pyperclip`, event-driven programming

**What I Built:**
- ☕ [Coffee Machine (Procedural)](CoffeeMachine.py) — Virtual coffee machine managing resources and coin payments
- ☕ [Coffee Machine (OOP)](Coffee%20Machine%20(OOPs)/) — Refactored Coffee Machine using `CoffeeMaker`, `MoneyMachine`, `Menu` classes
- ❓ [Quiz Game (OOP)](Quiz%20Game(OOPs)/) — True/False quiz game with OOP architecture
- 🖥️ [Intro to Tkinter](intro_to_tkinter/) — Tkinter widget experiments and demos
- 📏 [Miles to KM Converter](miles_to_km_converter/) — GUI unit converter using Tkinter
- 🍅 [Pomodoro App](pomodoro-app/) — Full Pomodoro timer with work/break cycles and countdown display
- 🔑 [Password Manager](password_manager/) — GUI password manager with strong password generation, JSON storage, and search
- 🃏 [Flash Card App](flash-card-project/) — French-to-English flashcard app with progress tracking and Pandas

</details>

---

<details>
<summary><strong>🟠 APIs & Automation — REST APIs, Email, Notifications</strong></summary>

<br>

### Files, CSV & Data
**What I Learnt:** `open()`, file modes, `with` statement, Pandas `DataFrame`, `read_csv()`, list/dictionary comprehensions

**What I Built:**
- ✉️ [Mail Merge](MailMerge/) — Generates personalized letters from a template and a name list
- 🐿️ [NYC Squirrel Census Analysis](NYC_Squirrel_Census_2018/) — Counts squirrels by fur color using Pandas
- 🗺️ [U.S. States Game](us_states_game/) — Interactive quiz on all 50 U.S. states using a Pandas-backed map
- 🔤 [NATO Alphabet Converter](NATO-alphabet/) — Converts words to NATO phonetic alphabet using dictionary comprehension

---

### Email Automation & Dates
**What I Learnt:** `smtplib`, SMTP configuration, `datetime` module, automating by date and weekday

**What I Built:**
- 📧 [Monday Motivation Quotes](monday_quotes/) — Sends a random motivational quote via email every Monday
- 🎂 [Birthday Wisher](birthday-wisher/) — Automatically sends personalized birthday emails from a CSV

---

### REST APIs
**What I Learnt:** API endpoints, parameters, JSON responses, API keys, `.env` files, `python-dotenv`, HTTP methods (GET, POST, PUT, DELETE)

**What I Built:**
- 🛰️ [ISS Overhead Notifier](ISS_overhead_notifier/) — Tracks the ISS position and sends an email when it's overhead at night
- 🌅 [Kanye Quotes App](kanye_quotes/) — Tkinter GUI fetching random Kanye West quotes from an API
- 🧠 [Quizzler App](quizzler-app/) — GUI quiz app pulling questions from the Open Trivia Database API
- 🌧️ [Rain Alert](rain_alert/) — Checks weather forecasts via OpenWeatherMap and sends an SMS via Twilio if rain is expected
- 📈 [Stock News Notifier](stock-news-notifier/) — Monitors stock price changes and sends SMS alerts with relevant news articles
- 📊 [Habit Tracker](habit-tracker/) — Logs daily habits to a Pixela graph using POST/PUT/DELETE API calls
- 🏋️ [Exercise Tracker](exercise_tracker/) — Logs natural language workout input to Google Sheets via Nutritionix and Sheety APIs
- ✈️ [Flight Deal Finder](flight-deals/) — Searches cheapest flights via the Tequila API and sends SMS/email alerts when prices drop

</details>

---

<details>
<summary><strong>🔵 Web Foundations — HTML & CSS</strong></summary>

<br>

### HTML Foundations & Intermediate HTML
**What I Learnt:** HTML document structure, heading/paragraph tags, lists, `<img>`, anchor tags, nested lists, multi-page sites

**What I Built:**
- 🎬 [Movie Ranking Page](web-foundations/HTML%20Projects/movie_ranking/) — HTML page ranking top movies with headings and lists
- 🍳 [Recipe Page](web-foundations/HTML%20Projects/recipe_using_lists/) — Recipe page using nested HTML lists
- 📋 [Nested List Page](web-foundations/HTML%20Projects/Nested%20list/) — Demonstrating complex nested list structures
- 🖼️ [Image Element Page](web-foundations/HTML%20Projects/Image%20Element/) — Practicing image embedding in HTML
- 🔗 [Anchor Tags Page](web-foundations/HTML%20Projects/Anchor%20Tags/) — Creating hyperlinks and navigation

---

### CSS Foundations & Intermediate CSS
**What I Learnt:** Inline/internal/external CSS, selectors (tag, class, ID), specificity, colors (Hex, RGB, HSL), font properties, the Box Model, browser dev tools

**What I Built:**
- 🎨 [Adding CSS](web-foundations/CSS%20Projects/Adding%20CSS/) — Exercises for all three methods of applying CSS
- 🎯 [CSS Selectors](web-foundations/CSS%20Projects/CSS%20Selectors/5.3%20CSS%20Selectors/) — Class, ID, and element selector practice
- 🔠 [Color Vocab Project](web-foundations/CSS%20Projects/Color%20Vocab%20Project/5.4%20Color%20Vocab%20Project/) — Styled color vocabulary grid
- 🎨 [CSS Colors](web-foundations/CSS%20Projects/CSS%20Colors/) — Color format exercises (Hex, RGB, HSL, transparency)
- 🔠 [Font Properties](web-foundations/CSS%20Projects/Font%20Properties/) — Font styling and text layout practice
- 📦 [CSS Box Model](web-foundations/CSS%20Projects/CSS%20Box%20Model/) — Padding, margins, borders, and box sizing
- 🖼️ [CSS Poster Project](web-foundations/CSS%20Projects/CSS%20Poster%20Project/) — Styled poster webpage with custom fonts and borders

</details>

---

<details>
<summary><strong>🟣 Web Scraping — BeautifulSoup, requests, regex</strong></summary>

<br>

### Web Scraping with Beautiful Soup
**What I Learnt:** Scraping ethics (`robots.txt`), `BeautifulSoup`, CSS selectors (`select()`, `select_one()`), live website scraping, chaining data processing

**What I Built:**
- 📰 [YC Top News Scraper](web-intermediate/yc_top_news_scrapper/) — Scrapes Hacker News to find the article with the highest upvotes
- 🎬 [Top 100 Movies Scraper](web-intermediate/100_movies_to_watch/) — Scrapes Empire's top 100 movies list and generates a `movies.txt` file

---

### Scraping + APIs + Email Alerts
**What I Learnt:** Authenticating with external services via browser headers, `re.sub()` for price parsing, email alerts via `smtplib`, `ytmusicapi` authentication flow

**What I Built:**
- 🎵 [Music Time Machine](Music%20Time%20Machine/) — Scrapes the Billboard Hot 100 for a chosen date and builds a YouTube Music playlist
- 🏷️ [Amazon Price Tracker](Amazon%20Price%20Tracker/) — Monitors an Amazon product price and emails an alert when it drops below a target

</details>

---

<details>
<summary><strong>🔴 Browser Automation — Selenium WebDriver</strong></summary>

<br>

### Selenium Fundamentals
**What I Learnt:** Selenium WebDriver setup, `By.ID`/`By.CSS_SELECTOR`/`By.NAME`/`By.XPATH`, `.click()`, `.send_keys()`, `WebDriverWait`, `expected_conditions`, `ChromeOptions`

**What I Built:**
- 🐍 [Python Events Scraper](SeleniumFundamentals/python-events-scrapper.py) — Scrapes python.org events using CSS selectors and `datetime` attributes
- 📋 [Form Auto-Fill Bot](SeleniumFundamentals/wikipedia-scrapper/interaction.py) — Automatically fills and submits a newsletter signup form
- 🍪 [Cookie Clicker Bot](automated-cookie-clicker/) — Plays Cookie Clicker autonomously for 5 minutes, buying upgrades in a loop

---

### Real-World Automation Bots
**What I Learnt:** Persistent Chrome profiles (`--user-data-dir`), multi-window handling (`window_handles`, `switch_to.window()`), `execute_script()` clicks, retry logic, `speedtest` library, `ElementClickInterceptedException`

**What I Built:**
- 🏋️ [Gym Booking Automation](Gym-Booking-Automation/) — Auto-books gym classes, handles waitlists, and verifies bookings with a QA summary
- 💘 [Tinder Auto-Swipe Bot](Tinder-swipe-bot/) — Logs in via Facebook OAuth and auto-likes 100 profiles with error recovery
- 📶 [X Internet Speed Complaint Bot](X-Complaint-Bot/) — Measures real internet speed via `speedtest` and auto-tweets at the ISP if speeds underperform
- 🤳 [Instagram Follower Bot](Social_Media-Follower-Bot/) — Scrolls a target account's follower list and follows each user
- 🏠 [Property Listing Bot](Property-Listing-Bot/) — Scrapes a Zillow-style page and auto-fills a Google Form for every listing

</details>

---

<details>
<summary><strong>🟢 Flask Web Development — Routing, Templates, Jinja2</strong></summary>

<br>

### Flask Fundamentals & Decorators
**What I Learnt:** `Flask(__name__)`, `@app.route()`, `__name__`/`__main__`, first-class functions, Python decorators, `*args`/`**kwargs` in decorators, Flask Debugger

**What I Built:**
- 🌐 [Flask Hello World Server](FlaskFundamentals/hello.py) — Minimal Flask server with a single `@app.route` returning HTML
- 🔢 [Advanced Decorator Exercise](FlaskFundamentals/decorator.py) — Authentication-style wrapper using `*args`/`**kwargs`
- 🎮 [Higher-Lower URL Game](higher-lower-flask-game/) — Flask game where the player guesses a number by navigating URL paths, with GIF responses

---

### HTML Templates & Static Files
**What I Learnt:** `render_template()`, Flask `templates/` and `static/` folder conventions, wiring pre-built HTML/CSS templates to a Flask backend

**What I Built:**
- 🏠 [Personal Birthday Invitation Site](my-personal-site/) — Flask-served invitation page with custom CSS and embedded images
- 💼 [Name Card Website](Name-Card-Website/) — Professional name card portfolio from an HTML template, served via Flask with full static assets

---

### Jinja2 Templating & Capstone
**What I Learnt:** Jinja2 `{{ variable }}`, `{% for %}` / `{% if %}` blocks, multiline statements, `url_for()`, injecting live API data into templates

**What I Built:**
- 🧪 [Jinja Fundamentals App](jinja-fundamentals/) — Multi-route Flask app with dynamic templates, genderize.io/agify.io API integration, and blog listing
- 📝 [Blog Capstone](blog-page/) — Flask blog app fetching posts from a JSON API and rendering home + individual post pages with Jinja2

</details>

---

## 💡 Key Takeaways

- **Projects > Theory** — building real things accelerates learning exponentially
- **Debugging is a skill** — not a sign of failure, but part of the craft
- **OOP changes everything** — structuring code with classes makes complex projects manageable
- **APIs unlock superpowers** — connecting to external services opens up endless possibilities
- **Automation is practical** — Selenium bots taught me to think about UI as a programmable interface

---

> *A curated collection of Python projects from my learning journey — built to solve real problems and reinforce practical skills.* ✌️
