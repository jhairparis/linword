#Fichero para visualozar la tabla users de la base de datos linword


import psycopg2

try:
    conn = psycopg2.connect(
        "postgres://linword_user:mqd4wIWFLQAqI0XSQoEQhBLjDeEtqbQW@dpg-cncijceg1b2c739i83jg-a.oregon-postgres.render.com/linword"
    )
    cur = conn.cursor()

    cur.execute("SELECT * FROM users")
    print(cur.fetchall())

    conn.close()
    print('Query executed successfully!')

except Exception as e:
    print('I am unable to connect to the database')
    print(e)