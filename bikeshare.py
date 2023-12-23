import pandas as pd


def get_city():
    city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')
    return city.lower()


def get_time_period():
    time_period = input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    return time_period.lower()


def get_month():
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
    while month not in months:
        print("Invalid month. Please enter a valid month.")
        month = input('\nWhich month? January, February, March, April, May, or June?\n').lower()
    return month


def get_day():
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
    while day not in days:
        print("Invalid day. Please enter a valid day.")
        day = input('\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').lower()
    return day


def load_data(city):
    file_path = f'{city.replace(" ", "_")}.csv'
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File {file_path} not found. Please make sure the file exists.")
        return None


def display_raw_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_data = input('Do you wish to continue? Enter yes or no\n').lower()


def popular_times_of_travel(df, time_period, month, day):
    print('\nCalculating popular times of travel...')

    if time_period == 'month':
        # Check if month column is available
        if 'month' in df.columns:
            df = df[df['month'] == month]
        else:
            print("Month information is not available in the dataset.")
            return

    elif time_period == 'day':
        # Check if day_of_week column is available
        if 'day_of_week' in df.columns:
            df = df[df['day_of_week'] == day.title()]
        else:
            print("Day information is not available in the dataset.")
            return

    # Most common hour of day
    if 'hour' in df.columns:
        most_common_hour = df['hour'].mode()[0]
        print("Most common hour of day:", most_common_hour)
    else:
        print("Hour information is not available in the dataset.")


def popular_stations_and_trip(df):
    print('\nCalculating popular stations and trips...')

    # Most common start station
    if 'Start Station' in df.columns:
        most_common_start_station = df['Start Station'].mode()[0]
        print("Most common start station:", most_common_start_station)
    else:
        print("Start Station information is not available in the dataset.")

    # Most common end station
    if 'End Station' in df.columns:
        most_common_end_station = df['End Station'].mode()[0]
        print("Most common end station:", most_common_end_station)
    else:
        print("End Station information is not available in the dataset.")

    # Most common trip from start to end
    if 'Start Station' in df.columns and 'End Station' in df.columns:
        most_common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
        print("Most common trip from start to end:", most_common_trip)
    else:
        print("Start and End Station information is not available in the dataset.")


def trip_duration(df):
    print('\nCalculating trip duration...')

    # Total travel time
    if 'Trip Duration' in df.columns:
        total_travel_time = df['Trip Duration'].sum()
        print("Total travel time:", total_travel_time)
    else:
        print("Trip Duration information is not available in the dataset.")

    # Average travel time
    if 'Trip Duration' in df.columns:
        average_travel_time = df['Trip Duration'].mean()
        print("Average travel time:", average_travel_time)
    else:
        print("Trip Duration information is not available in the dataset.")


def user_info(df):
    print('\nCalculating user info...')

    # Counts of each user type
    if 'User Type' in df.columns:
        user_type_counts = df['User Type'].value_counts()
        print("Counts of each user type:\n", user_type_counts)
    else:
        print("User Type information is not available in the dataset.")

    # Counts of each gender (only available for NYC and Chicago)
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print("Counts of each gender:\n", gender_counts)
    else:
        print("Gender information is not available in the dataset.")

    # Earliest, most recent, most common year of birth (only available for NYC and Chicago)
    if 'Birth Year' in df.columns:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])

        print("Earliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", most_common_birth_year)
    else:
        print("Birth Year information is not available in the dataset.")


def statistics():
    while True:
        city = get_city()
        df = load_data(city)

        if df is not None:
            time_period = get_time_period()

            if time_period == 'month':
                month = get_month()
                day = None
            elif time_period == 'day':
                month = None
                day = get_day()
            else:
                month = None
                day = None

            popular_times_of_travel(df, time_period, month, day)
            popular_stations_and_trip(df)
            trip_duration(df)
            user_info(df)

            display_raw_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
    statistics()

#%%
