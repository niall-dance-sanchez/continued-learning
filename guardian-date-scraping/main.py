"""Script for the ETL of the Guardian blind date page."""

from extract import scrape_all_dates, scrape_date_page
from transform import transform_ages_to_int, transform_all_dates

from datetime import datetime

if __name__ == "__main__":

    # data = scrape_all_dates()
    # print(data)

    page = scrape_date_page(1)
    print(page)

    print(transform_all_dates(page))

    # date = page[0][1]

    # print(datetime.strptime(page[2][0], "%-d %b %Y %H.%M %Z"))
    # print(transform_ages_to_int(date))
