from random import randint

import time

print ("Welcome to the magic 8 ball\n")

print((""" 	      _.a$$$$$a._
            ,$$$$$$$$$$$$$.
          ,$$$$$$$$$$$$$$$$$.
         d$$$$$$$$$$$$$$$$$$$b
        d$$$$$$$$~   ~$$$$$$$$b
       ($$$$$$$p   _   q$$$$$$$)
       $$$$$$$$   (_)   $$$$$$$$
       $$$$$$$$   (_)   $$$$$$$$
       ($$$$$$$b       d$$$$$$$)
        q$$$$$$$$a._.a$$$$$$$$p
         q$$$$$$$$$$$$$$$$$$$p
           $$$$$$$$$$$$$$$$$ 
             $$$$$$$$$$$$$ 
               ~$$$$$$$~ \n"""))

question = input("ask your question: ")

print()

if question == quit:
        
        exit()
else:        
        print ("Hold on while I think...\n")

        time.sleep(randint(0,15)+1)

        randomNumber = randint(0,2)+1

        if randomNumber == 1:

                yesan = randint(0,4)+1

                if yesan == 1:

                        print ("It is certain")

                elif yesan == 2:

                        print ("It is decidedly so")

                elif yesan == 3:

                        print ("without a doubt")

                elif yesan == 4:

                        print ("Yes Definitely")

                elif yesan == 5:

                        print ("you may rely on it")

        elif randomNumber == 2:

                maybe = randint(0,4)+1

                if maybe == 1:

                        print ("reply hazy try again")

                elif maybe == 2:

                        print ("ask again later")
        
                elif maybe == 3:

                        print ("better not tell you now")

                elif maybe == 4:

                        print ("cannot predict now")

                elif maybe == 5:

                        print ("concentrate and ask again")

        elif randomNumber == 3:

                no = randint(0,4)+1

                if no == 1:

                        print ("don't count on it")
        
                elif no == 2:

                        print ("my reply is no")

                elif no == 3:

                        print ("my sources say no")

                elif no == 4:

                        print ("outlook not so good")

                elif no == 5:

                        print ("very doubtful")
#Made By Patrick Bowden 
