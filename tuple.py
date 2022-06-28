#  tuples are ordered set of data
#  tuples are immutable just like strings
#  tuples use less memory than list
#  for things that shouldn't change can be given as tuple
#  tuples can be heterogeneous since it can have values of multiple types
#  But list is homogeneous as it can contain same type(string, tuple etc.) of details

t1 = "a", "b", "c", "d"  # tuple  # tuple without using parenthesis
t2 = ("x", "y", "z", "p", "q", "r")  # tuple with parenthesis, std way is to use parenthesis
print(t1)
print(t2)
##############################################
print()
name = "Tim"
age = 10
#  print method with normal values and tuple
print(name, age, "python", 2022)
print((name, age, "python", 2022))  # if we pass tuple as an argument to a function then parenthesis is must
#################################################

data = ["a", "b", "c"]
t_data = tuple(data)
print(t_data)
##############################################
a, b, c = 1, 2, 3  # tuple
print(a)
print(b)
print(c)
num = 4, 5, 6  # tuple
a, b, c = num  # a,b,c are not tuple, they are 3 diff variables
# since the tuple can't come on the left side of an assignment
print(a)  # unpacking a tuple
print(b)
print(c)

#  Unpacking tuple
metallica = "Ride the lightning", "Metallica", 1984
title, artist, year = metallica
print(title)
print(artist)
print(year)
#  List containing tuples, unpacking it
albums = [("Welcome to my nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("NightFlight", "Budgie", 1981)]

for album in enumerate(albums):
    index, (t, a, y) = album
    print(t, a, y)

for index, (t, a, y) in enumerate(albums):
    print(index + 1, t, a, y)
#####################################################
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow")
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     )]

for name, artist, year, songs in albums:
    print(name, artist, year, songs)

album  = albums[1]
print ()
print(album)
songs = album[3]
print(songs)
index, song = songs[2]
print()
print(song)
album1 = albums[2]
year = album1[2]
print()
print(year)