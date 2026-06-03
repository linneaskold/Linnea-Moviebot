
#Dehhär är träningsdata fï¿½r moviebotten i genre, mood och age rating.
movies = [
   
    #action

    {"title":"Iron Man","genre":"action","mood":"confident","age":"13+"},
    {"title":"Resident Evil","genre":"action","mood":"dread","age":"16+"},
    {"title":"Guardians of the Galaxy","genre":"action","mood":"fun","age":"13+"},
    {"title":"Bad boys","genre":"action","mood":"comedy","age":"16+"},
    {"title":"Avatar","genre":"action","mood":"grief","age":"13+"},
    {"title":"Avengers:Endgame","genre":"action","mood":"epic","age":"13+"},
    {"title":"Black Panther","genre":"action","mood":"heroic","age":"13+"},
    {"title":"The Dark Knight","genre":"action","mood":"intense","age":"16+"},
    {"title":"Spider-Man","genre":"action","mood":"heroic","age":"13+"},
    {"title":"Avengers: Infinity War","genre":"action","mood":"epic","age":"13+"},
    {"title":"Rush Hour","genre":"action","mood":"comedy","age":"13+"},

    #anime
    {"title":"Howls Moving Castle","genre":"anime","mood":"magical","age":"7+"},
    {"title":"A Silent Voice","genre":"anime","mood":"emotional","age":"13+"},
    {"title":"I Want To Eat Your Pancreas","genre":"anime","mood":"bittersweet","age":"13+"},
    {"title":"Suzume","genre" :"anime","mood":"adventure","age":"13+"},
    {"title":"The tunnel to summer, the exit of goodbyes","genre":"anime","mood":"touching","age":"13+"},
    {"title":"Your Name","genre":"anime","mood":"romantic","age":"13+"},
    {"title":"Weathering With You","genre":"anime","mood":"romantic","age":"13+"},
    

    #horror
    {"title":"Scream","genre":"horror","mood":"psychological","age":"16+"},
    {"title":"Ready or not","genre":"horror","mood":"tension","age":"16+"},
    {"title":"The Conjuring","genre":"horror","mood":"supernatural","age":"16+"},
    {"title":"The Ring","genre":"horror","mood":"creepy","age":"16+"},
    {"title":"The Exorcist","genre":"horror","mood":"demonic","age":"16+"},
    {"title":"A Quiet Place","genre":"horror","mood":"suspenseful","age":"13+"},
    {"title":"It","genre":"horror","mood":"scary","age":"16+"},
    

    #adventure
    {"title":"Jumanji","genre":"adventure","mood":"fun","age":"13+"},
    {"title":"The Maze Runner","genre":"adventure","mood":"intense","age":"13+"},
    {"title":"The Hunger Games","genre":"adventure","mood":"dystopian","age":"13+"},
    {"title":"Enola Holmes","genre":"adventure","mood":"mystery","age":"13+"},
    {"title":"The Lord of the Rings","genre":"adventure","mood":"epic","age":"13+"},
    {"title":"Pirates of the Caribbean","genre":"adventure","mood":"fun","age":"13+"},
    {"title":"Indiana Jones","genre":"adventure","mood":"classic","age":"13+"},
    {"title":"The Chronicles of Narnia","genre":"adventure","mood":"magical","age":"7+"},
    

    #sci-fi
    {"title":"Alien","genre":"sci-fi","mood":"isolation","age":"16+"},
    {"title":"Blade Runner","genre":"sci-fi","mood":"dystopian","age":"16+"},
    {"title":"The Matrix","genre":"sci-fi","mood":"mind-bending","age":"16+"},
    {"title":"Inception","genre":"sci-fi","mood":"thrilling","age":"13+"},
    {"title":"Interstellar","genre":"sci-fi","mood":"epic","age":"13+"},
    {"title":"Star Wars","genre":"sci-fi","mood":"adventure","age":"13+"},
    {"title":"Blade Runner 2049","genre":"sci-fi","mood":"atmospheric","age":"16+"},
    {"title":"The Martian","genre":"sci-fi","mood":"uplifting","age":"13+"},
    {"title":"Edge of Tomorrow","genre":"sci-fi","mood":"exciting","age":"13+"},
    {"title":"Minority Report","genre":"sci-fi","mood":"suspenseful","age":"13+"},
    {"title":"District 9","genre":"sci-fi","mood":"gritty","age":"16+"},

   

    #fantasy
    {"title":"Miss Peregrines Home For Peculiar Children","genre":"fantasy","mood":"dark","age":"13+"},
    {"title":"Harry Potter","genre":"fantasy","mood":"magical","age":"7+"},
    {"title":"The Chronicles of Narnia","genre":"fantasy","mood":"magical","age":"7+"},
    {"title":"Willow","genre":"fantasy","mood":"adventurous","age":"13+"},
    {"title":"Legend","genre":"fantasy","mood":"mythical","age":"13+"},
    {"title":"Dragonheart","genre":"fantasy","mood":"heroic","age":"13+"},
    {"title":"The Last Unicorn","genre":"fantasy","mood":"dreamlike","age":"7+"},
    {"title":"Labyrinth","genre":"fantasy","mood":"whimsical","age":"7+"},
    {"title":"The Hobbit: An Unexpected Journey","genre":"fantasy","mood":"adventurous","age":"13+"},
    {"title":"The Hobbit: The Desolation of Smaug","genre":"fantasy","mood":"exciting","age":"13+"},
    {"title":"The Hobbit: The Battle of the Five Armies","genre":"fantasy","mood":"heroic","age":"13+"},
    {"title":"Fantastic Beasts and Where to Find Them","genre":"fantasy","mood":"magical","age":"13+"},


   


    #disney
    {"title":"The princess and the frog","genre":"animation","mood":"nostalgic","age":"7+"},
    {"title":"Zootopia","genre":"animation","mood":"fun","age":"7+"},
    {"title":"Frozen","genre":"animation","mood":"magical","age":"7+"},
    {"title":"Moana","genre":"animation","mood":"adventure","age":"7+"},
    {"title":"Tangled","genre":"animation","mood":"romantic","age":"7+"},
    {"title":"Coco","genre":"animation","mood":"emotional","age":"7+"},
    {"title":"Mulan","genre":"animation","mood":"heroic","age":"7+"},
    {"title":"The Lion King","genre":"animation","mood":"epic","age":"7+"},


    #drama
    {"title":"Dead Poets Society","genre":"drama","mood":"tragic","age":"13+"},
    {"title":"Titanic","genre":"drama","mood":"romantic","age":"13+"},
    {"title":"Forrest Gump","genre":"drama","mood":"heartwarming","age":"13+"},
    {"title":"The Green Mile","genre":"drama","mood":"emotional","age":"16+"},
    {"title":"Good Will Hunting","genre":"drama","mood":"thought-provoking","age":"16+"},
    {"title":"The Pursuit of Happyness","genre":"drama","mood":"uplifting","age":"13+"},
    {"title":"Whiplash","genre":"drama","mood":"intense","age":"13+"},
    {"title":"Fight Club","genre":"drama","mood":"dark","age":"18+"},


    #thriller
    {"title":"Goosebumps","genre":"thriller","mood":"scary","age":"13+"},
    {"title":"Gone Girl","genre":"thriller","mood":"suspenseful","age":"16+"},
    {"title":"Shutter Island","genre":"thriller","mood":"mysterious","age":"16+"},
    {"title":"Prisoners","genre":"thriller","mood":"intense","age":"16+"},
    {"title":"The Silence of the Lambs","genre":"thriller","mood":"psychological","age":"16+"},
    {"title":"Nightcrawler","genre":"thriller","mood":"tense","age":"16+"},
    {"title":"The Girl with the Dragon Tattoo","genre":"thriller","mood":"gritty","age":"16+"},
    {"title":"Zodiac","genre":"thriller","mood":"investigative","age":"16+"},
    {"title":"The Prestige","genre":"thriller","mood":"mind-bending","age":"13+"},
    {"title":"Memento","genre":"thriller","mood":"puzzling","age":"16+"},

    #romance
    {"title":"The notebook","genre":"romance","mood":"romantic","age":"13+"},
    {"title":"La La Land","genre":"romance","mood":"bittersweet","age":"13+"},
    {"title":"A Star Is Born","genre":"romance","mood":"dramatic","age":"16+"},
    {"title":"Pretty Woman","genre":"romance","mood":"lighthearted","age":"13+"},
    {"title":"Ghost","genre":"romance","mood":"sentimental","age":"13+"},
    {"title":"Crazy Rich Asians","genre":"romance","mood":"fun","age":"13+"},
    {"title":"10 Things I Hate About You","genre":"romance","mood":"funny","age":"13+"},
    {"title":"When Harry Met Sally","genre":"romance","mood":"warm","age":"13+"},
    





    {"title":"Ready or not","genre":"scary","mood":"tension","age":"16+"},
    {"title":"Dead Poets Society","genre":"drama","mood":"tragic","age":"13+"},
    {"title":"Bad boys","genre":"action","mood":"comedy","age":"16+"},
    {"title":"Coraline","genre":"animation","mood":"dark","age":"13+"},
    {"title":"Goosebumps","genre":"thriller","mood":"scary","age":"13+"},
   ]

    #denhär är ord som man kan använda för att avsluta moviebot när den frågar om man vill ha en till rekommendation.
