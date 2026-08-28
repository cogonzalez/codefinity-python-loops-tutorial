# List of trips
trips = [['france', 'germany', 'italy', 'spain', 'netherlands', 'sweden', 'norway', 'switzerland', 'austria', 'portugal', 'belgium'],
         ['japan', 'china', 'thailand', 'vietnam', 'indonesia', 'india', 'malaysia', 'philippines', 'singapore', 'mongolia'],
         ['usa', 'canada', 'mexico', 'brazil', 'argentina', 'colombia', 'peru', 'chile', 'ecuador'],
         ['egypt', 'morocco', 'south africa', 'tunisia', 'algeria', 'kenya', 'nigeria', 'ethiopia'],
         ['australia', 'new zealand', 'fiji', 'papua new guinea', 'samoa']]

# List of all countries 
countries = []

# Iterate through each trip (sublist) in the nested list
for i in range(0,len(trips)):
    # Iterate through each item in the current trip (sublist)
    for j in range(0,len(trips[i])):
        # Capitalize each country name and append to countries
        countries.append(trips[i][j].capitalize())
# Testing
print('List of Countries:', countries)