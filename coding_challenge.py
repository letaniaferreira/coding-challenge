import random
add_random_number = random.randint(1,10) #selects random number
print add_random_number
x = add_random_number
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
add_random_letter = random.choice(letters)
print add_random_letter * add_random_number
#def plain_text(message):
    #plain_text = raw_input("Enter your message here: ") #gets input from user
    #print ''