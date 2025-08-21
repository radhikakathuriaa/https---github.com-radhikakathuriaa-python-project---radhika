from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


def create_driver():
    chrome_options = Options()
    # chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )

    service = Service(executable_path=r"C:\Users\rkathuri\Desktop\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


GENRES = ['action', 'comedy', 'drama', 'romance', 'horror']

PAGES = 2   # test with 1 page first


def scrape_genre(driver, genre, pages=1):
    movies = []

    for page in range(pages):
        start = page * 50 + 1
        url = f"https://www.imdb.com/search/title/?genres={genre}&start={start}"
        print(f"\n➡️ Visiting: {url}")

        try:
            driver.get(url)
        except Exception as e:
            print(f"❌ Failed to load page: {e}")
            continue

        time.sleep(3)  # wait for page to render

        movie_cards = driver.find_elements(By.CSS_SELECTOR, ".ipc-metadata-list-summary-item")
        print(f"🔍 Found {len(movie_cards)} movie cards on page {page + 1}")

        for card in movie_cards:
            try:
                 # Title → <a> with href containing "/title/"
                try:
                    title = card.find_element(By.CSS_SELECTOR, "a h3").text
                except:
                    title = None
                # Year (first inline-list item usually has the release year)
                try:
                    year = card.find_element(By.CSS_SELECTOR, "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > span:nth-child(1)").text
                except:   
                    year = None

                # Rating (IMDb rating if present)
                try:
                    rating = card.find_element(By.CSS_SELECTOR, "span[class*='rating']").text
                except:
                    rating = None

                movies.append({
                    "Genre": genre,
                    "Title": title,
                    "Year": year,
                    "Rating": rating
                })
            except Exception as e:
                print(f"⚠️ Error parsing movie card: {e}")

    return movies


def main():
    driver = create_driver()
    all_movies = []

    try:
        for genre in GENRES:
            print(f"\n📽️ Scraping genre: {genre}")
            genre_movies = scrape_genre(driver, genre, pages=PAGES)
            all_movies.extend(genre_movies)
            time.sleep(1)
    finally:
        driver.quit()

    if all_movies:
        df = pd.DataFrame(all_movies)
        df.to_excel("genre_movies_selenium.xlsx", index=False)
        print("✅ Data exported to genre_movies_selenium.xlsx")
    else:
        print("⚠️ No movies scraped.")


if __name__ == "__main__":
    main()
