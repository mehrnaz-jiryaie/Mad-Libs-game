def Holidays():
    print('\n STORIES : ')
    print('  1. The Festive Feast')
    print('  2. The Winter Wonderland')
    print('  3. The Cultural Celebration')
    story = int(input('\n CHOOSE A STORY : '))
    
    if story == 1:
        The_Festive_Feast()
    elif story == 2:
        The_Winter_Wonderland()
    elif story == 3:
        The_Cultural_Celebration()
    else:
        print('Choose again!')
        Holidays()



def The_Festive_Feast():
    print('\033[4;36m THE FESTIVE FEAST : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    adj2 = input('Write an adjective : ')
    adj3 = input('Write an adjective : ')
    food1 = input('Write a food name : ')
    food2 = input('Write a food name : ')
    adj4 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m hosted a(n) \033[4;34;43m\
{adj1}\033[0;0m\033[0;30;43m holiday feast for their friends and family. The \
table was adorned with \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m decorations and \
filled with a(n) \033[4;34;43m{adj3}\033[0;0m\033[0;30;43m spread of traditional \
dishes, from roasted \033[4;34;43m{food1}\033[0;0m\033[0;30;43m to decadent \
\033[4;34;43m{food2}\033[0;0m\033[0;30;43m, creating a warm and \033[4;34;43m\
{adj4}\033[0;0m\033[0;30;43m atmosphere of joy and gratitude.\033[0;0m')

    
    
    
def The_Winter_Wonderland():
    print('\033[4;36m THE WINTER WONDERLAND : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    destination = input('Write a destination : ')
    adj2 = input('Write an adjective : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    adj5 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m visited a(n) \033[4;34;43m\
{adj1}\033[0;0m\033[0;30;43m winter wonderland in \033[4;34;43m{destination}\
\033[0;0m\033[0;30;43m, where they enjoyed activities like ice skating, building \
\033[4;34;43m{adj2}\033[0;0m\033[0;30;43m snowmen, and sipping on \033[4;34;43m\
{adj3}\033[0;0m\033[0;30;43m hot cocoa by the fire. The twinkling lights and \
\033[4;34;43m{adj4}\033[0;0m\033[0;30;43m snowfall created a magical ambiance \
that made it feel like a(n) \033[4;34;43m{adj5}\033[0;0m\033[0;30;43m fairy tale \
come to life.\033[0;0m')
    
    
    
def The_Cultural_Celebration():
    print('\033[4;36m THE CULTURAL CELEBRATION : \033[0;0m')
    name = input('Write a name : ')
    adj1 = input('Write an adjective : ')
    city = input('Write a city name : ')
    adj2 = input('Write an adjective : ')
    adj3 = input('Write an adjective : ')
    adj4 = input('Write an adjective : ')
    adj5 = input('Write an adjective : ')
    
    print(f'\033[4;34;43m{name}\033[0;0m\033[0;30;43m attended a(n) \033[4;34;43m\
{adj1}\033[0;0m\033[0;30;43m cultural celebration in {city}\033[0;0m\033[0;30;43m\
, immersing themselves in the \033[4;34;43m{adj2}\033[0;0m\033[0;30;43m traditions \
and customs of the local community. From colorful parades to \033[4;34;43m{adj3}\
\033[0;0m\033[0;30;43m performances, they embraced the spirit of \033[4;34;43m\
{adj4}\033[0;0m\033[0;30;43m unity and diversity that made the holiday so \
\033[4;34;43m{adj5}\033[0;0m\033[0;30;43m special.\033[0;0m')