import time
import pandas as pd
import numpy as np

CITIES = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ]


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
    city_name=''
    while city_name not in CITIES :
        city_name=input('Which city do you want to explore Chicago , New York or Washington?\t').lower()
        if city_name in CITIES:
            city=CITIES[city_name]
        else:
            print('The name you entered is wrong\t')


    # get user input for month (all, january, february, ... , june)
    month_name=''
    while month_name not in MONTHS:
        month_name=input('Choose month to filter with or choose all for no filter \n').lower()
        if month_name in MONTHS:
            month=month_name
        else:
            print("The name you entered is wrong\t")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day_name=''
    while day_name not in DAYS:
        day_name=input('Choose day to filter with or choose all for no filter \n').lower()
        if day_name in DAYS:
            day=day_name
        else:
            print('The name you entered is wrong\t')

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
    
    df=pd.read_csv(city)
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month!='all':
        month = MONTHS.index(month)
        df = df.loc[df['month'] == month]
   
    if day!= 'all':
        df = df.loc[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]
    print("The most common month is:\t", MONTHS[common_month].title())

    # display the most common day of week
    most_common_day=df['day_of_week'].mode()[0]
    print("The most common day is:\t", most_common_day)

    # display the most common start hour
    most_common_start_hour =df['hour'].mode()[0]
    print("The most common hour is:\t", most_common_start_hour )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station :\t", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station :\t", most_common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is :" + str(frequent_combination.split("||")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=df['Trip Duration'].sum()
    print("Total travel time :\t", total_travel)


    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Mean Travel Time :\t',mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count of user types from the given fitered data is :\n" + str(user_types))

    if city == 'chicago.csv' :
        # TO DO: Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender))
        # Display earliest, most recent, and most common year of birth
        earliest_year=df['Birth Year'].min()
        print('Earliest year:\t',earliest_year)      
        recent_year=df['Birth Year'].max()
        print('Recent year:\t',recent_year)      
        most_common_year=df['Birth Year'].mode()[0]
        print('Most common year:\t',most_common_year) 
    
   
          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display(df):
    """Displays data on user request
    
    Args:
        df - Pandas DataFrame
    """
    print(df.head())
    next=0
    while True:
        view_data=input('\nIf you want to view next five row of raw data? Enter yes or no \n').lower()
        if view_data =='yes':
            next =next+5
            print(df.iloc[next:next+5])
        elif view_data =='no':
            print("\tGood bye")
            return
        else :
            print("\tInvalid input")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart == 'no':
            print("\tGood bye")
            break
        elif restart == 'yes':
            True
        else:
            print("\tInvalid input")
            break


if __name__ == "__main__":
	main()
