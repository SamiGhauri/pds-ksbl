import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    try:
        usecols = ['id', 'neighbourhood', 'price', 'bedrooms', 'bathrooms', 'neighbourhood_group_cleansed', 'property_type', 'room_type', 'minimum_nights', 'number_of_reviews', 'last_review', 'reviews_per_month', 'availability_365']
        airbnb = pd.read_csv('listings.csv', usecols=usecols)
        neighbourhoods = pd.read_csv('neighbourhoods.csv')
        calendar = pd.read_csv('calendar.csv')
        return airbnb, neighbourhoods, calendar
    except FileNotFoundError:
        print('Error: could not find data files. Please make sure the necessary files are in the same directory as this script.')
        return None, None, None


def clean_data(df, neighbourhoods):
    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Remove listings with missing data
    df.dropna(subset=['price', 'reviews_per_month', 'bedrooms'], inplace=True)

    # Convert price column to float
    replacement = {'\$':'', ',':''}
    df['price'] = (df['price']
                      .replace(replacement, regex=True)
                      .astype('float')) 

    # Convert date column to datetime format
    df['last_review'] = pd.to_datetime(df['last_review'])

    # Replace values in the room_type column to make them more readable
    df['room_type'] = df['room_type'].replace({
        'Private room': 'Private',
        'Entire home/apt': 'Entire',
        'Shared room': 'Shared',
        'Hotel room': 'Hotel'
    })

    # Merge listings and neighbourhoods data and drop duplicates from neighbourhood
    neighbourhoods.drop_duplicates(subset=['neighbourhood_group'], inplace=True)
    cleaned_data = pd.merge(df, neighbourhoods[['neighbourhood_group', 'neighbourhood']], how='left', left_on='neighbourhood_group_cleansed', right_on='neighbourhood_group')
    cleaned_data.drop(['neighbourhood_x', 'neighbourhood_group_cleansed'], axis=1, inplace=True)
    cleaned_data.rename(columns={'neighbourhood_y': 'neighbourhood'}, inplace=True)
    return cleaned_data


def get_popular_neighborhoods(cleaned_data):
    popular_neighborhoods = cleaned_data.groupby('neighbourhood_group').size().sort_values(ascending=False).head(5)
    return popular_neighborhoods


def get_avg_price_neighborhoods(cleaned_data):
    avg_price_neighborhoods = cleaned_data.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False).head(5)
    return avg_price_neighborhoods


def plot_seasonal_trend(calendar):
    replacement = {'\$':'', ',':''}
    calendar['price'] = (calendar['price']
                          .replace(replacement, regex=True)
                          .astype('float')) 

    calendar['date'] = pd.to_datetime(calendar['date'])
    calendar['month'] = calendar['date'].dt.month
    calendar['year'] = calendar['date'].dt.year

    monthly_avg_price = calendar.groupby(['year', 'month'])['price'].mean().reset_index()

    plt.figure(figsize=(12,6))
    sns.lineplot(x='month', y='price', hue='year', data=monthly_avg_price)
    plt.title('Seasonal Trend of Average Airbnb Listing Price')
    plt.xlabel('Month')
    plt.ylabel('Average Price (USD)')
    plt.show()


def plot_correlation_matrix(cleaned_data):
    corr = cleaned_data.corr(method='pearson')
    plt.figure(figsize=(10,10))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation Matrix for Airbnb Listing Data')
    plt.show()


def plot_scatter(cleaned_data, x_col, y_col, title):
    plt.figure(figsize=(10,6))
    sns.scatterplot(x=x_col, y=y_col, data=cleaned_data)
    plt.title(title)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.show()


def plot_distribution_room_types(cleaned_data):
    sns.countplot(data=cleaned_data, x='room_type')
    plt.title('Distribution of Room Types')
    plt.xlabel('Room Type')
    plt.ylabel('Count')
    plt.show()


def plot_distribution_prices(cleaned_data):
    sns.histplot(data=cleaned_data, x='price', bins=10, kde=True)
    plt.title('Distribution of Prices')
    plt.xlabel('Price')
    plt.ylabel('Count')
    plt.show()


def plot_price_vs_reviews(cleaned_data):
    sns.scatterplot(data=cleaned_data, x='price', y='number_of_reviews')
    plt.title('Price vs. Number of Reviews')
    plt.xlabel('Price')
    plt.ylabel('Number of Reviews')
    plt.show()


def get_avg_price_by_room_type(cleaned_data):
    avg_price_by_room_type = cleaned_data.groupby('room_type')['price'].mean()
    return avg_price_by_room_type


if __name__ == '__main__':
    # Load data
    airbnb, neighbourhoods, calendar = load_data()

    if airbnb is None:
        # Exit the program if data files are not found
        exit()

    # Clean data
    cleaned_data = clean_data(airbnb, neighbourhoods)

    # Identify popular neighborhoods
    popular_neighborhoods = get_popular_neighborhoods(cleaned_data)
    print('Top 5 popular neighbourhoods with number of listings:')
    print(popular_neighborhoods)
    print('\n')

    # Identify average price of listings in popular neighborhoods
    avg_price_neighborhoods = get_avg_price_neighborhoods(cleaned_data)
    print('Top 5 neighbourhoods with highest average price of listings:')
    print(avg_price_neighborhoods)
    print('\n')

    # Determine seasonal trend
    try:
        plot_seasonal_trend(calendar)
    except TypeError:
        print('Error: could not generate seasonal trend. Please make sure the calendar data is in the correct format.')
    
    # Generate correlation matrix
    plot_correlation_matrix(cleaned_data)

    # Generate scatter plot
    plot_scatter(cleaned_data, 'bedrooms', 'price', 'Number of Bedrooms vs Price for Airbnb Listings in Lisbon')

    # Distribution of room types
    plot_distribution_room_types(cleaned_data)

    # Distribution of prices
    plot_distribution_prices(cleaned_data)

    # Relationship between price and number of reviews
    plot_price_vs_reviews(cleaned_data)

    # Average price by room type
    avg_price_by_room_type = get_avg_price_by_room_type(cleaned_data)
    print(avg_price_by_room_type)