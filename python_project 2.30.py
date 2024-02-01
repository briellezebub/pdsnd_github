import pandas as pd

# Dictionary for city data files.
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # Get user input for city (chicago, new york city, washington).
    city = input("Enter the name of the city to analyze (Chicago, New York City, Washington): ").lower()
    # Validate input
    while city not in ['chicago', 'new york city', 'washington']:
        city = input("Invalid city name. Please enter Chicago, New York City, or Washington: ").lower()

    # Get user input for month (all, january, february, ... , june).
    month = input("Enter the name of the month to filter by, or 'all' for no filter: ").lower()
    # Validate input
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input("Invalid month. Please enter a valid month or 'all': ").lower()

    # Get user input for day of week (all, monday, tuesday, ... sunday).
    day = input("Enter the name of the day to filter by, or 'all' for no filter: ").lower()
    # Validate input
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input("Invalid day. Please enter a valid day or 'all': ").lower()

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        df = df[df['month'].str.lower() == month]
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]

    return df

def display_statistics(df, city, month, day):
    """
    Displays statistics on the most frequent times of travel.
    """
    print(f"\n--- Statistics for {city.title()}, Month: {month.title()}, Day: {day.title()} ---")
    if not df.empty:
        # Display most common start station.
        most_common_start = df['Start Station'].mode()[0]
        print("1. Most common start station:", most_common_start)

        # Display most common end station.
        most_common_end = df['End Station'].mode()[0]
        print("2. Most common end station:", most_common_end)

        # Display most frequent combination of start and end station.
        most_common_trip = df.groupby(['Start Station', 'End Station']).size().nlargest(1)
        print("3. Most common trip:", most_common_trip)

        # Display total travel time.
        total_travel_time = df['Trip Duration'].sum()
        print("4. Total travel time:", total_travel_time)

        # Display average travel time.
        average_travel_time = df['Trip Duration'].mean()
        print("5. Average travel time:", average_travel_time)

        # Display counts of each user type.
        user_types = df['User Type'].value_counts()
        print("6. Counts of each user type:\n", user_types)

        # Gender and birth year statistics if available.
        if 'Gender' in df.columns:
            gender_counts = df['Gender'].value_counts()
            pri
            
            nt("7. Counts of each gender:\n", gender_counts)
        if 'Birth Year' in df.columns:
            earliest_year = df['Birth Year'].min()
            latest_year = df['Birth Year'].max()
            common_year = df['Birth Year'].mode()[0]
            print(f"8. Birth year stats - Earliest: {earliest_year}, Latest: {latest_year}, Most common: {common_year}")
    else:
        print("No data available for the selected filters.")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_statistics(df, city, month, day)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
