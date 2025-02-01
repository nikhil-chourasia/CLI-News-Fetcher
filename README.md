# News Fetcher using Python & NewsAPI 📰

## Overview

This is a simple **News Fetcher script** built with Python using the **NewsAPI**. It allows users to fetch real-time news headlines based on **country, category, or specific sources**. The program interacts with the NewsAPI and displays the latest headlines in a structured format.

## Features ✨

- Fetches real-time news articles 📢
- Filter news by **country**, **category**, or **keyword** 🌍🔍
- Retrieve articles from specific sources 📰
- Handles missing data gracefully (No KeyErrors!) ✅
- Provides clean and structured output 🎯

## Prerequisites 📦

Make sure you have the following installed before running the script:

- Python 3.x
- `requests` module (Install using `pip install requests`)
- A **NewsAPI API Key** (Get it from [NewsAPI.org](https://newsapi.org/))

## Installation & Usage 🛠️

1. Clone this repository:

   ```
   git clone https://github.com/nikhil-chourasia/CLI-News-Fetcher.git
   ```

2. Install dependencies:

   ```
   pip install requests
   ```

3. Add your **NewsAPI API Key** inside the script:

   ```
   apiKey = 'YOUR_NEWSAPI_KEY'
   ```

4. Run the script:

   ```
   python main.py
   ```

5. Follow the prompts to select **Country (c)** or **Source (s)** and get the latest news! 🎉

## Example Output 📜

```
Hello User! You want to watch news in which format, Country(c) or Sources(s)?: c
Enter country code for news: us
Enter category of news (Press enter to skip): technology
Enter a Keyword you want to search for (Press enter to skip): AI

Title: AI Breakthroughs in 2024
Author: John Doe
Source: TechNews Daily
Published at: 2024-02-01T10:00:00Z
Description: Major advancements in AI are set to change the world this year...
URL: https://technews.com/ai-breakthroughs-2024
--------------------------------------------------------------------------------
```

## Future Improvements 🚀

- ✅ Build a **GUI version** using Tkinter or PyQt
- ✅ Integrate a **Telegram bot** for instant news updates
- ✅ Add a **web-based UI** using Flask or FastAPI

## License 📜

This project is open-source under the **MIT License**. Feel free to use and modify it!

---

👨‍💻 **Author:** [Nikhil Chourasia](https://github.com/nikhil-chourasia/)\
🌟 **If you found this useful, give it a ⭐ on GitHub!**

