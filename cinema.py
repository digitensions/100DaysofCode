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

def main():
    print("\nHello! welcome to the BFI 'Films of 2019' checker\n")
    print("You can use this script to check whether your favourite film of 2019")
    print("made it to their top 50 and which position the BFI gave it...\n")
    choice()
    retry()
    ranking()
    exit_script()

def choice():
    choose = str(input("Which film do you want to check?: ")).strip().title()
    if choose in films:
        print("\nThe film",choose,"is in the top 50, positioned at number",films[choose][0])
    else:
        print("\nYour film choice doesn't appear in the list, what a shame\n")

def retry():
    try_again = str(input("\nWould you like to try checking another film title? [y/n]: ")).strip().lower()
    if try_again[0] == "n":
        pass
    elif try_again[0] == "y":
        print("Okay, let's run this thing from the top again!")
        choice()
    else:
        print("Please try again answering just with an 'n' or 'y'")
        retry()

def ranking():
    answer = str(input("\nWould you like to see the complete list of films? [y/n]: ")).strip().lower()
    if answer[0] == "y":
        print("\nThe BFI's top 50 films for 2019 and their ranking: \n")
        for i in films:
            print(i,films[i])
    elif answer[0] == "n":
        pass
    else:
        print("Please try again answering just with an 'n' or 'y'")
        ranking()

def exit_script():
    print("\nThanks so much for trying out this BFI 'Film of 2019' checker. Good bye!\n")
    quit()

if __name__ == '__main__':
    main()
