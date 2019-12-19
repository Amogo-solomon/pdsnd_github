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
    #print('\nHello! Let\'s explore some US bikeshare data!')
    print('\n  Exploration of some US Bikeshare data. Welcome!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    cities = ["chicago", "new york city", "washington"]

    city = input('\nEnter city: either all, chicago, new york city or washinton : '  '  ').lower()

    while city not in cities:
          print("The city you entered is not available")
          city = input("\nEnter city:  either all, chicago, new york cit or washington :  " ).lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    months = ["all", "january", "february", "march", "april", "may", "june"]
    month = input("\nEnter months from january to june or all, if you dont want to filter by month :   ").lower()
    while month not in months:
         print("The month you entered is not available ")
         month = input("\nEnter month from january to june: or all: ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ["all", "monday", "tuesday", "wednesday", "thursday" "friday", "saturday", "sunday"]
    day = input("\nEnter day of the week :   ").lower()

    while day not in days:
        print("Please check spelling and try again")
        day = input("Enter day of the week: ").lower()


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
    #load data into dataframe
    df = pd.read_csv(CITY_DATA[city])

    #convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #extract month, day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    #filter by month 
    if month != 'all':
       #use the index of the months list to get the corresponding int
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
    
       #filter by month to create the new dataframe
       df = df[df['month'] == month]
    
    #filter by day of week
    if day != 'all':
        
       #filter by day of week to create new dataframe
       df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    #"""Displays statistics on the most frequent times of travel."""
    """Displaying mode of the statistics on frequency of time travel"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month:', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common month:', common_month)
     


    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most common start hour:', common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    #"""Displays statistics on the most popular stations and trip."""
    """Displaying Statistics on the most popular stations and Trip"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station:', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station:', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['comb'] = df['Start Station'] + 'to' + df['End Station']
    common_comb = df['comb'].mode()[0]
    print('Most frequent combination of start and end station:', common_comb)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    #"""Displays statistics on the total and average trip duration."""
    """Displaying statistics on the total and average trip duration"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('Total trip duration:', trip_duration)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean
    print('Mean trip duration:', mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Type:', user_types)


    # TO DO: Display counts of gender

    
    try:
        gender_count = df['Gender'].fillna('No gender specification:').value_counts()
        print('Total Gender is:', gender_count)
    except:
        print('No data in Gender')


    # TO DO: Display earliest, most recent, and most common year of birth
   

    try:
        recent_birth_year = df['Birth Year'].fillna('Birth year not available for this city:').min()
        print(' The most earliest birth year is:', recent_birth_year)
    except:
        print('No data in Birth year')
        



    try:
        common_birth_year = df['Birth Year'].fillna('Birth specification not available:').mode()[0]
        print('The common birth year is:', common_birth_year)
    except:
        print('No data in common birth year')
        
    
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
