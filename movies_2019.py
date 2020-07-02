#!/usr/bin/env python3

'''
Learning script that references a dictionary of films to see if user input film made it to the BFI's top 50 list.
Asks you to enter a film you'd like to check, then lists the item and it's rank if successful.
If not, asks if you'd like to see the complete list.
Asks finally if you'd like to restart the process by checking another title or not.
'''

films = {
    "The Mule": [50],
    "The Favourite": [49],
    "Just Don't Think I'll Scream": [48],
    "If Beale Street Could Talk": [47],
    "If Rose Plays Julie": [46],
    "Rocks": [45],
    "Honeyland": [44],
    "Holiday": [43],
    "I Lost My Body": [42],
    "Hale County This Morning, This Evening": [41],
    "Ray and Liz": [40],
    "Joker": [39],
    "Eigth Grade": [38],
    "No Data Plan": [37],
    "America": [36],
    "Zombi Child": [35],
    "Synonyms": [34],
    "Ash Is Purest White": [33],
    "Booksmart": [32],
    "Knives Out": [31],
    "In Fabric": [30],
    "I Was at Home, But...": [29],
    "Varda by Agnès": [28],
    "Ad Astra": [27],
    "The Hottest August": [26],
    "The Farewell": [25],
    "A Hidden Life": [24],
    "Transit": [23],
    "Border": [22],
    "Beanpole": [21],
    "Martin Eden": [20],
    "Hustlers": [19],
    "Happy as Lazzaro": [18],
    "The Lighthouse": [17],
    "Midsommar": [16],
    "For Sama": [15],
    "Marriage Story": [14],
    "Monos": [13],
    "Uncut Gems": [12],
    "High Life": [11],
    "Vitalina Varela": [10],
    "Us": [9],
    "Bait": [8],
    "Atlantics": [7],
    "Pain and Glory": [6],
    "Portrait of a Lady on Fire": [5],
    "Once Upon a Time... in Hollywood": [4],
    "The Irishman": [3],
    "Parasite": [2],
    "The Souvenir": [1]
}

exit_command = True
def main():
    # Welcome / intro statements
    print("\nHello! welcome to the BFI 'Films of 2019' checker\n")
    print("You can use this script to check whether your favourite film of 2019")
    print("made it to their top 50 and which position the BFI gave it...\n")
    # This is the first question asked of the user using string input, and puts it in choice variable
    # Uses .strip() to removes leading and trailing characters and .title() to alphabetize the first letter, matching dictionary
    choice = str(input("Which film do you want to check?: ")).strip().title()
    if choice in films:
        print("\nThe film",choice,"is in the top 50, positioned at number",films[choice][0])
    else:
        print("\nYour film choice doesn't appear in the list, what a shame :(\n")
    
    # This next variable input asks if you'd like to view the complete dictionary
    answer = str(input("\nWould you like to see the complete list of films? [y/n]: ")).strip().lower()
    if answer[0] == "y":
        print("\nThe BFI's top 50 films for 2019 and their ranking: \n")
        for i in films:
            print(i,films[i])
    elif answer[0] == "n":
        print("\nOkay!")
    else:
        print("I'm afraid you didn't give a valid answer. Let's start over!")
        
    # Final question asks if the user would like to try another films (probably pointless if they've seen the list!)
    try_again = str(input("\nWould you like to try checking another film title? [y/n]: ")).strip().lower()
    if try_again[0] == "n":
        print("\nThank you so much for trying this BFI 'Film of 2019' checker. Good bye!\n")
        quit()
    elif try_again[0] == "y":
        print("\nOkay, let's try again! Good luck :)\n********************************************************")
    else:
        print("I'm afraid you didn't give a valid answer. Let's start over!")        

# calls a loop that returns back to the start of main() unless "n" activates quit() above
while exit_command:
    main()
