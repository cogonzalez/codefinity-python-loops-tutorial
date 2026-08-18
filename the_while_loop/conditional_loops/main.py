# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Counter variable
short_name_count = 0

# Initialize index
i = 0
while i < len(countries):
    if len(countries[i]) < 7:
        print(countries[i], 'has a short name.')
        short_name_count += 1
    else:
        print(countries[i], 'has a long name.')
    i += 1

# Testing
print('Number of short country names:', short_name_count)