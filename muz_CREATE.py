import sqlalchemy

db = 'postgresql://muz:muz@localhost:5432/muz'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("""
                    create table genres(
                        id_genres serial primary key, 
                        name varchar(60) not null unique
                    );
                    
                    create table artist(
                        id_artist serial primary key, 
                        name text not null unique
                    );
                    
                    create table albums(
                        id_albums serial primary key, 
                        name text not null unique,
                        year_of_issue integer not null
                    );
                    
                    create table artist_genres_albums(
                        id_artist_genres_albums serial primary key,
                        artist_id integer references artist(id_artist), 
                        genres_id integer references genres(id_genres),
                        albums_id integer references albums(id_albums)
                    );
                    
                    create table collections(
                        id_collections serial primary key, 
                        name text not null unique,
                        year_of_issue integer not null
                    );
                    
                    create table tracks(
                        id_tracks serial primary key, 
                        name text not null unique,
                        duration numeric not null check(duration > 0),
                        id_albums integer references albums(id_albums)
                    );
                    
                    create table collections_tracks(
                        id_collections_tracks serial primary key,
                        collections_id integer references collections(id_collections), 
                        tracks_id integer references tracks(id_tracks)
                    );
                    """)
