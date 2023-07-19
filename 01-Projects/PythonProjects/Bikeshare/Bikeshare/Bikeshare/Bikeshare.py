import time
import pandas as pd
from tabulate import tabulate
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
# list for month + all
MONTH_LIST=['all','january','february','march','april'
            ,'may','june','july','august','september',
            'october','november','december']
# list for day + all
DAY_LIST=['all','monday','tuesday','wednesday','thursday'
          ,'friday','saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input('Please enter an city name :\n').lower()
      if city in CITY_DATA:
          break
      else:
          print('Sorry... city name.is not invalid..! :')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
       month = input("Please enter an month name or \'all' to show all month:\n").lower()
       if month in MONTH_LIST:
           break
       else:
          print('Oops.....incorrect month name...! :')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("Please input day name or \'all' to show all day:\n").lower()
        if day in DAY_LIST:
            break
        else:
          print('Oops.....incorrect day name...! :')

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

    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day of week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months=MONTH_LIST
        month = months.index(month) 

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].mode()[0]
    print('most common month :',common_month)
    print('-'*20)

    # TO DO: display the most common day of week
    common_day=df['day of week'].mode()[0]
    print('most common day :',common_day)
    print('-'*20)

    # TO DO: display the most common start hour
   # extract hour from the Start Time column to create an hour column
    df['hour']=df['Start Time'].dt.hour
   # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)
    print('-'*20)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('common Start Station : ',start_station)
    print('-'*20)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('common end Station : ',end_station)
    print('-'*20)

    # TO DO: display most frequent combination of start station and end station trip
    combination_station=df['Start Station']+ df['End Station']
    combination_station=combination_station.mode()[0]
    print('Common Combination Station : ',combination_station)
    print('-'*20)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # TO DO: display total travel time
    timea = df['Trip Duration']
    print('Total Travel Time is : ', timea.sum())
    print('-'*20)
    # TO DO: display mean travel time
    print('Average Travel Time is :' , timea.mean())
    print('-'*20)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types =df['User Type'].value_counts()
    print(user_types)
    print('-'*20)
    # TO DO: Display counts of gender
    if CITY_DATA !='washington':
       Gender=df['Gender'].value_counts()
       print(Gender)
       print('-'*20)
       # TO DO: Display earliest, most recent, and most common year of birth
       year_of_birth = df['Birth Year'].mode()[0]
       print('common year of birth : ',int(year_of_birth))
       print('-'*20)
       earliest = df['Birth Year'].min()
       print('earliest of birth: ',int(earliest))
       print('-'*20)
       earliest = df['Birth Year'].max()
       print('most recent of birth: ',int(earliest))
       print('-'*20)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data_display(df):
    i=0
    while True:
        display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        start_time = time.time()
        if display_data.lower() != 'yes':
           break
        try:
           print(tabulate(df.iloc[np.arange(0+i,5+i)], headers ="keys", tablefmt="simple"))
           print("\nThis took %s seconds." % (time.time() - start_time))
           print('-'*40)
           i+=5
        except :
            print('Data limit reached ......!')
            break


def data_show(df):
    " Displays rows data in DataFrame "
    show_data=input('\nWould you like to see 5 rows ? Enter yes or  press any key to exit.\n')
    if show_data.lower()=='yes':
        start_time = time.time()
        rows=5
         # to center and display all Columan in DataFrame
        pd.set_option('colheader_justify', 'center')
        pd.set_option('display.max_columns',200)
        df_rwos=df.head(rows)
        print(df_rwos)
        print("\nThis took %s seconds." % (time.time() - start_time))
        while True:
            contenu_show = input('\nWould you like to increase 5 rows ? Enter yes or  press any key to exit.\n')
            if contenu_show.lower()=='yes':
                rows+=5
                df_rwos=df.head(rows)
                print(df_rwos)
                print("\nThis took %s seconds." % (time.time() - start_time))
            else:
                break
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
        # data_show(df)
        data_display(df)
        restart = input('\nWould you like to restart? Enter yes or press any key to exit.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
 	main()
