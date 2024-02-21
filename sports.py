def Sports():
    print('\n STORIES : ')
    print('  1. The Championship Game')
    print('  2. The Swimming Competition')
    print('  3. The Soccer Tournament')
    story = int(input('\n CHOOSE A STORY : '))
    
    if story == 1:
        The_Championship_Game()
    elif story == 2:
        The_Swimming_Competition()
    elif story == 3:
        The_Soccer_Tournament()
    else:
        print('Choose again!')
        Sports()
        
        

def The_Championship_Game():
    print('\033[4;36m THE CHAMPIONSHIP GAME : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m and their team trained \
tirelessly for the upcoming \033[4;34;43m{adj1}\033[0;0m\033[0;30;43m championship \
game. With \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m determination and teamwork, \
they managed to secure a(n) \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m victory, \
celebrating with a(n) \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m display of \
confetti and cheers from the crowd.\033[0;0m')
    
    
    
def The_Swimming_Competition():
    print('\033[4;36m THE SWIMMING COMPETITION : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m participated in a(n) \
\033[4;34;43m{adj1}\033[0;0m\033[0;30;43m swimming competition at the local pool. \
Despite the \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m competition, they powered \
through the water with \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m strokes and \
emerged victorious, setting a new personal record and earning a(n) \
\033[4;34;43m{adj4}\033[0;0m\033[0;30;43m medal.\033[0;0m')
    
    
    
def The_Soccer_Tournament():
    print('\033[4;36m THE SOCCER TOURNAMENT : \033[0;0m')
    name = input('Write a name : ')
    city = input('Write a city name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m\'s soccer team traveled to \
\033[4;34;43m{city}\033[0;0m\033[0;30;43m to compete in a(n) \033[4;34;43m\
{adj1}\033[0;0m\033[0;30;43m tournament. With their \033[4;34;43m{adj2}\
\033[0;0m\033[0;30;43m footwork and strategic plays, they made it to the finals, \
where they faced off against a(n) \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m \
opponent in a(n) \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m showdown that kept \
spectators on the edge of their seats.\033[0;0m')