def Music():
    print('\n STORIES : ')
    print('  1. The Rock Concert')
    print('  2. Jazz Night')
    print('  3. Busking in the Subway')
    story = int(input('\n CHOOSE A STORY : '))
    
    if story == 1:
        The_Rock_Concert()
    elif story == 2:
        Jazz_Night()
    elif story == 3:
        Busking_in_the_Subway()
    else:
        print('Choose again!')
        Music()
        
        
        
def The_Rock_Concert():
    print('\033[4;36m THE ROCK CONCERT : \033[0;0m')
    name1 = input('Write a name :')
    adj1 = input('Write an adjective :')
    band_name = input('Write a band name :')
    adj2 = input('Write an adjective :')
    adj3 = input('Write an adjective :')
    name2 = input('Write a name :')
    adj4 = input('Write an adjective :')
    
    print(f'\033[4;34;43m{name1}\033[0;0m\033[0;30;43m and their friends attended \
a(n) \033[4;34;43m{adj1}\033[0;0m\033[0;30;43m rock concert featuring the \
legendary band, \033[4;34;43m{band_name}\033[0;0m\033[0;30;43m. The atmosphere \
was \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m, with the crowd chanting along \
to the \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m lyrics. During the concert, \
\033[4;34;43m{name2}\033[0;0m\033[0;30;43m even managed to get a(n) \
\033[4;34;43m{adj4}\033[0;0m\033[0;30;43m guitar pick thrown by the lead guitarist.\033[0;0m')



def Jazz_Night():
    print('\033[4;36m JAZZ NIGHT : \033[0;0m')
    name = input('Write a name :')
    adj1 = input('Write a adjective :')
    city = input('Write a city name :')
    adj2 = input('Write a adjective :')
    adj3 = input('Write a adjective :')
    verb = input('Write a verb :')
    adj4 = input('Write a adjective :')
    profession = input('Write a profession :')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m decided to spend their \
evening at a(n) \033[4;34;43m{adj1}\033[0;0m\033[0;30;43m jazz club in \
\033[4;34;43m{city}\033[0;0m\033[0;30;43m. The music was \
\033[4;34;43m{adj2}\033[0;0m\033[0;30;43m, with the band playing \
\033[4;34;43m{adj3}\033[0;0m\033[0;30;43m \
melodies. They even got up to \033[4;34;43m{verb}\033[0;0m\033[0;30;43m with \
a(n) \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m stranger who turned out to be \
a(n) \033[4;34;43m{profession}\033[0;0m\033[0;30;43m by day.\033[0;0m')
    


def Busking_in_the_Subway():
    print('\033[4;36m BUSKING IN THE SUBWAY : \033[0;0m')
    name1 = input('Write a name :')
    adj1 = input('Write a adjective :')
    adj2 = input('Write a adjective :')
    adj3 = input('Write a adjective :')
    adj4 = input('Write a adjective :')
    name2 = input('Write a name :')
    adj5 = input('Write a adjective :')
    adj6 = input('Write a adjective :')
    
    print(f'\033[4;34;43m{name1}\033[0;0m\033[0;30;43m stumbled upon a(n) \
\033[4;34;43m{adj1}\033[0;0m\033[0;30;43m musician performing in the subway \
station. They were playing a(n) \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m \
instrument and drawing a(n) \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m crowd with \
their \033[4;34;43m{adj4}\033[0;0m\033[0;30;43m melodies. \
\033[4;34;43m{name2}\033[0;0m\033[0;30;43m couldn\'t resist joining in, grabbing \
a(n) \033[4;34;43m{adj5}\033[0;0m\033[0;30;43m tambourine and adding to the \
\033[4;34;43m{adj6}\033[0;0m\033[0;30;43m rhythm.\033[0;0m')