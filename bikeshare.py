import time
import pandas as pd
import numpy as np
import calendar as cl
import datetime as dt


def dict_dataset():
    """
        Containing the datasets used in the program
        
        Return: 
            (dict): dict_dst - dictionary of the datasets used in the program
    """
    # dictionary of datasets
    dict_dst = { 
        'chicago': 'chicago.csv',
        'new york city': 'new_york_city.csv',
        'washington': 'washington.csv' 
    }
    return dict_dst
    

def raw_data():
    """ 
        Raw data is displayed upon request by the user in this manner: 
            A prompt asks the user to enter a city to see its raw data or 'q' to quit this option.
            If correct city is entered 5 lines of raw data is displayed and the user is asked
            to enter y(yes) or n(no) if he/she wants to see 5 more lines of raw data, 
            and the prompt continues to ask and displays until the user says 'n/no'.
    """
    try: 
        print('Hello! Let\'s see some US cities\' bikeshare raw data!')

        # list of cities
        list_city = ['chicago', 'new york city', 'washington']

        while True: 
            city = (input('Enter city[chicago, new york city, washington] to see its raw data or \'q\' to quit this option: ')).lower()
            if city not in list_city and city == 'q':
                break
            elif city not in list_city:
                print('Sorry, incorrect city. Try again!')
            else:
                # dictionary of datasets
                dict_dts = dict_dataset()
                # Load file into a dataframe
                df = pd.read_csv(dict_dts[city])
                # number of row in the dataframe
                num_row = df.shape[0]
                # number of line to display
                nline = 5
                print(df.head(nline))
                while True:
                    see_more = (input('Press y(yes) to see more of this dataset or n(no) to quit: ')).lower()
                    if see_more == 'y' or see_more == 'yes':
                        print(df[nline:nline+5])
                        nline += 5
                    elif see_more == 'n' or see_more == 'no':
                        break
                    else:
                        print('Sorry, incorrect response. Try again!')
    except (ValueError, KeyboardInterrupt): 
        print('\nSorry, invalid input!\n')
    else: 
        print('-'*40)
        print('\n')
                  

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    try:
        # Dictionary of city, month and day
        dict_cmd = {
            'city': ['chicago', 'new york city', 'washington'],
            'month': ['all', 'january', 'february', 'march', 'april', 'may', 'june'],
            'day': ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        } 
        
        # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True: 
            city = (input('Enter city [chicago, new york city, washington]: ')).lower()
            if city in dict_cmd['city']:
                break
            else: 
                print('Sorry, incorrect city. Try again!')
                
        # TO DO: get user input for month (all, january, february, ... , june)
        while True: 
            month = (input('Enter month [all, january, february, ... , june]: ')).lower() 
            if month in dict_cmd['month']:
                break
            else: 
                print('Sorry, incorrect month. Try again!')
                
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True: 
            day = (input('Enter day of week [all, monday, tuesday, ... sunday]: ')).lower()
            if day in dict_cmd['day']:
                break
            else: 
                print('Sorry, incorrect day. Try again!')
                
    except (TypeError, ValueError, KeyboardInterrupt):
        print('\nSorry, invalid input!')
    else: 
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
    # dictionary of datasets
    dict_dts = dict_dataset()
    
    # Load file into a dataframe
    df = pd.read_csv(dict_dts[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df        
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['Start Time'].dt.month
    most_common_month = list(cl.month_name)[month.mode()[0]]
    print('The most common month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = (df['Start Time'].dt.weekday_name).mode()[0]
    print('The most common day of the week:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = (df['Start Time'].dt.hour).mode()[0]
    print('The most common start hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station:', most_start_station)

    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station:', most_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = (most_start_station, most_end_station)
    print('Frequent combination of start and end station trip:', most_frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # convert the End Time column to datetime 
    df['End Time'] = pd.to_datetime(df['End Time'])
    # calculate travel time in minutes for each row
    df['Travel Time'] = (df['End Time'] - df['Start Time']).dt.seconds / 60
    total_travel_time = df['Travel Time'].sum()
    print('Total travel time(minutes):', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print('Mean travel time(minutes):',  mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('Counts of user types:\n{}'.format(count_user_type))
    
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('\nCounts of gender:\n{}'.format(count_gender))
    else:
        print('\nSorry, no \'Gender\' data for this dataset!')
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # earliest year of birth
        earliest_yob = df['Birth Year'].min()
        print('\nEarliest year of birth:', earliest_yob)

        # most recent year of birth
        most_recent_yob = df['Birth Year'].max()
        print('Most recent year of birth:', most_recent_yob)

        # most common year of birth
        most_common_yob = df['Birth Year'].mode()[0]
        print('Most common year of birth:', most_common_yob)
    else:
        print('\nSorry, no \'Birth Year\' data for this dataset!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        raw_data()
        
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
