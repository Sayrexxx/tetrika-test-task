import csv
import requests
from bs4 import BeautifulSoup
import time

WIKI_URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
CSV_FILENAME = "beasts.csv"


def get_all_animals_by_letter():
    url = WIKI_URL
    beast_count = {}

    while url:
        resp = requests.get(url)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        for h3 in soup.select("div.mw-category-group > h3"):
            letter = h3.text.strip().upper()
            ul = h3.find_next_sibling("ul")
            count = len(ul.find_all("li")) if ul else 0
            beast_count[letter] = beast_count.get(letter, 0) + count

        paginator = soup.select_one(
            "div#mw-pages a:-soup-contains('Следующая страница')"
        )
        if not paginator:
            for a in soup.select("div#mw-pages a"):
                if a.text.strip().startswith("Следующая страница"):
                    paginator = a
                    break
        time_url = "https://ru.wikipedia.org"
        url = time_url + paginator["href"] if paginator else None
        if url:
            time.sleep(0.5)

    return beast_count


def write_beasts_csv(beast_count, filename=CSV_FILENAME):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter in sorted(beast_count):
            writer.writerow([letter, beast_count[letter]])


if __name__ == "__main__":
    beasts = get_all_animals_by_letter()
    write_beasts_csv(beasts)
    print(f"Done, written to {CSV_FILENAME}")
