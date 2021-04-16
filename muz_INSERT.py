import sqlalchemy

db = 'postgresql://muz:muz@localhost:5432/muz'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

artist_list = ['Course Of Nature', 'Ozzy Osbourne', 'Thirty Seconds To Mars', 'Disturbed', 'Lacuna Coil',
               'AC/DC', 'Linkin Park'
               ]

genres_list = ['Metal', 'Rock', 'Alternative', 'Gothic Metal', 'Rap']

albums_dict = {'Black Rain (Expanded Edition)': 2007, 'Endgame': 2011, 'Superkala': 2002, 'AMERICA': 2018,
               'The Lost Children': 2011, 'Shallow Life': 2009, 'Highway to Hell': 1979, 'Meteora': 2003
               }

track_dict = {'Not Going Away': [4.32, 8],
              "I Dont Wanna Stop": [3.59, 8],
              'The Almighty Dollar': [6.57, 8],
              'Architects': [3.42, 9],
              'Help Is On The Way': [3.57, 9],
              'Disparity By Design': [3.48, 9],
              'Wall of Shame': [4.02, 10],
              'Caught in the Sun': [4.51, 10],
              'Difference of Opinion': [4.02, 10],
              'Walk On Water': [3.05, 11],
              'Dangerous Night': [3.19, 11],
              'Rescue Me': [3.37, 11],
              'Hell': [4.15, 12],
              'A Welcome Burden': [3.31, 12],
              'This Moment': [3.05, 12],
              'Survive': [3.34, 13],
              "I Wont Tell You": [3.49, 13],
              'Not Enough': [3.40, 13],
              'Highway to Hell': [3.28, 14],
              'Girls Got Rhythm': [3.23, 14],
              "If You Want Blood (Youve Got It)": [4.34, 14],
              "Dont Stay": [3.07, 15],
              'Somewhere I Belong': [3.33, 15],
              'Lying from You': [2.55, 15],
              'Close My Eyes Forever': [3.35, 8]
              }

for i in artist_list:
    connection.execute(f"INSERT INTO artist(name) VALUES('{i}');")

for i in genres_list:
    connection.execute(f"INSERT INTO genres(name) VALUES('{i}');")

for i in albums_dict.items():
    connection.execute(f"INSERT INTO albums(name, year_of_issue) VALUES('{i[0]}', {i[1]});")

for i in track_dict.items():
    connection.execute(f"INSERT INTO tracks(name, duration, id_albums)"
                       f"VALUES('{i[0]}', {i[1][0]}, {i[1][1]});")

connection.execute("""
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (10, 3, 15);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (10, 2, 15);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (10, 1, 15);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (10, 5, 15);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (9, 2, 14);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (9, 1, 14);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (8, 1, 13);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (8, 2, 13);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (8, 4, 13);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (7, 1, 12);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (7, 2, 12);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (7, 3, 12);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (6, 2, 11);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (5, 1, 8);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (4, 3, 10);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (3, 1, 9);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (3, 2, 9);
                    INSERT INTO artist_genres_albums (artist_id, genres_id, albums_id)
                        VALUES (3, 3, 9);
                    """)

connection.execute("""
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 1',2013);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 2',2014);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 3',2015);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 4',2016);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 5',2017);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 6',2018);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 7',2019);
                    INSERT INTO collections (name, year_of_issue)
                        VALUES ('best of year 8',2020);
                    """)

connection.execute("""
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (1, 2);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (1, 3);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (1, 4);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (1, 5);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (1, 6);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (6, 11);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (6, 12);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (6, 3);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (6, 14);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (6, 16);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (7, 8);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (7, 15);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (7, 17);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (8, 18);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (8, 19);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (8, 13);
                    INSERT INTO collections_tracks (collections_id, tracks_id)
                        VALUES (8, 2);
                    """)
