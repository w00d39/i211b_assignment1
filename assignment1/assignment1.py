import random, string, time, os

def open_english():
    try:
        #opening the file and reading it
        with open ('top_english_nouns_lower_100000.txt', 'r') as file: 
            english = file.read() #reads the file
            nouns = english.splitlines() #splits the file into a list of nouns
        return nouns
    except FileNotFoundError: #if the file is not found
        print("Error: The file 'top_english_nouns_lower_100000.txt' was not found.")
       
        

def memorable_generator(num):
    nouns = open_english()
    try:
        password = [] #what will be returned at the end and stores the password while it is being generated
        randyNum = string.digits #string of digits to be randomly selected
        for i in range(num): #for loop generates the password based on how big num is

            #does the random selection of the nouns and digits then concatenates together in pair
            pair = random.choice(nouns) + random.choice(randyNum)
            #adds the pair to password list
            password.append(pair)
            #joins the password list with hyphens into a string and stamps the time it was made
        password = "-".join(password) 
        stampedPassword = (password, time.asctime())
    
        #returning the password and the time it was generated
        return stampedPassword
    except nouns == None:
        return print("something went wrong. try again")


def random_generator(num):
    try:
        password = [] #what will be returned at the end and stores the password while it is being generated
        randyPool = string.ascii_letters + string.digits + string.punctuation #a pool of all possible characters randy can choose from
        for i in range(num): #for loop generates the password based on how big num is. Num in this case is the specified length of the password
            password.append(random.choice(randyPool)) #choosing the character from the pool and appending it to the password list
        password = "".join(password) #joins the password list into a string
        stampedPassword = (password, time.asctime()) # stamps the time it
        
        #returning the password and the time it was generated
        return stampedPassword
    except:
        return print("something went wrong. try again")

def save_password(directory, password):
    try:
        if os.path.exists(directory) == False: #if the directory does not exist
            os.makedirs(directory) #make the directory
        #opens the file and writes the password and the time it was generated
        with open(os.path.join(directory, 'Generated_Passwords.txt'), 'a') as file:
            file.write(password[0] + "\t " + password[1] + "\n")
    except:
        return print("something went wrong. try again")




option = input("Welcome! Do you want your password to be memorable or random? \n")

if option == "memorable": #if the user wants a memorable password
    for i in range(1000):
        password = memorable_generator(4)
        if password: #if the password was generated
            save_password('Memorable', password) #saves said passowrd


elif option == "random": #if the user wants a random password
    num = int(input("How many characters do you want your password to be? \n")) #follow up with desired length of password
    for i in range(1000):
        password = random_generator(num)
        if password: #if the password was generated
            save_password('Random', password) #saves said password
else: #if the user inputs something other than 'memorable' or 'random'
    print("Error: Invalid input. Please enter 'memorable' or 'random'.")

