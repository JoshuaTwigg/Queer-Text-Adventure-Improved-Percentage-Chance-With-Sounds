import random

import time

import winsound

# """
# you enter the room.All is unfamiliar to you but what looks to be a donkey with a 6 on its forehead comes
# trotting up to you,all seems well until it speaks with the voice of a rusty hinge.
# """ maybe demon offers you a gift if you accept you are bound to the demon


def devil_dog():
    print("""
you open the door to a city of rubble and fire and the echo of flames. It was there that it came bounding towards you, 
its chest faced the hopeless grey thickening sky and arms and legs carried the evil soul like that of a dog 
from another world. Its body reversed like some sick joke, but unlike the others this one spoke. For some reason you 
feel the urge to pat the creature from previous memory of another life ,but this time its different. It reveals what it
has done to the city in devastating detail. From the depiction of its vile body, you know it must be a demon,
creatures well known for their treachery and deceit. It then offers you a choice.
    """)
    time.sleep(2)
    winsound.PlaySound("demon wav", winsound.SND_FILENAME)
    
    print("""
(a) It spares you and instead reduces a neighbouring city also to rubble and fire 
(b) It spares you and instead curses a small spirit child
(c) You offer yourself to the demon to safeguard other victims
    """)
    user = input("action? ")
    if user == "a":
        print("")
    elif user == "b":
        print("")
    elif user == "c":
        print("""
The demon betrays you, destroying the neighbouring city all whilst 
making you its sole witness to the destruction then making you its new host  
        """)


def spider_head():
    print("""
You come to what seems to be a great desert but in front of you stands a giant head with its mouth open. Spiders
endlessly rushing in and out of it they let you pass scurrying away as they sound. you enter the mouth
as there is no clear way to go. you go for ages and end up rising up cellar stairs. when you reach the top a 
strange sight. a horde of what used to be humans with flawed faces and skin hanging off their bones as if starving
as if trying to escape its host all facing away from you, facing the floor trying to hide themselves from an evil
and scorching sun and feeding at the dirt for something to eat. You cover your eyes, tricked by the suns welcoming
brightness, eerily quiet. you must be careful here.

(a) silently turn around and go back whence you came
(b) introduce yourself 
    """)
    time.sleep(3)
    winsound.PlaySound("eating wav", winsound.SND_FILENAME)

    user = input("action? ")
    if user:
        print("game end")


def death_roll_two():
    roll = random.randint(1, 2)
    print(roll)
    if roll != 1:
        print("""
realising your intention to leave the room and disobeying its order, it pounces on your head gnawing and grabbing
at anything it can get its hands on intending to kill you. Luckily, you manage to shake it off of you and make your
escape \n opening door!
        """)
        time.sleep(5)
        winsound.PlaySound("door wav", winsound.SND_FILENAME)
        spider_head()
    else:
        print("""
realising your intention to leave the room and disobeying its order, it pounces on your head gnawing and grabbing
at anything it can get its hands on. It then proceeds to devour your soul for refusing what it wants, cursing you
to its own fate.        
        """)
        exit()


def decision():
    user = input("action? ").lower()
    if user == "a" or "b" or "c":
        print("""
it quickly snatches the meal eats it and lets you go on points to the direction your looking for and goes back
to rocking in its rehearsed motions        
        """)
        devil_dog()


# """
# if you make the right decision the leper will point you to the safer door. if you are kind it could also be a trap.
# being kind is a trap.
# """

def the_leper():
    print(""" 
There in the center of a pitch white room, on a struggling one legged stool sits some sort of creep horror,
a pale leper resembling a feasted on human of some sorts with its back facing you rocking back and forth and nibbling.
There is a hastily built box on a small table adjacent to the horror with an unknown contents. You watch, stunned.
    """)
    winsound.PlaySound("ghoul wav", winsound.SND_FILENAME)
    print("""
(a) move silently to the nearest adjoining door hoping it doesnt notice you
(b) approach the horror
(c) ask the horror for directions
    """)
    user = input("action? ")
    if user == "a" or "b" or "c":
        print("""
no matter your attempt, it senses a change in the air and quickly turns to face you, rocking back and forth, nibbling
at itself and pointing to the rickety box. It looks unstable and could be aggressive if your not careful.
        """)
        print("""
(a) open the box
(b) Leave the box and leave the room  
        """)
        user_two = input("action? ")
        if user_two == "a":
            winsound.PlaySound("box open wav", winsound.SND_FILENAME)
            print("""
You open the box to find 3 items, what do you feed the creature?
  
(a) a long ago rotten apple
(b) carrot with the skin colour of the creature
(c) a finger         
            """)
            decision()
        else:
            death_roll_two()


