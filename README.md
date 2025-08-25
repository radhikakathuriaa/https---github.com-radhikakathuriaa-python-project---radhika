
#  Movie Suggestion Bot (with IMDb Scraper)

This project has two parts:

1. Scraper → Uses Selenium to scrape movies by genre from IMDb and saves them into an Excel file.  
2. Movie Bot → Loads the dataset and suggests random movies interactively.  

---

## Features
- Scrape movies from IMDb (Title, Year, Genre, Rating).  
- Export dataset to `genre_movies_selenium.xlsx`.  
- Ask the user for a genre and suggest a random movie.
- - Predefined supported genres:
  ```python
  GENRES = ['action', 'comedy', 'drama', 'romance', 'horror']
- Lightweight and extendable.  

---

## Technologies Used
- **Python 3.x**  
- **selenium** (web scraping)  
- **pandas** (data handling)  
- **openpyxl** (Excel support)  
- **random** (movie selection)  

---

## 📂 Project Structure
```
movie-bot/
│── ScrapeMovie.py.py          # Scrapes IMDb movies by genre
│── Moviebot.py.py             # Suggests random movies from dataset
│── genre_movies_selenium.xlsx # Auto-generated dataset after scraping
│── README.md                  # Documentation
```

---

## How to Run

### 1. Install Dependencies
```bash
pip install pandas openpyxl selenium
```

You will also need **ChromeDriver** installed and matching your Chrome browser version.  
Update the path in `ScrapeMovie.py.py`:
```python
service = Service(executable_path=r"C:\Users\YourName\chromedriver.exe")
```

---

### 2. Scrape Movies
Run the scraper to collect movies:
```bash
python ScrapeMovie.py.py
```

This will create an Excel file:
```
genre_movies_selenium.xlsx
```

---

### 3. Run the Movie Bot
After scraping, run the movie suggestion bot:
```bash
python Moviebot.py.py
```

Example:
```
👉 Enter a genre (or type 'exit' to quit): action
🎬 Suggested Movie: Mad Max: Fury Road (2015) ⭐ 8.1
```

---
**
Example Dataset (Excel)**

| Genre   | Title                    | Year | Rating |
| ------- | ------------------------ | ---- | ------ |
| action  | Mad Max: Fury Road       | 2015 | 8.1    |
| comedy  | The Mask                 | 1994 | 6.9    |
| drama   | The Shawshank Redemption | 1994 | 9.3    |
| romance | Titanic                  | 1997 | 7.8    |
| horror  | The Conjuring            | 2013 | 7.5    |

---

## Future Enhancements
- Add more genres dynamically.  
- Scrape multiple pages for larger datasets.  




