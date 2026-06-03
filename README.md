# 🐍 100 Days of Python — Angela Yu's Bootcamp

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Course](https://img.shields.io/badge/Udemy-100%20Days%20of%20Code-EC5252?logo=udemy&logoColor=white)](https://www.udemy.com/course/100-days-of-code/)
[![Progress](https://img.shields.io/badge/Progress-Day%2044%2F100-green)]()

This repository documents my journey through Dr. Angela Yu's **"100 Days of Code: The Complete Python Pro Bootcamp"** on Udemy. Each day includes new concepts, exercises, and a project that reinforces learning through hands-on coding.

---

## 📖 Table of Contents

| Section | Days | Focus |
|---------|------|-------|
| [Beginner Python](#-section-1--beginner-python-days-114) | 1 – 14 | Variables, Control Flow, Functions, Loops, Beginner Projects |
| [Intermediate Python & GUI](#-section-2--intermediate-python--gui-days-1531) | 15 – 31 | OOP, Turtle Graphics, Tkinter GUI, Files, Pandas, APIs |
| [Intermediate+ Python & APIs](#-section-3--intermediate-python--apis-days-3240) | 32 – 40 | Email Automation, REST APIs, Authentication, Capstone Projects |
| [Web Foundations](#-section-4--web-foundations-days-41-44) | 41 – 44 | HTML, Intermediate HTML, CSS Foundations & Intermediate CSS |

---

## 🟢 Section 1 — Beginner Python (Days 1–14)

---

### 📅 Day 1 — Working with Variables

**What I Learnt:**
- Printing output using `print()`
- String concatenation and manipulation
- Variables and naming conventions
- The `input()` function for user interaction
- Debugging basic syntax errors

**What I Built:**
- 🎸 [Band Name Generator](brandNameGenerator.py) — Generates a fun band name by combining user's city and pet name

---

### 📅 Day 2 — Data Types & String Manipulation

**What I Learnt:**
- Data types: Strings, Integers, Floats, Booleans
- Type conversion / type casting (`int()`, `float()`, `str()`)
- Mathematical operations in Python
- F-strings for formatted output
- The `round()` function

**What I Built:**
- 💰 [Tip Calculator](TipCalculator.py) — Splits a restaurant bill among friends with a custom tip percentage

---

### 📅 Day 3 — Control Flow & Logical Operators

**What I Learnt:**
- Conditional statements: `if`, `elif`, `else`
- Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
- Logical operators: `and`, `or`, `not`
- Nested `if` statements
- Multiple `if` vs `if/elif/else` differences

**What I Built:**
- 🏝️ [Treasure Island Game](TreasureIslandGame.py) — A text-based choose-your-own-adventure game with ASCII art
- 💕 [Love Calculator](loveCalculator.py) — Calculates a "love score" based on how many letters of the names match with "TRUE" and "LOVE"

---

### 📅 Day 4 — Randomisation & Python Lists

**What I Learnt:**
- The `random` module (`randint()`, `choice()`, `choices()`)
- Python Lists: creating, indexing, and modifying
- Nested lists
- Index errors and how to avoid them

**What I Built:**
- ✊✋✌️ [Rock Paper Scissors](rockPaperScissor.py) — Classic game against the computer with ASCII art visuals

---

### 📅 Day 5 — Python Loops

**What I Learnt:**
- `for` loops and iterating over lists/ranges
- The `range()` function
- `while` loops
- Loop control flow
- Using loops for accumulation patterns

**What I Built:**
- 🔐 [Password Generator](passwordGenerator.py) — Generates strong random passwords with customizable letters, symbols, and numbers count

---

### 📅 Day 6 — Python Functions & Karel

**What I Learnt:**
- Defining and calling functions
- Indentation and code blocks
- The concept of reusable code
- Solving problems with functions (Karel robot exercises)
- While loops in the context of functions

**What I Built:**
- 🤖 Karel Robot challenges (Reeborg's World — web-based, no local file)

---

### 📅 Day 7 — Hangman Project

**What I Learnt:**
- Flow charts for planning program logic
- Using `for` loops with strings
- Working with multiple Python files/modules
- Using `import` to organize code
- ASCII art for visual feedback
- Tracking game state with lists

**What I Built:**
- 🪓 [Hangman Game](Hangman%20game/) — Full Hangman game with word list, ASCII art stages, and lives tracking (`main.py`, `hangman_art.py`, `hangman_words.py`)

---

### 📅 Day 8 — Function Parameters & Caesar Cipher

**What I Learnt:**
- Functions with parameters (positional & keyword arguments)
- The difference between parameters and arguments
- Multiple return values
- Caesar Cipher encryption/decryption logic

**What I Built:**
- 🔒 [Caesar Cipher](Caeser%20Cipher/) — Encrypt and decrypt messages using the classic Caesar Cipher shift algorithm with ASCII art logo (`main.py`, `art.py`)

---

### 📅 Day 9 — Dictionaries & Nesting

**What I Learnt:**
- Python Dictionaries: creating, accessing, and modifying
- Nesting: lists in dictionaries, dictionaries in lists, dictionaries in dictionaries
- Iterating over dictionaries
- Using dictionaries to store structured data

**What I Built:**
- 🔨 [Secret Auction](Secret%20Auction/) — A blind auction program where multiple users can bid secretly, and the highest bidder wins (`main.py`, `art.py`)

---

### 📅 Day 10 — Functions with Outputs (Return Values)

**What I Learnt:**
- Functions with return values
- The `return` keyword and multiple return statements
- Docstrings for documenting functions
- Combining dictionaries, lists, and functions
- Recursion basics

**What I Built:**
- 🧮 [Simple Calculator](Simple%20Calculator/) — A fully functional calculator that supports chaining operations and restarting calculations (`main.py`, `art.py`)

---

### 📅 Day 11 — Blackjack Capstone Project

**What I Learnt:**
- Applying all concepts from Days 1–10 in a capstone project
- Complex program flow with multiple functions
- Game state management
- Procedural programming best practices
- Planning before coding (pseudocode / flowcharts)

**What I Built:**
- 🃏 [Blackjack Game](Blackjack%20Game/) — A complete Blackjack (21) card game against the computer with proper game rules, ace handling, and ASCII art (`main.py`, `art.py`)

---

### 📅 Day 12 — Scope & Namespacing

**What I Learnt:**
- Local vs. Global scope
- Namespaces in Python
- The `global` keyword (and why to avoid it)
- Block scope (Python doesn't have it unlike other languages)
- Constants and naming conventions (e.g., `UPPER_CASE`)

**What I Built:**
- 🔢 [Number Guessing Game](Number%20Gussing%20Game/) — Guess the number between 1–100 with Easy (10 attempts) and Hard (5 attempts) difficulty modes (`main.py`, `art.py`)

---

### 📅 Day 13 — Debugging

**What I Learnt:**
- Common types of bugs: syntax, runtime, logical
- Debugging techniques: `print()` statements, using a debugger
- Reading error messages and tracebacks
- Reproducing bugs systematically
- Using breakpoints

**What I Built:**
- 🐛 Debugging exercises (practice-based, no standalone project)

---

### 📅 Day 14 — Higher Lower Game Project

**What I Learnt:**
- Applying all beginner Python concepts in a complete project
- Comparing data from a dataset
- Game loop logic with score tracking
- Working with external data files
- Creating engaging CLI experiences

**What I Built:**
- 📊 [Higher Lower Game](Higher%20Lower%20game/) — Compare follower counts of celebrities/brands and guess who has more. Features game data, score tracking, and ASCII art (`main.py`, `art.py`, `game_data.py`)

---

## 🟡 Section 2 — Intermediate Python & GUI (Days 15–31)

---

### 📅 Day 15 — Local Dev Environment Setup & Coffee Machine

**What I Learnt:**
- Setting up a local development environment (PyCharm / VS Code)
- Running Python scripts locally instead of online IDEs
- Working with complex dictionaries and nested data
- Modelling real-world processes in code
- Handling user input with validation

**What I Built:**
- ☕ [Coffee Machine (Procedural)](CoffeeMachine.py) — A virtual coffee machine that manages resources, processes coin payments, and serves espresso/latte/cappuccino

---

### 📅 Day 16 — Object-Oriented Programming (OOP)

**What I Learnt:**
- Introduction to OOP: classes and objects
- Attributes and methods
- Constructors with `__init__()`
- The `self` keyword
- Refactoring procedural code to OOP
- Using external modules/classes

**What I Built:**
- ☕ [Coffee Machine (OOP Version)](Coffee%20Machine%20(OOPs)/) — Refactored the Day 15 Coffee Machine using OOP principles with separate classes: `CoffeeMaker`, `MoneyMachine`, `Menu` (`main.py`, `coffee_maker.py`, `menu.py`, `money_machine.py`)

---

### 📅 Day 17 — The Quiz Project & Benefits of OOP

**What I Learnt:**
- Creating classes from scratch
- Class attributes vs. instance attributes
- Designing with OOP: separating data, models, and logic
- Working with True/False question banks
- Understanding the benefits of OOP (modularity, reusability)

**What I Built:**
- ❓ [Quiz Game (OOP)](Quiz%20Game(OOPs)/) — A True/False quiz game built with OOP — separate classes for Question model, QuizBrain logic, and data (`main.py`, `question_model.py`, `quiz_brain.py`, `data.py`)

---

### 📅 Day 18 — Turtle Graphics & GUI

**What I Learnt:**
- The `turtle` module for graphics
- Drawing shapes, lines, and patterns
- RGB colors and `colormode(255)`
- Importing and using external packages
- Creating artistic patterns programmatically

**What I Built:**
- 🐢 [Random Walk](RandomWalk/) — A turtle graphics program that draws random colorful paths (`randomwalk.py`, `shapes.py`)
- 🌀 [Spirograph](spirograph.py) — Draws beautiful spirograph patterns using turtle graphics with random colors
- 🎨 [Spot Painting](spotpainting/) — Recreates a Damien Hirst-style spot painting using turtle graphics and extracted color palette (`spot.py`)

---

### 📅 Day 19 — Instances, State & Higher-Order Functions

**What I Learnt:**
- Event listeners in turtle graphics
- Higher-order functions (passing functions as arguments)
- Object state and tracking changes
- Turtle screen events: `onkey()`, `listen()`
- Coordinate system in turtle graphics

**What I Built:**
- 🐢 [Turtle Race](TurtleRace/) — A colorful turtle racing game where users bet on which turtle wins, using event listeners and random movement (`turtleRace.py`, `eventListeners.py`)

---

### 📅 Day 20 — Snake Game Part 1

**What I Learnt:**
- Animation with screen refresh using `tracer()` and `update()`
- Coordinate-based movement on screen
- Controlling objects with keyboard input
- Creating a snake body using multiple turtle segments
- Screen setup and configuration

**What I Built:**
- 🐍 [Snake Game V1](SnakeGame/) — Part 1 of the classic Snake game with smooth movement, keyboard controls, food spawning, and collision detection (`main.py`, `snake.py`, `food.py`, `scoreboard.py`)

---

### 📅 Day 21 — Snake Game Part 2 (Inheritance & List Slicing)

**What I Learnt:**
- Class inheritance in Python
- List slicing techniques
- Detecting collisions (wall & tail collisions)
- Extending the snake when eating food
- Score tracking and game over logic

**What I Built:**
- 🐍 [Snake Game V2](SnakeGame%20V0.2/) — Complete Snake game with inheritance-based scoreboard, high score tracking saved to file, tail collision detection, and polished gameplay (`main.py`, `snake.py`, `food.py`, `scoreboard.py`, `data.txt`)

---

### 📅 Day 22 — Pong: The Famous Arcade Game

**What I Learnt:**
- Building a full game with multiple classes
- Paddle and ball physics (movement, bouncing)
- Collision detection with walls and paddles
- Scoring system for two players
- Game loop timing and speed control

**What I Built:**
- 🏓 [Pong Game](Pong/) — Classic 2-player Pong arcade game with paddles, ball physics, wall/paddle collisions, and a scoreboard (`main.py`, `paddle.py`, `ball.py`, `scoreboard.py`)

---

### 📅 Day 23 — Turtle Crossing Capstone Project

**What I Learnt:**
- Applying OOP to build a multi-class game from scratch
- Managing multiple moving objects on screen
- Increasing game difficulty over time
- End-to-end game development lifecycle
- Capstone-level problem solving

**What I Built:**
- 🚗 [Turtle Crossing Game](turtle-crossing/) — A Frogger-style game where a turtle must cross a busy road, with increasing difficulty levels (`main.py`, `player.py`, `car_manager.py`, `scoreboard.py`)

---

### 📅 Day 24 — Files, Directories & Paths

**What I Learnt:**
- Reading and writing files with `open()`
- File modes: `"r"`, `"w"`, `"a"`
- Absolute vs. relative file paths
- Using `with` statement for safe file handling
- The `readlines()` and `writelines()` methods

**What I Built:**
- ✉️ [Mail Merge](MailMerge/) — Automatically generates personalized letters by replacing placeholder names from a template with names from a list (`main.py`, `Input/`, `Output/`)

---

### 📅 Day 25 — CSV Data & the Pandas Library

**What I Learnt:**
- Working with CSV files
- Introduction to the Pandas library
- DataFrames and Series
- Reading CSVs with `pandas.read_csv()`
- Filtering, iterating, and creating DataFrames
- Exporting data to CSV

**What I Built:**
- 🐿️ [NYC Squirrel Census Analysis](NYC_Squirrel_Census_2018/) — Analyzes the 2018 Central Park Squirrel Census data to count squirrels by fur color using Pandas (`main.py`, CSV data)
- 🗺️ [U.S. States Game](us_states_game/) — An interactive quiz where you name all 50 U.S. states on a map, with Pandas tracking correct answers and exporting states to learn (`main.py`, `50_states.csv`, `blank_states_img.gif`)

---

### 📅 Day 26 — List Comprehensions & NATO Alphabet

**What I Learnt:**
- List comprehension syntax and patterns
- Dictionary comprehension
- Iterating over Pandas DataFrames with comprehensions
- Filtering with conditional list comprehensions
- Writing concise Pythonic code

**What I Built:**
- 🔤 [NATO Alphabet Converter](NATO-alphabet/) — Converts any word into its NATO phonetic alphabet equivalent using dictionary comprehension and Pandas (`main.py`, `nato_phonetic_alphabet.csv`)

---

### 📅 Day 27 — Tkinter, *args, **kwargs & GUI Programs

**What I Learnt:**
- Introduction to `tkinter` for building desktop GUIs
- `*args` (unlimited positional arguments) and `**kwargs` (unlimited keyword arguments)
- Creating windows, labels, buttons, entries, and layouts
- The `grid()` and `pack()` layout managers
- Event-driven programming with buttons and callbacks

**What I Built:**
- 🖥️ [Intro to Tkinter](intro_to_tkinter/) — Tkinter GUI experiments and widget demos (`main.py`)
- 📏 [Miles to KM Converter](miles_to_km_converter/) — A GUI app that converts miles to kilometers using Tkinter (`main.py`)

---

### 📅 Day 28 — Tkinter Dynamic Typing & Pomodoro App

**What I Learnt:**
- Tkinter `Canvas` widget for drawing and images
- `after()` method for timed events
- Dynamic typing in Python
- Building countdown timers
- Managing UI state with global variables
- Color constants and UI theming

**What I Built:**
- 🍅 [Pomodoro App](pomodoro-app/) — A full Pomodoro timer GUI with work/break cycles, countdown display, tomato image, and check marks for completed sessions (`main.py`, `tomato.png`)

---

### 📅 Day 29 — Building a Password Manager with Tkinter

**What I Learnt:**
- Multi-widget Tkinter layouts with `grid()`
- Reading/writing data to files
- The `pyperclip` module for clipboard functionality
- `messagebox` for dialog pop-ups
- Generating and storing secure passwords
- UI/UX design for forms

**What I Built:**
- 🔑 [Password Manager](password_manager/) — A GUI password manager that generates strong passwords, saves credentials to a JSON file, and copies passwords to clipboard (`main.py`, `logo.png`, `data.json`)

---

### 📅 Day 30 — Errors, Exceptions & JSON Data

**What I Learnt:**
- `try`, `except`, `else`, `finally` blocks
- Handling specific exceptions (`FileNotFoundError`, `KeyError`, etc.)
- Raising custom exceptions with `raise`
- Reading and writing JSON data (`json.load()`, `json.dump()`, `json.update()`)
- Updating and searching JSON files

**What I Built:**
- 🔑 [Password Manager v2](password_manager/) — Enhanced the Password Manager with JSON storage, search functionality, and robust error handling (`main.py`, `data.json`)

---

### 📅 Day 31 — Flash Card Capstone Project

**What I Learnt:**
- Tkinter `Canvas` for complex layouts with images and text
- Working with Pandas to load and filter CSV data
- Timers and delayed function execution with `after()`
- Saving learning progress to file
- Building a complete study tool end-to-end

**What I Built:**
- 🃏 [Flash Card App](flash-card-project/) — A French-to-English flashcard learning app with card flip animation, progress tracking, and words-to-learn filtering (`main.py`, `data/french_words.csv`, card images)

---

## 🟠 Section 3 — Intermediate+ Python & APIs (Days 32–40)

---

### 📅 Day 32 — Send Email (smtplib) & Manage Dates (datetime)

**What I Learnt:**
- Sending emails with Python using `smtplib`
- SMTP protocol and email server configuration
- The `datetime` module: date, time, and weekday
- Automating actions based on date and time
- Reading from text files for email content

**What I Built:**
- 📧 [Monday Motivation Quotes](monday_quotes/) — Sends a random motivational quote via email every Monday using `smtplib` and `datetime` (`main.py`, `quotes.txt`)
- 🎂 [Birthday Wisher](birthday-wisher/) — Automatically sends personalized birthday emails by checking a CSV of birthdays against today's date (`main.py`, `birthdays.csv`, `letter_templates/`)

---

### 📅 Day 33 — API Endpoints & API Parameters

**What I Learnt:**
- What is an API and how it works
- Making HTTP requests with the `requests` library
- API endpoints, parameters, and response codes
- Parsing JSON API responses
- Working with the ISS (International Space Station) API and Sunrise/Sunset API

**What I Built:**
- 🛰️ [ISS Overhead Notifier](ISS_overhead_notifier/) — Tracks the ISS position in real time and sends an email notification when it's overhead during nighttime (`main.py`)
- 🌅 [Kanye Quotes App](kanye_quotes/) — A Tkinter GUI that fetches random Kanye West quotes from an API and displays them on a stylish card (`main.py`, `kanye.png`, `background.png`)

---

### 📅 Day 34 — API Practice: GUI Quiz App

**What I Learnt:**
- Fetching data from the Open Trivia Database API
- Unescaping HTML entities in API responses
- Building a quiz UI with Tkinter
- Connecting API data to a GUI application
- Real-time score tracking and visual feedback (green/red flashes)

**What I Built:**
- 🧠 [Quizzler App](quizzler-app/) — A GUI-based True/False quiz app that pulls questions from the Open Trivia API, with score tracking and color-coded feedback (`main.py`, `ui.py`, `quiz_brain.py`, `question_model.py`, `data.py`)

---

### 📅 Day 35 — Keys, Authentication & Environment Variables

**What I Learnt:**
- API authentication with API keys
- Environment variables for securing sensitive data
- The `.env` file and `python-dotenv`
- Working with weather APIs (OpenWeatherMap)
- Sending SMS notifications via Twilio API

**What I Built:**
- 🌧️ [Rain Alert](rain_alert/) — Checks the weather forecast using the OpenWeatherMap API and sends an SMS alert via Twilio if rain is expected (`main.py`)

---

### 📅 Day 36 — Stock Trading News Alert

**What I Learnt:**
- Chaining multiple APIs together in one project
- Stock price monitoring with the Alpha Vantage API
- Fetching news articles with the News API
- Percentage change calculations
- Conditional SMS notifications based on market movement

**What I Built:**
- 📈 [Stock News Notifier](stock-news-notifier/) — Monitors stock price changes and sends SMS alerts with relevant news articles when the price moves significantly (`main.py`)

---

### 📅 Day 37 — Habit Tracking with Pixela API

**What I Learnt:**
- Advanced API usage: POST, PUT, DELETE HTTP methods
- API authentication with custom headers
- Creating and managing user accounts via API
- Graph creation and data visualization through APIs
- Working with the Pixela API for habit tracking

**What I Built:**
- 📊 [Habit Tracker](habit-tracker/) — A habit tracking app that creates a Pixela graph and logs daily progress using POST/PUT/DELETE API calls with custom authentication headers (`main.py`)

---

### 📅 Day 38 — Workout Tracking with Google Sheets

**What I Learnt:**
- Natural Language Processing for exercise input (Nutritionix API)
- Automatic logging to Google Sheets via the Sheety API
- Working with date and time formatting
- Environment variables and Bearer Token authentication
- Connecting multiple APIs in a pipeline

**What I Built:**
- 🏋️ [Exercise Tracker](exercise_tracker/) — Logs workouts using natural language input (e.g., "ran 5km and cycled 30 minutes"), processes them through the Nutritionix API, and records calories/duration to Google Sheets via Sheety (`main.py`)

---

### 📅 Day 39 — Flight Deal Finder (Part 1)

**What I Learnt:**
- Searching for cheap flights using the Amadeus/Tequila API
- Structuring a large multi-file project
- The data manager pattern for spreadsheet interaction
- Flight search logic with origin/destination and date ranges
- Object-oriented data modelling for flight results

**What I Built:**
- ✈️ [Flight Deals — Part 1](flight-deals/) — Searches for the cheapest flights from your city to destinations stored in a Google Sheet, using the Tequila Flight Search API (`main.py`, `flight_search.py`, `data_manager.py`, `flight_data.py`, `notification_manager.py`)

---

### 📅 Day 40 — Flight Deal Finder (Part 2)

**What I Learnt:**
- Adding customer sign-up and email notifications
- Multi-city and stopover flight search logic
- Sending formatted email alerts with flight details
- Error handling for API failures
- Building a complete end-to-end automated system

**What I Built:**
- ✈️ [Flight Deals — Complete](flight-deals/) — Extended the Flight Deal Finder with email/SMS notifications, customer management, and multi-city search with stopovers (`notification_manager.py`, `main.py`, `requirements.txt`)

---

## 🔵 Section 4 — Web Foundations (Days 41–44)

---

### 📅 Day 41 — HTML Foundations

**What I Learnt:**
- Introduction to HTML (HyperText Markup Language)
- HTML document structure: `<!DOCTYPE>`, `<html>`, `<head>`, `<body>`
- Heading tags (`<h1>` to `<h6>`) and paragraph tags (`<p>`)
- Self-closing tags like `<br>` and `<hr>`
- Creating ordered and unordered lists (`<ol>`, `<ul>`, `<li>`)

**What I Built:**
- 🎬 [Movie Ranking Page](web-foundations/HTML%20Projects/movie_ranking/) — An HTML page ranking top movies using heading and list elements (`index.html`)
- 🍳 [Recipe Page](web-foundations/HTML%20Projects/recipe_using_lists/) — A recipe page using nested HTML lists for ingredients and instructions (`index.html`)

---

### 📅 Day 42 — Intermediate HTML

**What I Learnt:**
- Nesting lists within lists
- The `<img>` element and `src`/`alt` attributes
- Anchor tags `<a>` and the `href` attribute for hyperlinks
- Image elements with sizing
- Building multi-page websites with links

**What I Built:**
- 📋 [Nested List Page](web-foundations/HTML%20Projects/Nested%20list/) — An HTML page demonstrating complex nested list structures (`index.html`)
- 🖼️ [Image Element Page](web-foundations/HTML%20Projects/Image%20Element/) — Practicing embedding images in HTML (`index.html`)
- 🔗 [Anchor Tags Page](web-foundations/HTML%20Projects/Anchor%20Tags/) — Practicing creating hyperlinks and navigation with anchor tags (`index.html`)

---

### 📅 Day 43 — Introduction to CSS

**What I Learnt:**
- How to add CSS to HTML (Inline, Internal, and External CSS)
- CSS Selectors (Tag, Class, and ID selectors) and their specificity rules
- Customizing colors, fonts, backgrounds, and layout aesthetics
- Structuring files with external stylesheets

**What I Built:**
- 🎨 [Adding CSS](web-foundations/CSS%20Projects/Adding%20CSS/) — Exercises demonstrating inline, internal, and external CSS methods (`index.html`, `inline.html`, `internal.html`, `external.html`, `style.css`)
- 🎯 [CSS Selectors](web-foundations/CSS%20Projects/CSS%20Selectors/5.3%20CSS%20Selectors/) — Practicing class, ID, and element selectors (`index.html`, `style.css`)
- 🔠 [Color Vocab Project](web-foundations/CSS%20Projects/Color%20Vocab%20Project/5.4%20Color%20Vocab%20Project/) — Staged CSS exercise displaying color vocab grid with styled fonts and layouts (`index.html`, `style.css`)

---

### 📅 Day 44 — Intermediate CSS

**What I Learnt:**
- CSS Colors (Hex codes, RGB, HSL, and color naming conventions)
- Font Properties (Font family, size, weight, line height, and style)
- Inspecting CSS (using browser developer tools to inspect and debug styles)
- The CSS Box Model (Understanding margins, padding, borders, and content sizing)

**What I Built:**
- 🎨 [CSS Colors](web-foundations/CSS%20Projects/CSS%20Colors/) — Exercises on utilizing different color formats and transparency in CSS (`index.html`)
- 🔠 [Font Properties](web-foundations/CSS%20Projects/Font%20Properties/) — Practice styling fonts, sizes, and formatting text layouts (`index.html`, `font-family.html`, `font-size.html`)
- 📦 [CSS Box Model](web-foundations/CSS%20Projects/CSS%20Box%20Model/) — Layout exercise to understand padding, margins, borders, and box dimensions (`index.html`)
- 🖼️ [CSS Poster Project](web-foundations/CSS%20Projects/CSS%20Poster%20Project/) — A web page displaying a poster with styled fonts, margins, and borders around a custom image (`index.html`, `style.css`)

---

## 🛠️ Tools & Technologies Used

| Category | Tools |
|----------|-------|
| **Language** | Python 3 |
| **IDE** | PyCharm, VS Code |
| **GUI** | Tkinter, Turtle Graphics |
| **Data** | Pandas, CSV, JSON |
| **APIs** | OpenWeatherMap, Twilio, Pixela, Nutritionix, Sheety, Tequila/Amadeus, Open Trivia DB, ISS API, Kanye REST |
| **Email** | smtplib, SMTP |
| **Web** | HTML, CSS |
| **Version Control** | Git & GitHub |

---

## 📂 Repository Structure

```
100_Days_Of_Python/
├── brandNameGenerator.py          # Day 1
├── TipCalculator.py               # Day 2
├── TreasureIslandGame.py          # Day 3
├── loveCalculator.py              # Day 3
├── rockPaperScissor.py            # Day 4
├── passwordGenerator.py           # Day 5
├── Hangman game/                  # Day 7
├── Caeser Cipher/                 # Day 8
├── Secret Auction/                # Day 9
├── Simple Calculator/             # Day 10
├── Blackjack Game/                # Day 11
├── Number Gussing Game/           # Day 12
├── Higher Lower game/             # Day 14
├── CoffeeMachine.py               # Day 15
├── Coffee Machine (OOPs)/         # Day 16
├── Quiz Game(OOPs)/               # Day 17
├── RandomWalk/                    # Day 18
├── spirograph.py                  # Day 18
├── spotpainting/                  # Day 18
├── TurtleRace/                    # Day 19
├── SnakeGame/                     # Day 20
├── SnakeGame V0.2/                # Day 21
├── Pong/                          # Day 22
├── turtle-crossing/               # Day 23
├── MailMerge/                     # Day 24
├── NYC_Squirrel_Census_2018/      # Day 25
├── us_states_game/                # Day 25
├── NATO-alphabet/                 # Day 26
├── intro_to_tkinter/              # Day 27
├── miles_to_km_converter/         # Day 27
├── pomodoro-app/                  # Day 28
├── password_manager/              # Day 29–30
├── flash-card-project/            # Day 31
├── monday_quotes/                 # Day 32
├── birthday-wisher/               # Day 32
├── ISS_overhead_notifier/         # Day 33
├── kanye_quotes/                  # Day 33
├── quizzler-app/                  # Day 34
├── rain_alert/                    # Day 35
├── stock-news-notifier/           # Day 36
├── habit-tracker/                 # Day 37
├── exercise_tracker/              # Day 38
├── flight-deals/                  # Day 39–40
└── web-foundations/               # Day 41–44
    ├── HTML Projects/              # Days 41–42
    │   ├── movie_ranking/
    │   ├── recipe_using_lists/
    │   ├── Nested list/
    │   ├── Image Element/
    │   └── Anchor Tags/
    └── CSS Projects/               # Days 43–44
        ├── Adding CSS/
        ├── CSS Selectors/
        ├── Color Vocab Project/
        ├── CSS Colors/
        ├── Font Properties/
        ├── CSS Box Model/
        └── CSS Poster Project/
```

---

## 📈 Progress Tracker

| Day | Status | Topic |
|-----|--------|-------|
| 1 | ✅ | Variables |
| 2 | ✅ | Data Types & Strings |
| 3 | ✅ | Control Flow |
| 4 | ✅ | Randomisation & Lists |
| 5 | ✅ | Loops |
| 6 | ✅ | Functions & Karel |
| 7 | ✅ | Hangman |
| 8 | ✅ | Caesar Cipher |
| 9 | ✅ | Dictionaries & Nesting |
| 10 | ✅ | Calculator |
| 11 | ✅ | Blackjack Capstone |
| 12 | ✅ | Scope & Number Guessing |
| 13 | ✅ | Debugging |
| 14 | ✅ | Higher Lower Game |
| 15 | ✅ | Coffee Machine |
| 16 | ✅ | OOP |
| 17 | ✅ | Quiz Project |
| 18 | ✅ | Turtle & GUI |
| 19 | ✅ | Instances & State |
| 20 | ✅ | Snake Game Part 1 |
| 21 | ✅ | Snake Game Part 2 |
| 22 | ✅ | Pong |
| 23 | ✅ | Turtle Crossing |
| 24 | ✅ | Files & Paths |
| 25 | ✅ | CSV & Pandas |
| 26 | ✅ | List Comprehensions |
| 27 | ✅ | Tkinter |
| 28 | ✅ | Pomodoro App |
| 29 | ✅ | Password Manager |
| 30 | ✅ | Errors & JSON |
| 31 | ✅ | Flash Card Capstone |
| 32 | ✅ | Email & Dates |
| 33 | ✅ | APIs |
| 34 | ✅ | GUI Quiz App |
| 35 | ✅ | API Keys & Auth |
| 36 | ✅ | Stock News Alert |
| 37 | ✅ | Habit Tracker |
| 38 | ✅ | Workout Tracking |
| 39 | ✅ | Flight Deals Part 1 |
| 40 | ✅ | Flight Deals Part 2 |
| 41 | ✅ | HTML Foundations |
| 42 | ✅ | Intermediate HTML |
| 43 | ✅ | Introduction to CSS |
| 44 | ✅ | Intermediate CSS |
| 45–100 | ⬜ | Coming soon... |

---

## 💡 Key Takeaways

- **Consistency over speed** — showing up every day matters more than finishing fast
- **Projects > Theory** — building real things accelerates learning exponentially
- **Debugging is a skill** — not a sign of failure, but part of the craft
- **OOP changes everything** — structuring code with classes makes complex projects manageable
- **APIs unlock superpowers** — connecting to external services opens up endless possibilities

---

## 🚀 What's Next

- Continue from **Day 45** onwards
- Upcoming topics: Web Scraping with BeautifulSoup, Selenium, Flask Web Development, Databases, Data Science, and more

---

> *This repository is a work in progress. Updated as I progress through the remaining days of the bootcamp.* ✌️
