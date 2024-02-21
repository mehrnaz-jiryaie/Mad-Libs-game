def Travel():
    print('\n STORIES : ')
    print('  1. Lost in the Jungle')
    print('  2. Misadventures in Paris')
    print('  3. Cross-Country Road Trip')
    story = int(input('\n CHOOSE A STORY : \n'))
    
    if story == 1:
        Lost_in_the_Jungle()
    elif story == 2:
        Misadventures_in_Paris()
    elif story == 3:
        Cross_Country_Road_Trip()
    else:
        print('Choose again!')
        Travel()
        
        
def Lost_in_the_Jungle():
    print('\033[4;36m LOST IN THE JUNGLE : \033[0;0m')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    plc = input('Write a place name : ')
    name = input('Write a name : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    adj5 = input('Write an adjective : ')
    noun = input('Write a plural noun :')
    adj6 = input('Write an adjective :')
    
    print(f'\033[0;30;43m While on a(n) \033[4;34;43m{adj1}\033[0;0m\033[0;30;43m \
adventure through the \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m jungles of \
\033[4;34;43m{plc}, {name}\033[0;0m\033[0;30;43m stumbled upon a(n) \
\033[4;34;43m{adj3}\033[0;0m\033[0;30;43m temple hidden deep within the foliage.\
Inside, they found a(n) \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m artifact that \
transported them to a(n) \033[4;34;43m{adj5}\033[0;0m\033[0;30;43m dimension \
where they encountered \033[4;34;43m{noun}\033[0;0m\033[0;30;43m who spoke in \
\033[4;34;43m{adj6}\033[0;0m\033[0;30;43m tones.\033[0;0m')
    

    
def Misadventures_in_Paris():
    print('\033[4;36m MISADVENTURES IN PARIS : \033[0;0m')
    city = input('Write a city name :')
    name = input('Write a name :')
    adj1 = input('Write an adjective :')
    adj2 = input('Write an adjective :')
    food = input('Write a food name :')
    adj3 = input('Write an adjective :')
    adj4 = input('Write an adjective :')
    animal = input('Write an animal name :')

    print(f'\033[0;30;43mDuring their trip to \033[4;34;43m{city}, {name}\033[0;0m\033[0;30;43m\
 decided to explore the city\'s \033[4;34;43m{adj1}\033[0;0m\033[0;30;43m streets.\
They stumbled upon a(n) \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m cafe where they \
tried the local specialty, \033[4;34;43m{food}\033[0;0m\033[0;30;43m. Later, \
they got lost in the \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m alleyways of \
Montmartre and ended up having a(n)\033[4;34;43m{adj4}\033[0;0m\033[0;30;43m\
 encounter with a street performer dressed as a(n) \033[4;34;43m{animal}.\033[0;0m')
        
    
    
def Cross_Country_Road_Trip():
    print('\033[4;36m CROSS COUNTRY ROAD TRIP : \033[0;0m')
    name = input('Write a name :')
    adj1 = input('Write an adjective :')
    country = input('Write a country name :')
    adj2 = input('Write an adjective :')
    food = input('Write a food name :')
    adj3 = input('Write an adjective :')
    adj4 = input('Write an adjective :')
    animal = input('Write an animal name :')
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m and their friends embarked \
on a(n) \033[4;43;34m{adj1}\033[0;0m\033[0;30;43m road trip across \
\033[4;34;43m{country}\033[0;0m\033[0;30;43m. Along the way, they stopped at \
a(n) \033[4;43;34m{adj2}\033[0;0m\033[0;30;43m roadside diner where they tried \
the famous \033[4;34;43m{food}\033[0;0m\033[0;30;43m. They also visited a(n) \
\033[4;34;43m{adj3}\033[0;0m\033[0;30;43m national park where they encountered \
a(n) \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m wildlife including \
\033[4;34;43m{animal}\033[0;0m\033[0;30;43m roaming freely.\033[0;0m')
    