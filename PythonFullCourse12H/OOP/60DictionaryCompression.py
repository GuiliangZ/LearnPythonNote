# dictionary compression = create dictionaries using an expression
#                           can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable }
# dictionary = {key: function(value) for (key, value) in iterable }


#convert fariheit to celcius

cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angles': 100, 'Chicago': 50}

cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}

print(cities_in_C)


# Find a sunny whether
weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles':"sunny", 'Chicago':"cloudy"}

sunny_wheather = {key: value for (key,value) in weather.items() if value == "sunny"}

print(sunny_wheather)


#Judge whether the temperature is good whether or not
desc_cities = {key: ("WARM" if value >= 40 else "CLOD") for (key,value) in cities_in_F.items()}

print(desc_cities)


# Use a function to replace the complex "if statement"
def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Cold"

desc_cities_2 = {key: check_temp(value) for (key, value) in cities_in_F.items()}
print(desc_cities_2)






