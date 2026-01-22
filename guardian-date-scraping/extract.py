"""Functions for extracting data from the Guardian blind dates page."""

from requests import get
from bs4 import BeautifulSoup


def scrape_front_page_date(page_number: int) -> list[tuple]:
    """
    Scrapes the data for a chosen guardian blind date page and returns 
    it as a list of tuples where each tuple contains the title and 
    date of the blind date.
    """
    scraped_data = []
    url = f"https://www.theguardian.com/lifeandstyle/series/blind-date?page={page_number}"

    page = get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    dates = soup.find_all("div", class_="dcr-11l4sjk")

    for date in dates:
        people = date.find("div", class_="dcr-oi4shr")
        article_date = date.find("span", class_="dcr-8fifzy")
        url = date.find("a", class_="dcr-2yd10d", href=True)

        try:
            scraped_data.append((article_date.text, people.text, url["href"]))
        except AttributeError:
            print("Different Format")

    return scraped_data


def scrape_all_front_page_dates() -> list[tuple]:
    """Scrapes all of the blind dates available on the Guardian website."""

    is_new_page = True
    page_number = 1
    all_dates = []

    while is_new_page:
        page_data = scrape_front_page_date(page_number)

        if page_data[0] in all_dates:
            is_new_page = False
        else:
            all_dates.extend(page_data)
            page_number += 1

    return all_dates


def scrape_all_article_data(front_page_data: list[tuple]) -> list[tuple]:
    """Scrapes relevant data within each data article."""

    url = "https://www.theguardian.com/"
    couple_data = []

    for date in front_page_data:
        page = get(url + date[2])
        soup = BeautifulSoup(page.content, "html.parser")

        date_article = soup.find_all("div", class_="dcr-1uvtuj9")

        page = get(url + date[2])
        soup = BeautifulSoup(page.content, "html.parser")

        date_article = soup.find("div", class_="dcr-1uvtuj9")

        if not date_article:
            date_article = soup.find("div", class_="dcr-1x40mxr")

        couple_names = date_article.find("h2", class_="dcr-n4qeq9")

        if couple_names:
            couple_names = couple_names.text.split()
            couple_data.append((couple_names[0], couple_names[-1]))
        else:
            couple_names = date_article.find("h3", class_="dcr-130mj7b")
            if couple_names:
                couple_names = couple_names.text.split()
                couple_data.append((couple_names[0], couple_names[-1]))

    return couple_data


if __name__ == "__main__":

    front_pages = scrape_all_front_page_dates()
    for i in range(1, 41):
        print(f"page {i}")
        front_pages = scrape_front_page_date(i)
        article_data = scrape_all_article_data(front_pages)
        print(article_data)
        print(f"front {len(front_pages)}")
        print(f"article {len(article_data)}")

    # front_page_data = scrape_front_page_date(10)

    # url = "https://www.theguardian.com/"
    # couple_data = []

    # for date in front_page_data:
    #     page = get(url + date[2])
    #     soup = BeautifulSoup(page.content, "html.parser")

    #     date_article = soup.find_all("div", class_="dcr-1uvtuj9")

    #     page = get(url + date[2])
    #     soup = BeautifulSoup(page.content, "html.parser")

    #     date_article = soup.find("div", class_="dcr-1uvtuj9")

    #     if not date_article:
    #         date_article = soup.find("div", class_="dcr-1x40mxr")

    #     couple_names = date_article.find(
    #         "h2", class_="dcr-n4qeq9")

    #     if couple_names:
    #         couple_names = couple_names.text.split()
    #         if couple_names:
    #             couple_data.append((couple_names[0], couple_names[-1]))
    #     else:
    #         couple_names = date_article.find(
    #             "h3", class_="dcr-130mj7b")
    #         if couple_names:
    #             couple_names = couple_names.text.split()
    #             if couple_names:
    #                 couple_data.append((couple_names[0], couple_names[-1]))

    # print(couple_data)
