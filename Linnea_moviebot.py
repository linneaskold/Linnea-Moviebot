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
    {"title":"Ready or not","genre":"scary","mood":"tension","age":"16+"},
    {"title":"Dead Poets Society","genre":"drama","mood":"tragic","age":"13+"},
    {"title":"Bad boys","genre":"action","mood":"comedy","age":"16+"},
    {"title":"Coraline","genre":"animation","mood":"dark","age":"13+"},
    {"title":"Goosebumps","genre":"thriller","mood":"scary","age":"13+"},
    ]

exit_words = ["thank you","thx","bye","no"]






def run_moviebot():
      
    while True:
        genre = input ("What genre are you interested in?").strip().lower()
        mood = input ("What mood do you want?").strip().lower()
        age = input ("What age rating are you looking for? (7+, 13+, 16+)").strip().lower()

        recommendations = 0

      
        for movie in movies:
            score = 0
            if movie["genre"] == genre:
                score += 3
            if movie["mood"] == mood:
                 score += 2
            if movie["age"] == age:
                score += 2


            if score > 2:
               print("I recommend you to watch:", movie["title"])

               recommendations += 1

            if recommendations == 3:
                   break


         
     
        else: 
          print("Sorry, I couldn't find a movie that matches your preferences.")

        

        if input("Do you want another recommendation? (yes/no)").lower() in exit_words:
            print("Thank you for using MovieBot! Enjoy your movie!")
            break

      


run_moviebot()


#nästa gång kan jag försöka få den att ge feedback