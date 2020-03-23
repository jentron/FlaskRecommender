# FlaskRecommender
This is a Recommendation Engine for IMDB movies written in Python, Flask and SQL for CS3580

Dr. Ball is wanting a complete app
I was thinking about doing the project using:

  - Flask (https://pypi.org/project/Flask/) 
  - SQLite3 (https://docs.python.org/3/library/sqlite3.html)


Installation:
  - Clone the repository
  - cd into "database" and run "python3 database.py" 
    - this will create the movies1.db file
    - this will fail if the movies1.db file already exists
    - the file database.py loads the sql schema from movies_db_ddl.sql 
  - cd back to the root folder (e.g.  ~/Documents/Weber/CS3580/FlaskRecommender/ )
  - launch the project with ./startup.sh
  - launch the url (http://127.0.0.1:5000/)
  
