CREATE TABLE genres
(
	genre_id  INTEGER PRIMARY KEY AUTOINCREMENT,
	label            TEXT    UNIQUE NOT NULL
);

CREATE TABLE movies
(
	movie_id  INT PRIMARY KEY     NOT NULL,
	title     TEXT    NOT NULL,
	year      INT     NOT NULL,
	imdb_id   TEXT     NOT NULL,
	imdb_rating NUMBER NULL,
	imdb_poster TEXT NULL,
	description TEXT
);

CREATE TABLE movie_genres
(
	movie_genre_id  INTEGER PRIMARY KEY AUTOINCREMENT,
	movie_id        INT    NOT NULL,
	genre_id        INT    NOT NULL,
	FOREIGN KEY(movie_id) REFERENCES movies(movie_id),
	FOREIGN KEY(genre_id) REFERENCES genres(genre_id)
);

CREATE INDEX idx_movie_id
ON movie_genres (movie_id);

CREATE INDEX idx_genre_id
ON movie_genres (genre_id);


