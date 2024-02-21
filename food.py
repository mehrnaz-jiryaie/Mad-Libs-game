def Food():
    print('\n STORIES : ')
    print('  1. Cooking Disaster')
    print('  2. Street Food Adventure')
    print('  3. Family Feast')
    story = int(input('\n CHOOSE A STORY : '))
    
    if story == 1:
        Cooking_Disaster()
    elif story == 2:
        Street_Food_Adventure()
    elif story == 3:
        Family_Feast()
    else:
        print('Choose again!')
        Food()
        


def Cooking_Disaster():
    print('\033[4;36m COOKING DISASTER : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    ingredient = input('Write an ingredient : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m attempted to make a(n) \
\033[4;34;43m{adj1}\033[0;0m\033[0;30;43m meal for their friends, but it turned \
into a(n) \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m disaster. They accidentally \
added too much \033[4;34;43m{ingredient}\033[0;0m\033[0;30;43m, causing the dish \
to become overly \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m. Despite the mishap, \
everyone had a good laugh and ended up ordering \
\033[4;34;43m{adj4}\033[0;0m\033[0;30;43m pizza instead.\033[0;0m')
    
    
    
def Street_Food_Adventure():
    print('\033[4;36m STREET FOOD ADVENTURE : \033[0;0m')
    city = input('Write a city name : ')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    food1 = input('Write a food name : ')
    food2 = input('Write a food name : ')
    adj3 = input('Write an adjective : ')
    food3 = input('Write a food name : ')
    
    print(f'\033[0;30;43mWhile exploring the bustling streets of \
\033[4;34;43m{city}, {name}\033[0;0m\033[0;30;43m \
stumbled upon a(n) \033[4;34;43m{adj1}\033[0;0m\033[0;30;43m food market. \
They tried a variety of \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m street foods,\
including \033[4;34;43m{food1}\033[0;0m\033[0;30;43m and \
\033[4;34;43m{food2}\033[0;0m\033[0;30;43m, each bursting with \
\033[4;34;43m{adj3}\033[0;0m\033[0;30;43m flavors. \
Their favorite was a spicy \033[4;34;43m{food2}\033[0;0m\033[0;30;43m that left \
their mouth tingling for hours.\033[0;0m')
    
    
    
def Family_Feast():
    print('\033[4;36m FAMILY FEAST : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    animal = input('Write an animal name : ')
    food = input('Write a food name : ')
    adj3 = input('Write an adjective : ')
    
    print(f'\033[0;30;43mFor the holidays, \033[4;34;43m{name} \
\033[0;0m\033[0;30;43m gathered with their family for a(n) \
\033[4;34;43m{adj1}\033[0;0m\033[0;30;43m feast. The table was filled with a(n) \
\033[4;34;43m{adj2}\033[0;0m\033[0;30;43m array of dishes, from roasted \
\033[4;34;43m{animal}\033[0;0m\033[0;30;43m to creamy \033[4;34;43m{food} \
\033[0;0m\033[0;30;43m. Everyone shared stories and laughter as they indulged \
in the \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m meal, creating memories that would \
last a lifetime.\033[0;0m')