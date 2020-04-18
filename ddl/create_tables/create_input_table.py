import psycopg2
try:
    connection = psycopg2.connect(user = "stevenwei",
                                  password = "Chicago16",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "ezrecipe")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    create_input_table_query = "CREATE TABLE input_ingredients ( \
                                input_id SERIAL PRIMARY KEY, \
                                ingredients_str TEXT ARRAY \
                                )"
    
    cursor.execute(create_input_table_query)
    print("INPUT INGREDIENTS table successfully created") 


    connection.commit()

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while creating database to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")