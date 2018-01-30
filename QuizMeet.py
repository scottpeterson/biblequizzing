#!/usr/bin/env python3

import textwrap


storage = {'date' : 'Friday, February 9 - Saturday, February 10, 2018',
            'meet' : 'District Meet #4', 
            'location' : 'Lighthouse Christian Center',
            'address' : '3409 23rd St. S.W. Puyallup, WA 98373',
            'churches' : 9,
            'teams' : 25,
            'prelims' : 6,
            'rooms' : 4,
            'stats' : 'Lilly Peterson, (working remotely)',
            'lunch' : 'Yes',
            'mtg': 'Yes',
            'mtg_room' : 'Quiz Room #2, Lighthouse Room #9',
            'meet director' : 'Scott Peterson',
            'twitter' : '@PNWQuizzing',
            'tw_pod' : '@InsideQuizzing',
            'email_pod' : 'iq@cbqz.org',
            'insta' : '@pnw_biblequizzing',
                }
quizmasters = { 'q1' : 'Scott Peterson',
                'q2' : 'Abby Ashcraft',
                'q3' : 'Gryphon Shafer',
                'q4' : 'Cutty Welt'
                   }

scorekeepers = {'sk1' : 'TBA',
                'sk2' : 'TBA',
                'sk3' : 'TBA',
                'sk4' : 'TBA'
                }

answer_judges = {   'aj1' : 'None',
                    'aj2' : 'None',
                    'aj3' : 'None',
                    'aj4' : 'None'
                }

notes = {   'note1' : '+ All score sheets should be brought by the winning team to Quiz Room 1 to Scott and placed on the printer.',
            'note2' : '+ Due to technical difficulties, there will not be a scoreboard in Room 1 for the majority of the meet, and maybe not for all of it.',
            'note3' : '+ If it all works out, Year-To-Date Team and Individual stats will be projected in Room 1 following awards',
            'note4' : '+ For our leaders and officials, **please plan to come to the leadership meeting during lunch on Saturday.** We will be talking extensively about end of the year things: Meet 5 happenings, District Championships details, Great West information, Internationals information, volunteers and/or coaches for GWI and Internationals and so much more.'
            }

def update_data():
    print('I\'m a quick program that will prompt you for information for the upcoming quiz meet, and update that information in the database.')
    print('\n')
    
    # Room 1 Quizmaster
    q1 = input('The quizmaster for Room 1 is currently set to: {}. Would you like to change it?'.format(quizmasters['q1']))
    q1 = q1.upper()
    if q1 == "NO":
        pass
    else:
        q1 = input('Who will be the quizmaster for Room 1?')
        quizmasters['q1'] = q1

# ideally I'd like to create a loop here for each quiz room....not sure how to do it...I have a lot of hardcoded info in my printed info to the end user

# when running update_data() in ipython, it changes the dictionary value for 'q1' THERE, but not in my actual file....





def email_message():

    print('''Below is all the information you could ever want for the upcoming quiz meet.
    
#Meet Documents Attached:
+ {} Meet Schedule.xlsx (change the dropdown to select your team name and all your team's prelims will be highlighted)
+ {} Meet Schedule.pdf
+ {} Roster.xlsx (*for Gryphon!!*)
+ {} Roster.pdf

+ the documents are also linked on the website (www.pnwquizzing.com).  
+ Just the Roster for now. 
+ The others will be linked the day of the quiz meet. 

#Entering and Leaving Quiz Rooms
+ Please enter and leave quiz rooms **only between quizzes**.  (we all did poorly on this at the last quiz meet)
+ If you absolutely must enter during a quiz, it *must be between questions*, and not while a quizzer is answering.  
+ Please hold each other accountable for this!   

#Backup Acme Equipment
+ If you have Acme quiz equipment, please label it and bring it as a backup for the district's Acme quiz equipment.  

*Please let me know if anything looks amiss or if you have any questions.* 
*It's much easier for me to fix any errors far in advance of the meet.* 
                 '''.format(storage['meet'], storage['meet'], storage['meet'], storage['meet']))

    print('#MEET DATE, LOCATION, ADDRESS')
    print('+ {} will occur on {} and will be held at {} which is located at {} '.format(storage['meet'], storage['date'], storage['location'], storage['address']))
    print('\n\n')
    print('#LUNCH INFORMATION')
    if storage['lunch'] == 'No':
        print('+ There will be no lunch provided at the church.')
    else:
        print('+ There will be lunch provided at the church.')
    print('\n')
    print('#LEADERSHIP MEETING')
    if storage['mtg'] == 'No':
        print('+ There will be no leadership meeting during lunch.')
    else:
        print('+ There will be a leadership meting during lunch in {}'.format(storage['mtg_room']))
    print('\n')
    print('#MISCELLANEOUS INFORMATION')
    for value in notes.values():
        print(value, '\n')
    print('#QUIZ MEET COMPETITION INFORMATION')
    print('+ There are {} churches participating in {}.'.format(storage['churches'], storage['meet']))
    print('+ There are {} teams participating in {}.'.format(storage['teams'], storage['meet']))
    print('+ Each team will have {} preliminary quizzes.'.format(storage['prelims']))
    print('+ These preliminary quizzes will occur across {} quiz rooms.'.format(storage['rooms']))
    print('\n')
    print('#OFFICIALS')
    print('##QUIZMASTERS')
    print('The quizmasters for each quiz room are: \n')
    for key, value in quizmasters.items():
        print('+ {}: {}'.format(key, value))
    print('\n')
    print('##ANSWER JUDGES')
    print('The scorekeepers for each quiz room are: \n')
    for key, value in scorekeepers.items():
        print('+ {}: {}'.format(key, value))
    print('\n')
    print('##SCOREKEEPERS')
    print('The answer judges for each quiz room are: \n')
    for key, value in answer_judges.items():
        print('+ {}: {}'.format(key, value))
    print('\n')
    print('##STATISTICIAN')
    print('The statistician for the meet is: {}'.format(storage['stats']))
    print('\n')
    print('##MEET DIRECTOR')
    print('The meet director is: {}'.format(storage['meet director']))
    print('\n')
    print('##SOCIAL MEDIA')
    print('+ The new podcast for quizzing is live! Search "Inside Quizzing iTunes" and you\'ll find it!')
    print('+ The email address of the podcast is {}.  You can email questions and feedback'.format(storage['email_pod']))
    print('+ The Twitter account of the podcast is {}.'.format(storage['tw_pod']))
    print('+ Pacific Northwest Bible Quizzing\'s Twitter account is {}'.format(storage['twitter']))
    print('+ Pacific Northwest Bible Quizzing\'s Instagram account is {}'.format(storage['insta']))


# # Ideas for future development
# Write another separate program that prompts a user for all the inputs
