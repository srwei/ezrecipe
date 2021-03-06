import psycopg2
try:
    connection = psycopg2.connect(user = "stevenwei",
                                  password = "Chicago16",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "ezrecipe")

    cursor = connection.cursor()

    create_url_table_query = "CREATE TABLE urls ( \
                                recipe_id INTEGER PRIMARY KEY, \
                                recipe_url TEXT, \
                                picture_url TEXT \
                                )"
    
    cursor.execute(create_url_table_query)
    connection.commit()
    print('Succesfully created URL table')

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating database to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")