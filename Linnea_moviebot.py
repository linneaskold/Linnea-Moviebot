movies = [
    {"title":"Iron Man","genre":"action","mood":"confident","age":"13+"},
    {"title":"Howls Moving Castle","genre":"anime","mood":"magical","age":"7+"},
    {"title":"Scream","genre":"scary","mood":"psychological","age":"16+"},
    {"title":"A Silent Voice","genre":"anime","mood":"emotional","age":"13+"},
    {"title":"I Want To Eat Your Pancreas","genre":"anime","mood":"bittersweet","age":"13+"},
    {"title":"Jumanji","genre":"adventure","mood":"fun","age":"13+"},
    {"title":"Alien","genre":"sci-fi","mood":"isolation","age":"16+"},
    {"title":"Resident Evil","genre":"action","mood":"dread","age":"16+"},
    {"title":"Miss Peregrines Home For Peculiar Children","genre":"fantasy","mood":"dark","age":"13+"},
    {"title":"The princess and the frog","genre":"animation","mood":"nostalgic","age":"7+"},
    {"title":"Guardians of the Galaxy","genre":"action","mood":"fun","age":"13+"},
    {"title":"Suzume","genre" :"anime","mood":"adventure","age":"13+"},
    {"title":"The tunnel to summer, the exit of goodbyes","genre":"anime","mood":"touching","age":"13+"},
    ]

exit_words = ["thank you","thx","bye"]





def run_moviebot():
      
    while True:
        genre = input ("What genre are you interested in?")
        mood = input ("What mood do you want?")
        age = input ("What age rating are you looking for? (7+, 13+, 16+)")

        best_score = 0
        best_movie = "" 
        for movie in movies:
            score = 0
        if movie["genre"] == genre:
            score += 3
        if movie["mood"] == mood:
            score += 2
        if movie["age"] == age:
            score += 2
        if score > best_score:
            best_score = score
            best_movie = (movie["title"], score)
         
        if best_movie:      
          print("I recommend you to watch:", best_movie)
        else: 
          print("Sorry, I couldn't find a movie that matches your preferences.")
      

run_moviebot()


#Koden loopar och ger en film men den ger inte rätt film efter preferens