exit_words = ["thank you","thx","bye","no"]








#Denhär kör programmet
def run_moviebot():
      
    #Denhär innebär att sålänge som användaren inte avslutar programmet så kommer programmet köra.
    while True:

        #Denhär delen under frågar användaren om genre, mood och age och sparar användarens svar
        genre = input ("What genre are you interested in?").strip().lower()
        mood = input ("What mood do you want?").strip().lower()
        age = input ("What age rating are you looking for? (7+, 13+, 16+)").strip().lower()
       
        #Den sätter recomendations till 0 varje gång koden startar
        recommendations = 0
        #Denhär under gör en lista
        recommended_titles = []


      #Denhär under kommer jämföra användarens svar med träningsdata och ge rekommendationer baserat på hur väl de matchar. Ju mer de matchar desto högre poäng för filmen.
        for movie in movies:
            score = 0
            if movie["genre"].lower() == genre:
                score += 3
            if movie["mood"].lower() == mood:
                 score += 2
            if movie["age"].lower() == age:
                score += 2

                #Denhär under innebär om score är över 2 poäng kommer den rekommendera filmen och lägga till i rekomendations och när den har gett 3 rekommendationer så kommer den sluta ge fler rekommendationer.



            if score > 2:
               print("I recommend you to watch:", movie["title"])

               recommendations += 1

            if recommendations == 3:
                   break


        #Om rekommendationerna är 0 så kommer den säga att det inte kunde hitta en film som matchar användarens preferenser.
        if recommendations == 0:
            print("Sorry, I couldn't find a movie that matches your preferences.")

        #Här under så frågar den användaren om man gillade rekommendationerna och om man gillade dem och svarar yes så kommer den fråga vilken film man gillade bäst. Och när man skriver vilken film man gillade bäst så kommer den lägga till två poäng.
        else:
            like = input("Did you like the recommendations? (yes/no)").lower()
            if like == "yes":
                print("Which movie did you like the most?")
                if input().lower() == movie["title"].lower():
                    score += 2
                    
                
               #Här om är om man inte gillade rekommendationerna och svarar no så kommer den dra av två poäng.
            elif like == "no":
                score -= 2
            
                    
        #Här finns svaret som den ska skriva om  den inte kunde hitta en film som matchar användarens preferenser.
            else: 
             print("Sorry, I couldn't find a movie that matches your preferences.")

             #Här under så frågar den om användaren vill ha en till rekommendation.
        if input("Do you want another recommendation? (yes/no)").lower() in exit_words:
             print("Thank you for using MovieBot! Enjoy your movie!")
             break

    
         
         #lower() gör att det inte spelar någon roll om jag använder stora eller små bokstäver.
     
        else: 
          print("Sorry, I couldn't find a movie that matches your preferences.")

        

        if input("Do you want another recommendation? (yes/no)").lower() in exit_words:
            print("Thank you for using MovieBot! Enjoy your movie!")
            break

      


run_moviebot()


