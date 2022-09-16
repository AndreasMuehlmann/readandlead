import sys
import os


def get_actions(path):
    subdirs = [element for element in os.listdir(path) \
            if element != 'story.txt']
    
    return {subdir[0]: subdir for subdir in subdirs}


def print_actions(actions):
    for action in actions.values():
        print(action, end = '  ')


def get_choice(actions):
    while True: 
        choice = input()

        if choice == 'quit':
            sys.exit()

        if not choice:
            print('\nYou at least have to type something.\n')
            continue

        if choice[0] not in actions.keys():
            print('\nThis actions is not available.\n')
            continue

        return choice[0]


def main():
    path = os.path.dirname(__file__)
    path = os.path.join(path, 'Levels')

    print('\n\nREADANDLEAD\n')
    print('Write "quit" to quit the game.')
    print('Type the first letter of the action to decide what to do.\n')

    while True:
        print('\n------------------------------------------------------------\n')
        with open(os.path.join(path, 'story.txt')) as file:
            print(file.read())
        print('------------------------------------------------------------\n')

        
        actions = get_actions(path)
        if len(actions) == 0:
            return

        print('What will you do?')
        print_actions(actions)
        print()

        choice = get_choice(actions)
        path = os.path.join(path, actions[choice])
        

if __name__ == '__main__':
    main()
