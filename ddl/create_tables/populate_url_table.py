import psycopg2
import csv
from bs4 import BeautifulSoup
import re
import requests

try:
    connection = psycopg2.connect(user = "stevenwei",
                                  password = "Chicago16",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "ezrecipe")

    cursor = connection.cursor()

    try:
        with open('/Users/stevenwei/Programming/Projects/django-ezrecipe-react/ddl/src_data/recipes.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                recipe_id = row[0]
                recipe_url = "http://www.allrecipes.com/recipe/{}".format(row[0])
                response = requests.get(recipe_url)
                soup = BeautifulSoup(response.text, "html.parser")
                x = soup.find_all("img", class_= "rec-photo")
                if x:
                    u = re.findall(r'src="(.*?)"', str(x))[0]
                    picture_url = u
                if not x:
                    picture_url = "no picture"
                entry = [recipe_id, recipe_url, picture_url]
                cursor.execute("INSERT INTO urls VALUES (%s, %s, %s)", entry)
                print("Populated URLS for {}".format(row[1]))
            print("Successfully inserted into the ingredients table")

    except:
        print("Failed insert URLS recipe table")

    connection.commit()

    # Print PostgreSQL version

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating database to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")