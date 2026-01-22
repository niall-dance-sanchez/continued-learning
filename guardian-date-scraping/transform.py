"""Functions for transforming data from the Guardian blind dates page."""

from datetime import datetime


def transform_ages_to_int(date_description: str) -> list[int]:
    """
    Extracts all of the ages in a string and 
    transforms their type to an integer.
    """

    ages = []
    age = ""

    for char in date_description:

        # check if the character is an integer
        if (ord(char) - ord('0') >= 0 and ord(char) - ord('0') <= 9):
            age += char
        else:
            if age:
                ages.append(int(age))
                age = ""

    # deals with an age being at the end of a string
    if age:
        ages.append(int(age))

    # ensures there are two recorded ages if both people are the same age
    if len(ages) == 1:
        ages.append(ages[0])

    return ages


def transform_date_datetime(datetime_string: str) -> datetime:
    """Transforms the date's date and time string into a datetime object."""

    # have to replace the Guardian's usage of 'Sept' to 'Sep' for datetime conversion
    if "Sept" in datetime_string:
        date_parts = datetime_string.split()
        date_parts[1] = "Sep"
        datetime_string = " ".join(date_parts)
        return datetime.strptime(datetime_string, "%-d %b %Y %H.%M %Z")

    return datetime.strptime(datetime_string, "%-d %b %Y %H.%M %Z")


def transform_date_article(date: tuple) -> list:
    """
    Transforms a single blind date article into a 
    clean format to be uploaded to the database.
    """

    transformed_date = []
    transformed_date.append(transform_date_datetime(date[0]))
    transformed_date.extend(transform_ages_to_int(date[1]))

    return transformed_date


def transform_all_dates(dates: list[tuple]) -> list[list]:
    """
    Transforms all of the Guardian blind date articles 
    into a clean format to be uploaded to a database.
    """

    return [transform_date_article(date) for date in dates]
