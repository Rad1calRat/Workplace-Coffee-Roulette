import csv #import csv module
import random #import random module

name = [] #create an empty list to store the names of team members
email = [] #create an empty list to store the emails of team members
random.shuffle(name) # Shuffle the list of team members

def get_team_members(): #function to get team members from CSV file
    global name, email #global variables to be used in the function
    # Open CSV file containing team members
    with open('people.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # skip the first row of the csv file
        rows = list(csv_reader)
            # row 0 is a list containing the names of team members
            # row 1 is a list containing the emails of team members
        name = [row[0] for row in rows]
        csv_file.seek(0) # reset the cursor to the start of the file
        email = [row[1] for row in rows]


def save_pairing_history(pair): #function to save the pairing to a file
    try: 
        with open('historic.csv', 'a', newline="") as file:
            writer = csv.writer(file)
            writer.writerow(pair)
    except OSError:
        print("File not found")

def pair_up(): #function to pair up team members    
    global previously_paired, penalties #global variables to be used in the function 
    previously_paired = set() #create an empty set to store previously paired team members
    penalties = {} #create an empty dictionary to store the penalties
    if not hasattr(pair_up, 'previously_paired'): #if the function has not been run before
        pair_up.previously_paired = set() #create an empty set to store previously paired team members
        if not hasattr(pair_up, 'penalties'): #if the function has not been run before
            pair_up.penalties = {} #create an empty dictionary to store the penalties  
    num_pairs = len(name) // 2 # number of pairs of team members in the list
    for i in range(num_pairs):
        pair = name[i*2:(i+1)*2] #create a list of pairs of team members
        member1 = pair[0] #assign the first member of the pair to a variable
        if all(members in previously_paired for members in pair): #if the pair of team members is in the list of previously paired team members
            new_member = random.choice(name) #choose a new member from the list of team members
            pair[1] = new_member #assign the new member to the second member of the pair
            penalties[member1] = penalties.get(member1, 0) + 1 #increment the penalty for the first member of the pair by 1
        else:
            pair_up.penalties.update({member: penalties.get(member, 0) + 1 for member in pair}) #increment the penalty for each member of the pair by 1
        pair_up.previously_paired.update(pair) #add the pair of team members to the list of previously paired team members
        print(pair)
    save_pairing_history(pair) #save the pairing to a file

def main():
    get_team_members()
    while True:
        try:
            group_size = int(input("How many people per group for this round of Coffee-Roulette? ")) # number of people per group
            if group_size > len(name):
                print("The number of people per group is too large. Please try again.")
                raise ValueError #ValueError is a built-in exception that is raised when a function or operation is attempted which is not allowed.           
            elif group_size < 2:
                print("The number of people per group is too small. Please try again.")
                raise ValueError
            else:     
                num_groups = len(name) // group_size #number of groups
                for i in range(num_groups):
                    group = name[i*group_size:(i+1)*group_size]
                    print(group)
                pair_up() #call the pair_up function
                break
        except ValueError:
            continue
main()