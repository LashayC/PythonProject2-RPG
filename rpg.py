#!/usr/bin/env python3
"""RPG Game"""

def showInstructions():
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''House of the Night RPG: The premier of your favoriate show comes on tonight. Turn the power back on in the basement, find the remote, and get the hulu password. Gather in the Living Room to win the game.
    ========
    Commands:
      go [direction]
      get [item]
      use [object]
      show instructions
      show status
      q for quit
    ''')

def describeRoom():
    """Explain """

def showStatus():
    """determine the current status of the player"""
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom)
    print('You can go in the following directions:')
    for direction, room in rooms[currentRoom]['directions'].items():
        print(f"""
        - {direction} to {room}
        """)
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom] and len(rooms[currentRoom]["item"]) > 0:
        print(f'You see a {rooms[currentRoom]["item"]} you can get')
    elif "item" in rooms[currentRoom] and len(rooms[currentRoom]["item"]) == 0:
        print('You\'ve already collected the items in this room')
    # check if theres an object in the room, you can use, if so print it.
    if "use" in rooms[currentRoom] and len(rooms[currentRoom]["item"]) > 0:
        print(f'You see a {rooms[currentRoom]["use"]} you can use')
    elif "use" in rooms[currentRoom] and len(rooms[currentRoom]["use"]) > 0:
        print('You\'ve already collected used the objects in this room')
    # check if theres a monster in the room, you can approach, if so print it.
    if "monster" in rooms[currentRoom] and 'complete' in rooms[currentRoom]['monster']:
        print(f'You see a monster: {rooms[currentRoom]["monster"]}')
    elif "monster" in rooms[currentRoom] and 'complete' not in rooms[currentRoom]['monster']:
        print("You've already defeated this rooms monster")

    print("---------------------------")

def main():
    global currentRoom
    global inventory
    global rooms
    # an inventory, which is initially empty
    inventory = []

    # a dictionary linking a room to other rooms
    ## A dictionary linking a room to other rooms
    rooms = {

                'Upstairs Hall' : {
                    'directions' : {
                        'north' : 'Attic',
                        'northeast' : 'Bathroom',
                        'east' : 'Office',
                        'northwest' : 'Your Bedroom',
                        'west' : 'Master Bedroom',
                        'south' : 'Stairs'
                        }
                    },
                'Attic' : {
                    'directions' : {
                        'south' : 'Upstairs Hall'
                        },
                    'use' : ['lever'], #trapdoor to Downstairs Hall
                    },
                'Your Bedroom' : {
                    'directions' : {
                        'southeast' : 'Upstairs Hall'
                        },
                    },
                'Master Bedroom' : {
                    'directions' : {
                        'east' : 'Upstairs Hall'
                        },
                    'item' : ['bone']
                    },
                'Bathroom' : {
                    'directions' : {
                        'southwest' : 'Upstairs Hall',
                        'south' : 'Mirror Otherside'
                        },
                    'need' : ['riddle answer']
                    },
                'Office' : {
                    'directions': {
                        'west' : 'Upstairs Hall'
                        },
                    'monster' : ['Larry the Undead'], # gives hulu pwd
                    'need' : ['coffee'],
                    },
                'Stairs' : {
                    'directions' : {
                        'north' : 'Upstairs Hall',
                        'south' : 'Living Room'
                        }
                    },
                'Entry Way' : {
                    'directions': {
                        'west' : 'Living Room'
                        }
                    },
                'Living Room' : {
                    'directions' : {
                        'north' : 'Stairs',
                        'east' : 'Entry Way',
                        'west' : 'Downstairs Hall'
                        },
                    'use' : ['tv'],
                    'need' : ['remote', 'power', 'hulu password'],
                    },
                'Downstairs Hall' : {
                    'directions' : {
                        'west' : 'Dining Room',
                        'east' : 'Kitchen',
                        'south' : 'Basement',
                        'east' : 'Living Room'
                        }
                    },
                'Dining Room' : {
                    'directions' : {
                        'east' : 'Downstairs Hall',
                        'south' : 'Kitchen',
                        'north' : 'Backyard'
                        },
                    'item' : ['empty coffee mug']
                    },
                'Kitchen' : {
                    'directions' : {
                        'north' : 'Dining Room'
                        },
                    'use' : ['coffee machine'],
                    'need' : ['power', 'empty coffee mug']
                    },
                'Backyard' : {
                    'directions' : {
                        'south' : 'Dining Room'
                        },
                    'monster' : ['Werewolf'],
                    'need' : ['bone']
                    },
                'Basement' : {
                    'directions' : {
                        'north' : "Downstairs Hall"
                        },
                    'use' : ['power switch'],
                    },
                'Mirror Otherside' : {
                    'directions': {
                        'north' : 'Bathroom'
                        },
                    'item' : ['You found satisfaction of a job well done']
                }
            }

    # start the player in the Hall
    currentRoom = 'Entry Way'

    showInstructions()
    showStatus()
    # breaking this while loop means the game is over
    while True:
        #showStatus()

        # the player MUST type something in
        # otherwise input will keep asking
        move = ''
        
        move = input('>').lower().split(" ", 1)
        
        # while loop and normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]  
        while move[0] != 'q' and move[0] != 'show' and move[0] != 'go' and move[0] != 'get' and move[0] != 'use' and move == '':
            print('Please enter a valid response')
            move = input('>').lower().split(" ", 1)

        # if move == q, quit the game
        if move[0]== 'q':
            print('Game Over')
            break

        #if they type 'show' first
        if move[0] == 'show':
            # if commands
            if move[1] == 'instructions':
                showInstructions()
            # if status
            if move[1] == 'status':
                showStatus()

        #if they type 'go' first
        if move[0] == 'go':
            #check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]["directions"]:
                #set the current room to the new room
                currentRoom = rooms[currentRoom]["directions"][move[1]]
                showStatus()
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')

        #if they type 'get' first
        if move[0] == 'get' :
            # make three checks:
            # 1. if current room has item key but is emptied out
            # 2. if the current room contains an item
            # 3. if the item in the room matches the item the player wishes to get
            if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] == []:
                print('You\'ve already collected everything in this room.')
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                #add the item to their inventory
                inventory.append(move[1])
                #display a helpful message
                print(move[1] + ' got!')
                #delete the item from item list in the room's dictionary
                #del rooms[currentRoom]['item']
                rooms[currentRoom]['item'].remove(move[1])
                #show updated status
                showStatus()
            # if there's no item in the room or the item doesn't match
            else:
                #tell them they can't get it
                print('Can\'t get ' + move[1] + '!')

        #if they type 'use' first
        if move[0] == 'use' :
            # make two checks:
            # 1. if the current room contains something that can be used
            # 2. if the object in use in the room matches the object the player wishes to use
            if 'use' in rooms[currentRoom] and move[1] in rooms[currentRoom]['use']:
                # check if item in room has already been used.
                if 'need' in rooms[currentRoom] and 'complete' in rooms[currentRoom]['need']:
                    print(f'You have already used {move[1]}')

                # use in Attic
                if currentRoom == 'Attic':
                    print('The lever opened a trap door and dropped you into the Downstairs Hall!')
                    currentRoom = 'Downstairs Hall'
                    showStatus()
                
                # use in Kitchen
                if currentRoom == 'Kitchen':
                    # loop through needed items, and move any already inside inventory
                    for needed in rooms[currentRoom]['need']:
                        if needed in inventory:
                            rooms[currentRoom]['need'].remove(needed)
                    # if things are still needed, print out
                    if rooms[currentRoom]['need']:
                        for needed in rooms[currentRoom]['need']:
                            print(f'You need {needed}')
                    # if everything needed 
                    else:
                        print('You acquired a full coffee mug!')
                        inventory.remove('empty coffee mug')
                        inventory.append('full coffee mug')
                        rooms[currentRoom]['need'].append('complete')
                        rooms[currentRoom]['use'].remove(move[1])

                        #show updated status
                        showStatus()

                
                # use in Living Room
                if currentRoom == 'Living Room':
                    # loop through needed items, and move any already inside inventory
                    for needed in rooms[currentRoom]['need']:
                        if needed in inventory:
                            rooms[currentRoom]['need'].remove('needed')
                    # if things are still needed, print out
                    if rooms[currentRoom]['need']:
                        for needed in rooms[currentRoom]['need']:
                            print(f'You need {needed}')
                    # if everything needed 
                    else:
                        print('You finished the game!')
                        rooms[currentRoom]['need'].append('complete')
                        # continue to game winning if statement
                        continue

                # use in Basement
                if currentRoom == 'Basement':
                    print('You flipeed the power switch and turned it on! The power is now up in the house.')
                    #remove the need for power in kitchen and living room
                    rooms['Living Room']['need'].remove('power')
                    rooms['Kitchen']['need'].remove('power')
                    rooms[currentRoom]['use'].remove(move[1])
                    #show updated status
                    showStatus()
            # if there's no item in the room or the item doesn't match
            else:
                #tell them they can't get it
                print('Can\'t use ' + move[1] + '!')

        ## If a player enters a room with a monster

        
        if 'monster' in rooms[currentRoom]:
            # check if item in room has already been used.
            if 'complete' in rooms[currentRoom]['monster']:
                print(f'You have already defeated {rooms[currentRoom]["monster"][0]}')

            # monster in Backyard
            if currentRoom == 'Backyard':
                # check if needed item in inventory
                if 'bone' in inventory:
                    print(f'{rooms[currentRoom]["monster"]} is distracted by a bone. An item is dropped.')
                    inventory.remove('bone')
                    rooms[currentRoom]['monster'].append('complete')
                    rooms[currentRoom]['item'] = ['remote']
                    showStatus()
                else:
                    print('You need a bone for a distraction')

            # monster in Office
            if currentRoom == 'Office':
                # check if needed item in inventory
                if 'full coffee mug' in inventory:
                    print(f'{rooms[currentRoom]["monster"]} is satisfied by coffee. An item is dropped.')
                    inventory.remove('full coffee mug')
                    rooms[currentRoom]['monster'].append('complete')
                    rooms[currentRoom]['item'] = ['hulu password']
                    showStatus()
                else:
                    print('You need to offer a full coffee mug to get the hulu password from Larry the Undead')
    
        ## Define how a player can win
        if currentRoom == 'Living Room' and 'remote' in inventory and 'hulu password' in inventory:
            print('You managed to get everything you need to watch the premier of your favorite show... YOU WIN!')
            break

if __name__ == "__main__":
    main()