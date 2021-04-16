import sqlalchemy

db = 'postgresql://muz:muz@localhost:5432/muz'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

al_year = connection.execute("""SELECT name, year_of_issue FROM albums WHERE year_of_issue = 2011;
                            """).fetchall()
print(al_year)

tr_dur = connection.execute("""SELECT name, duration FROM tracks ORDER BY duration DESC;
                            """).fetchone()
print(tr_dur)

tr_dur2 = connection.execute("""SELECT name, duration FROM tracks WHERE duration >= 3.5 ORDER BY duration;
                            """).fetchall()
print(tr_dur2)

col_year = connection.execute("""SELECT name, year_of_issue FROM collections WHERE year_of_issue
                            BETWEEN 2018 AND 2020; 
                            """).fetchall()
print(col_year)

my_word = connection.execute("""SELECT name FROM tracks WHERE name LIKE '%%_my_%%' OR name LIKE '%%_My_%%';
                            """).fetchall()
print(my_word)

one_word = connection.execute("""SELECT name FROM tracks WHERE (LENGTH(name) - LENGTH(replace(name, ' ', ''))) = 0;
                            """).fetchall()
print(one_word)
