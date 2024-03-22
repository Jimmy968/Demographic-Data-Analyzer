import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male'][['age']].mean()[0]
    average_age_men = round(average_age_men, 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = 100 * df['education'].value_counts()['Bachelors'] / df['education'].value_counts().sum()
    percentage_bachelors = round(percentage_bachelors, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_and_rich = df[(df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]
    higher_education_and_rich_percentage = round(100 * len(higher_education_and_rich) / len(higher_education), 1)
    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_and_rich = df[(~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) & (df['salary'] == '>50K')]
    lower_education_and_rich_percentage = round(100 * len(lower_education_and_rich) / len(lower_education), 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    # or        = df['hours-per-week'].value_counts()[min_work_hours]

    min_workers_and_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]

    rich_percentage = 100 * len(min_workers_and_rich) / len(min_workers)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100).idxmax()
    highest_earning_country_percentage = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100).max()
    highest_earning_country_percentage = round(highest_earning_country_percentage, 1)

    # Identify the most popular occupation for those who earn >50K in India.
    rich_indian_people = df[(df['salary'] == '>50K') & (df['native-country'] == 'India')]
    top_IN_occupation = rich_indian_people['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_and_rich_percentage}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_and_rich_percentage}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_and_rich_percentage,
        'lower_education_rich': lower_education_and_rich_percentage,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }