import sqlite3
from movie import Movie

conn =sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE movie (
            moviename text,
            actor text,
            actress text,
            year integer
            )""")

def insert_movie(mov):
    with conn:
        c.execute("INSERT INTO movie VALUES (:moviename,:actor,:actress,:year)", {'moviename':mov.moviename,'actor':mov.actor,'actress':mov.actress,'year':mov.year})


def get_movie_by_actor(actor):
    c.execute("SELECT * FROM movie WHERE actor=:actor", {'actor': actor})
    return c.fetchall()


def update_year(mov, year):
    with conn:
        c.execute("""UPDATE movie SET year = :year
                    WHERE actor = :actor AND actress = :actress""",
                  {'actor':mov.actor,'actress':mov.actress,'year':mov.year})


def remove_movie(mov):
    with conn:
        c.execute("DELETE from movie WHERE actor = :actor AND actress = :actress",
                  {'actor':mov.actor,'actress':mov.actress})

movie_1= Movie('Life of Pi','Suraj Sharma','Tabu','2011')

movie_2= Movie('The Dark Knight','Christian Bale','Maggie Gyllenhaal','2008')

insert_movie(movie_1)
insert_movie(movie_2)

movie_name=get_movie_by_actor('Christian Bale')

print(movie_name)

update_year(movie_1,2012)

remove_movie(movie_2)

movie_name=get_movie_by_actor('Christian Bale')

print(movie_name)



c.execute("INSERT INTO movie VALUES ('Vikram','Kamal','NIL','2022')")
c.execute("INSERT INTO movie VALUES ('Sarpatta Parambarai','Arya','Dushara Vijayan','2021')")
c.execute("INSERT INTO movie VALUES ('Thuppakki','Vijay','Kajal Aggarwal','2012')")
c.execute("INSERT INTO movie VALUES ('KGF2','Yash','Srinidhi Shetty','2022')")
c.execute("INSERT INTO movie VALUES ('The Founder','Michael Keaton','Linda Cardellini','2016')")
c.execute("INSERT INTO movie VALUES ('The Pursuit if Happyness','Will Smith','Thandiwe Newton','2006')")

conn.commit()

c.execute("INSERT INTO movie VALUES (?,?,?,?)",(movie_1.moviename,movie_1.actor,movie_1.actress,movie_1.year))

c.execute("INSERT INTO movie VALUES(:moviename,:actor,:actress,:year)",{'moviename':movie_2.moviename,'actor':movie_2.actor,'actress':movie_2.actress,'year':movie_2.year})

c.execute("SELECT * FROM movie")

c.execute("SELECT * FROM movie WHERE actor=?",('Kamal',))

print(c.fetchall())

c.execute("SELECT * FROM movie WHERE actor=:actor",{'actor':'Will Smith'})

print(c.fetchall())

c.execute("SELECT * FROM movie")

print(c.fetchall())

c.execute("SELECT actor FROM movie ORDER BY moviename")

print(c.fetchall())

conn.commit()



conn.close()