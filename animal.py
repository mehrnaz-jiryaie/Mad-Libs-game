def Animal():
    print('\n STORIES : ')
    print('  1. The Mischievous Puppy')
    print('  2. The Great Safari Adventure')
    print('  3. The Dolphin Encounter')
    story = int(input('\n CHOOSE A STORY : '))
    
    if story == 1 :
        The_Mischievous_Puppy()
    elif story == 2:
        The_Great_Safari_Adventure()
    elif story == 3:
        The_Dolphin_Encounter()
    else:
        print('Choose again!')
        Animal()
        
        

def The_Mischievous_Puppy():
    print('\033[4;36m THE MISCHIEVOUS PUPPY : \033[0;0m')
    name1 = input('Write a name :')
    adj1 = input('Write an adjective :')
    adj2 = input('Write an adjective :')
    name2 = input('Write a name :')
    adj3 = input('Write an adjective :')
    adj4 = input('Write an adjective :')
    
    print(f'\033[4;34;43m{name1}\033[0;0m\033[0;30;43m witnessed a(n) \
\033[4;34;43m{adj1}\033[0;0m\033[0;30;43m squirrel bravely navigate its way \
through a(n) \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m obstacle course of \
branches and wires to reach a(n) \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m stash \
of nuts. Inspired by the squirrel\'s determination, {name2} decided to tackle \
their own challenges with the same \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m spirit.\033[0;0m')
    
    

def The_Great_Safari_Adventure():
    print('\033[4;36m THE GREAT SAFARI ADVENTURE : \033[0;0m')
    name1 = input('Write a name :')
    adj1 = input('Write an adjective :')
    country = input('Write a country name :')
    adj2 = input('Write an adjective :')
    name2 = input('Write a name :')
    adj3 = input('Write an adjective :')
    
    print(f'\033[4;34;43m{name1}\033[0;0m\033[0;30;43m embarked on a(n) \
\033[4;34;43m{adj1}\033[0;0m\033[0;30;43m safari adventure in \033[4;34;43m\
{country}\033[0;0m\033[0;30;43m where they encountered a variety of \033[4;34;43m\
{adj2}\033[0;0m\033[0;30;43m animals in their natural habitat. From majestic \
lions to playful monkeys, each sighting filled \033[4;34;43m{name2}\
\033[0;0m\033[0;30;43m with a sense of \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m \
wonder and appreciation for the beauty of wildlife.\033[0;0m')
    
    
    
def The_Dolphin_Encounter():
    print('\033[4;36m THE DOLPHIN ENCOUNTER : \033[0;0m')
    destination = input('Write a destination :')
    name = input('Write a name :')
    adj1 = input('Write an adjective :')
    adj2 = input('Write an adjective :')
    adj3 = input('Write an adjective :')
    print(f'\033[0;30;43mWhile on vacation in \033[4;34;43m{destination}, \
{name}\033[0;0m\033[0;30;43m decided to go on a(n) \033[4;34;43m{adj1}\
\033[0;0m\033[0;30;43m dolphin tour. They were thrilled when a pod of \
\033[4;34;43m{adj2}\033[0;0m\033[0;30;43m dolphins swam alongside the boat, \
performing acrobatic tricks and filling the air with their \033[4;34;43m{adj3}\
\033[0;0m\033[0;30;43m clicks and whistles.\033[0;0m')