def yes_no():
    user_two = input("accept the invitation to ensure you do not upset the man? y/n:").lower()
    if user_two == "n":
        print("you abandon that idea, you know if you are to find peace you must trust your instincts,"
              "swiftly exiting the room through the next door")
        devil_dog()
    elif user_two == "y":
        print("""
The painting has a strange but attractive lure to you, you pace forward towards it as if under some spell. The
bearded woman starts to resemble the most irresistible of idea to you
                """)
        death_roll()


# """
# def_painting if user chooses (a) they get a different set of options, if (b) you are attacked but still
# ends in friendly encounter, if (c) which is cowards way out you get unfriendly encounter.
# """

def death_roll():
    roll = random.randint(1, 4)
    if roll != 1 or 2:
        print("""
she too begins to pull you though you willingly assist her you can now not escape the painting
        """)
        print("you become tired and cannot move, who knows when you will awake")
        exit()
    elif roll == 3 or 4:
        print("""
she too begins to pull you though you willingly assist her, but as you reach the barrier between spirit and soul
the bearded woman seems to lack the strength to capture your soul. In a rage she drops you, cursing herself.
 You suddenly regain your strength of mind, how lucky you are to have escaped her clutches.
You swiftly exit the room through the nearest door. face your fears and you are rewarded with friendly animals.
        """)
        devil_dog()


def the_painting():
    print("""
You enter the room which is as empty as your belief in such a place. the room is dusty and scattered
with webbed furniture. A vintage tune plays on an a turn table of sorts but you cant make out any of the words.
In the center is a painting of a bearded woman. You feel the urge to inspect the painting, blowing off the dust
and feeling its texture. There is a bad energy about the place.
    """)
    print("""
(a) touch the painting 
(b) throw the painting to the floor
(c) resist your temptation and steer clear of the painting
    """)
    winsound.PlaySound("radio wav", winsound.SND_FILENAME)
    user = input("action?").lower()
    if user == "a":
        print("""
she comes to life, walks with a limp is talking but you cant understand what she is murmuring
a man in a painting moving. gesturing you to come and join him.looks trapped, a tortured soul pacing
to and fro as you watch bewildered
              """)
        yes_no()
    elif user == "b":
        print("""
you force the painting off its hinge and its crashes to the floor swirling in a rectangular motion,then...silence.
Then you hear footsteps beneath the floor you stand on and they are quickly becoming louder and louder. you feel 
a presence grab at you through your salvation, the thin wood floor and quickly leave the room.\n\n opening door!
            """)
        winsound.PlaySound("walking wav", winsound.SND_FILENAME)
        winsound.PlaySound("door wav", winsound.SND_FILENAME)
        devil_dog()
    elif user == "c":
        print("fearful of the painting, you decide to leave through the next door")
        print("opening door! ")
        winsound.PlaySound("door wav", winsound.SND_FILENAME)
        time.sleep(4)
        spider_head()


# """
# def path_one and def path_two random % chance that you will end up in a different room with different creatures and
# choices
# """

def path_one():
    roll = random.randint(1, 5)
    if roll != 1:
        print("""
@THE@PAINTING@
        """)
        print("a hand of unknown motive and body grabs at you but you manage to slip through its grasp")
        the_painting()
    else:
        print("\n@THE LEPER@")
        the_leper()


# """
# def path_two rewards user when they take risky door, they meet a friendly creature. choosing safe sounding
# door is a trap. 80% friendly leper or 20% unfriendly painting
# """

def path_two():
    roll = random.randint(1, 5)
    if roll != 1:
        print("a hand of unknown motive and body grabs at you but you manage to slip through its grasp...")
        the_leper()
    else:
        the_painting()


def decision_one():
    time.sleep(2)
    print("""
you inspect your surroundings. All seems fuzzy and grey, a constant storm, unfamiliar to you. 
you are in a room with 2 doors, door (a) seems to resemble memories, some that are good, perhaps some bad.
Door (b) resembles a dark shadow and you feel uneasy just by looking at it.      
    """)
    time.sleep(3)
    choice_one = input("which door do you choose: ")
    if choice_one == "a":
        print("You trust your senses,hoping it is your good memories")
        winsound.PlaySound("door wav", winsound.SND_FILENAME)
        path_one()
    elif choice_one == "b":
        print("you ignore your senses and pick the door even if it is eager to frighten you off ")
        winsound.PlaySound("door wav", winsound.SND_FILENAME)
        path_two()


# """
# start game
# """

start_game = input("do you wish to venture forth? y/n: ").lower()

if start_game == "y":
    print("where....")
    time.sleep(2)
    print("am i? ")
    time.sleep(2)
    print("......")
    time.sleep(2)
    print("who am i? ")
    time.sleep(3)
    time.sleep(1.5)
    print("i feel...uneasy here ")
    time.sleep(4)
    print("and....tired ")
    decision_one()
else:
    print("check under your bed tonight... ")
    exit()
