import sqlalchemy
from pprint import pprint

db = 'postgresql://muz:muz@localhost:5432/muz'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

# al_year = connection.execute("""SELECT name, year_of_issue FROM albums WHERE year_of_issue = 2011;
#                             """).fetchall()
# print(al_year)
#
# tr_dur = connection.execute("""SELECT name, duration FROM tracks ORDER BY duration DESC;
#                             """).fetchone()
# print(tr_dur)
#
# tr_dur2 = connection.execute("""SELECT name, duration FROM tracks WHERE duration >= 3.5 ORDER BY duration;
#                             """).fetchall()
# print(tr_dur2)
#
# col_year = connection.execute("""SELECT name, year_of_issue FROM collections WHERE year_of_issue
#                             BETWEEN 2018 AND 2020;
#                             """).fetchall()
# print(col_year)
#
# my_word = connection.execute("""SELECT name FROM tracks WHERE name LIKE '%%_my_%%' OR name LIKE '%%_My_%%';
#                             """).fetchall()
# print(my_word)
#
# one_word = connection.execute("""SELECT name FROM tracks WHERE (LENGTH(name) - LENGTH(replace(name, ' ', ''))) = 0;
#                             """).fetchall()
# print(one_word)

ga_count = connection.execute("""SELECT DISTINCT g.name, COUNT(artist_id) FROM genres g
                            LEFT JOIN artist_genres_albums aga ON aga.genres_id = g.id_genres
                            GROUP BY g.name
                            """).fetchall()

pprint(ga_count)

ya_count = connection.execute("""SELECT COUNT(id_tracks) FROM tracks a
                            LEFT JOIN albums al ON al.id_albums = a.id_albums
                            WHERE year_of_issue BETWEEN 2019 AND 2020
                            GROUP BY year_of_issue;
                            """).fetchall()
pprint(ya_count)

al_avg = connection.execute("""SELECT al.name, AVG(duration) FROM tracks a
                          LEFT JOIN albums al ON al.id_albums = a.id_albums
                          GROUP BY al.name;
                          """).fetchall()
pprint(al_avg)

not2020 = connection.execute("""SELECT name FROM artist
                          WHERE name != (
                          SELECT DISTINCT ar.name FROM albums a 
                          LEFT JOIN artist_genres_albums aga ON aga.albums_id = a.id_albums
                          LEFT JOIN artist ar ON ar.id_artist = artist_id
                          WHERE year_of_issue = 2020);                      
                          """).fetchall()
pprint(not2020)

ar_col = connection.execute("""SELECT DISTINCT c.name FROM collections c
                         LEFT JOIN collections_tracks ct ON ct.collections_id = c.id_collections
                         LEFT JOIN tracks t ON t.id_tracks = ct.tracks_id
                         LEFT JOIN albums al ON al.id_albums = t.id_albums
                         LEFT JOIN artist_genres_albums aga ON aga.albums_id = al.id_albums
                         LEFT JOIN artist ar ON ar.id_artist = aga.artist_id
                         WHERE ar.name = 'Ozzy Osbourne';
                         """).fetchall()
pprint(ar_col)

g1_more = connection.execute("""SELECT a.name FROM albums a
                          LEFT JOIN artist_genres_albums aga ON aga.albums_id = a.id_albums
                          LEFT JOIN genres g ON g.id_genres = aga.genres_id
                          LEFT JOIN artist ar ON ar.id_artist = aga.artist_id
                          GROUP BY a.name
                          HAVING COUNT(g.id_genres) > 1;
                          """).fetchall()
pprint(g1_more)

not_col = connection.execute("""SELECT name FROM tracks
                          WHERE name NOT IN (
                          SELECT DISTINCT t.name FROM tracks t
                          RIGHT JOIN collections_tracks ct ON ct.tracks_id = t.id_tracks)
                          """).fetchall()
pprint(not_col)

ar_mind = connection.execute("""SELECT DISTINCT ar.name FROM artist ar 
                           LEFT JOIN artist_genres_albums aga ON aga.artist_id = ar.id_artist
                           LEFT JOIN albums al ON al.id_albums = aga.albums_id
                           LEFT JOIN tracks t ON t.id_albums = al.id_albums
                           WHERE t.duration = (
                           SELECT t.duration FROM artist ar 
                           LEFT JOIN artist_genres_albums aga ON aga.artist_id = ar.id_artist
                           LEFT JOIN albums al ON al.id_albums = aga.albums_id
                           LEFT JOIN tracks t ON t.id_albums = al.id_albums
                           ORDER BY duration
                           LIMIT 1);
                           """).fetchall()
pprint(ar_mind)

x = connection.execute("""SELECT al.name FROM albums al
                     LEFT JOIN tracks t ON t.id_albums = al.id_albums
                     WHERE (al.name, id_tracks) IN (
                     SELECT al.name, COUNT(id_tracks) FROM albums al
                     LEFT JOIN tracks t ON t.id_albums = al.id_albums
                     GROUP BY al.name
                     ORDER BY COUNT(id_tracks)
                     LIMIT 1)
                     """).fetchall()
pprint(x)

