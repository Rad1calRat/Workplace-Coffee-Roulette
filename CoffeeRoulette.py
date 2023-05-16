import csv
import random

name = [] #create an empty list to store the names of team members
email = [] #create an empty list to store the emails of team members

def get_team_members():
    # Function to get team members from CSV file
    
    global name, email #global variables to be used in the function
    
    with open('people.csv', 'r') as csv_file: #open the CSV file
        csv_reader = csv.reader(csv_file, delimiter=',') # Read the CSV file
        next(csv_reader) # Skip the first row of the csv file
        
        for row in csv_reader:
            name.append(row[0])  # Append the name to the name list
            email.append(row[1])  # Append the email to the email list
    
    return name, email # Return the list of names and the list of emails

def main():
    get_team_members()
    team_members = list(zip(name, email)) # Combine the list of names and the list of emails
    random.shuffle(team_members) # Shuffle the list of names
    while True:
        try:
            group_size = int(input("How many people per group for this round of Coffee-Roulette? ")) # Number of people per group
            if group_size > len(name):
                print("The number of people per group is too large. Please try again.")
                raise ValueError # ValueError is a built-in exception that is raised when a function or operation is attempted which is not allowed.           
            elif group_size < 2:
                print("The number of people per group is too small. Please try again.")
                raise ValueError
            else:     
                num_groups = len(name) // group_size # Group size
                with open("CoffeeResults.txt", "w") as file: # Open a text file to write the results
                    for i in range(num_groups): # Loop through the number of groups
                        group = team_members[i *group_size: (i+1)*group_size] # Create a group of people
                        group_names, group_emails = zip(*group) # Unzip the group of people
                        file.write("-" *150 + "\n") # Write a line of dashes to separate the groups
                        file.write("Group {}: {}\n".format(i+1,", ".join(group_names))) # Write the group number and the names of the people in the group
                        file.write("Emails: {}\n".format(", ".join(group_emails))) # Write the emails of the people in the group
                        print("Group {}: {}".format(i+1, ", ".join(group_names))) # Print the group number and the names of the people in the group
                        print("Emails: {}".format(", ".join(group_emails))) # Print the emails of the people in the group
                break
        except ValueError:
            continue

main()
