## 1. If Statements ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4]) #we assigned the fifth element as the row index 4.
    
    if price == 0.0:  
        free_apps_ratings.append(rating)
        #we are trying to assigned the freeapps to a different list
avg_rating_free = sum(free_apps_ratings) / len(free_apps_ratings)
    
    # Complete the code from here

## 2. Booleans ##

a_price = 0

if a_price == 0:
    print('This is free')
if a_price == 1:
    print('This is not free')

## 3. The Average Rating of Non-free Apps ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_apps_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])   
    if price > 0.0:
        non_free_apps_ratings.append(rating)
    
avg_rating_non_free = sum(non_free_apps_ratings) / len(non_free_apps_ratings)

## 5. Multiple Conditions ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

free_games_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    genre = row[11]
    if price == 0.0 and genre == 'Games':
        free_games_ratings.append(rating)
avg_rating_free_games = sum(free_games_ratings)/ len(free_games_ratings)
    # Complete code from here

## 6. The or Operator ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    if genre == 'Games' or genre == 'Social Networking':
        games_social_ratings.append(rating)
avg_games_social = sum(games_social_ratings)/len(games_social_ratings)
print(avg_games_social)
    # Complete code from here

## 7. Combining Logical Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

free_games_social_ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    
    if (genre == 'Social Networking' or genre == 'Games') and price == 0:
        free_games_social_ratings.append(rating)
        
avg_free = sum(free_games_social_ratings) / len(free_games_social_ratings)

non_free_games_social_ratings= []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    if (genre=='Social Networking' or genre=='Games') and price>0:
        non_free_games_social_ratings.append(rating)
avg_non_free = sum(non_free_games_social_ratings)/len(non_free_games_social_ratings)
# Non-free apps (average)

## 8. The Not Operator ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

non_free_non_sn_games = []
for row in apps_data[1:]:
    rating = float(row[7])
    genre = row[11]
    price = float(row[4])
    if not (genre=='Social Networking' or genre =='Games') and price>0:
        non_free_non_sn_games.append(rating)
avg_non_free_non_sn_games =                         sum(non_free_non_sn_games)/len(non_free_non_sn_games)
    
    # Complete code here

## 9. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()



ratings = []
for row in apps_data[1:]:
    rating = float(row[7])
    price = float(row[4])
    if price > 9:
        ratings.append(rating)
avg_rating = sum(ratings)/len(ratings)
n_apps_more_9 = len(ratings)
n_apps_less_9 = len(apps_data[1:]) - len(ratings)

## 10. The else Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    else:
        app.append('non-free')
apps_data[0].append('free_or_not')
print(apps_data[:6])
    # Complete code from here

## 11. The elif Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
opened_file.close()

for app in apps_data[1:]:
    price = float(app[4])
    if price == 0.0:
        app.append('free')
    elif price > 0 and price < 20:
        app.append('affordable')
    elif price > 20 and price < 50:
        app.append('expensive')
    else: 
        app.append('very expensive')
apps_data[0].append('price_label')
print(apps_data[:6])
    # Complete code from here