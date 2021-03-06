import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

city = input("Which City would you like to analyze: chicago, new york city or washington:  ")
if city == "chicago":
    print("ok!")
elif city == "new york city":
    print("ok!")
elif city == "washington":
    print("ok!")
else:
    print("thats not a valid response, please retry")


    # get user input for month (all, january, february, ... , june)

month = input("Which month would you like to look at: Jan, Feb, Mar...:  ")
if month == "Jan":
    print("ok!")
elif month == "Feb":
    print("ok!")
elif month == "Mar":
    print("ok!")
elif month == "Apr":
    print("ok!")
elif month == "May":
    print("ok!")
elif month == "Jun":
    print("ok!")
elif month == "Jul":
    print("ok!")
elif month == "Aug":
    print("ok!")
elif month == "Sep":
    print("ok!")
elif month == "Oct":
    print("ok!")
elif month == "Nov":
    print("ok!")
elif month == "Dec":
    print("ok!")
else:
    print("thats not a valid response, please retry")

    # get user input for day of week (all, monday, tuesday, ... sunday)

day = input("Which day would you like to review: Mon, Tue, Wed....:  ")
if day == "Mon":
    print("ok!")
elif day == "Tue":
    print("ok!")
elif day == "Wed":
    print("ok!")
elif day == "Thu":
    print("ok!")
elif day == "Fri":
    print("ok!")
elif day == "Sat":
    print("ok!")
elif day == "Sun":
    print("ok!")
else:
    print("thats not a valid response, please retry")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month


    # display the most common day of week


    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station


    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
