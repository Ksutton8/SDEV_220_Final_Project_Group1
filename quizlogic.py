

rap_hiphop = 0
indie_alt = 0
rb = 0
pop = 0
rock = 0


#question 1
print('1. When do you typically listen to music?')
print(' A. While working out/exercising')
print(' B. While relaxing at home')
print(' C. While studying or doing homework')
print(' D. At social gatherings or parties')

answer = input('Enter your answer: ')

if answer == 'A':
    rap_hiphop += 2
    rock += 2
    pop += 2
elif answer == 'B':
    indie_alt += 2
    rb += 2
elif answer == 'C':
    indie_alt += 2
    rb += 2
elif answer == 'D':
    rap_hiphop += 2
    pop += 2
else:
    print('Please enter A, B, C, or D')


#question 2
print('2. What genre of music are you most drawn too?')
print('  A. Pop')
print('  B. Rap/Hip-Hop')
print('  C. Alternative/Indie')
print('  D. R&B')
print('  E. Alternative/Rock')

answer = input('Enter your answer: ')

if answer == 'A':
    pop +=3
elif answer == 'B':
    rap_hiphop += 3
elif answer == 'C':
    indie_alt += 3
elif answer == 'D':
    rb += 3
elif answer == 'E':
    rock += 3
else:
    print('Please enter A, B, C, D, or E')


#question 3
print('3. What moods do you typically associate with music?')
print(' A. Introspective/Reflective')
print(' B. Sad/Melancholic')
print(' C. Energetic/Upbeat')
print(' D. Sensual/Romantic')
print(' E. Angst/Rebellious')
print(' F. Confidence/Empowerment')

answer = input('Enter your answer: ')

if answer == 'A':
    indie_alt += 1
elif answer == 'B':
    indie_alt += 1
elif answer == 'C':
    pop += 1
elif answer == 'D':
    rb += 1
elif answer == 'E':
    rock += 1
elif answer == 'F':
    rap_hiphop += 1
else:
    print('Please enter A, B, C, D, E, or F')

#question 4
print('4. Do you resonate more with the lyrics or the beat of a song?')
print(' A. I primarily focus on the lyrics and their meaning.')
print(' B. I pay more attention to the beat and rhythm of music.')

answer = input('Enter your answer: ')

if answer == 'A':
    indie_alt += 2
    rb += 2
elif answer == 'B':
    pop += 2
    rock += 2
    rap_hiphop += 2
else:
    print('Please enter A or B')


#question 5
print('5. Which artists or bands do you enjoy listening to the most?')
print(' A. Mitski / Hozier / Lana Del Rey')
print(' B. BTS / Beyonce / Lady Gaga')
print(' C. Megan Thee Stallion / J.Cole / Drake')
print(' D. Fall Out Boy / Paramore / Arctic Monkeys')
print(' E. SZA / Brent Faiyaz / Frank Ocean')

answer = input('Enter your answer: ')

if answer == 'A':
    indie_alt += 3
elif answer == 'B':
    pop += 3
elif answer == 'C':
    rap_hiphop += 3
elif answer == 'D':
    rock += 3
elif answer == 'E':
    rb += 3
else:
    print('Please enter A, B, C, D, or E')


genre_score = max(indie_alt, pop, rap_hiphop, rock, rb)

if indie_alt == genre_score:
    print('We think you\'ll love these artists:  ') # enter indie artists

if rock == genre_score:
    print('We think you\'ll love these artists:  ') # enter rock artists

if pop == genre_score:
    print('We think you\'ll love these artists:  ') # enter pop artists

if rb == genre_score:
    print('We think you\'ll love these artists:  ') # enter r&b artists

if rap_hiphop == genre_score:
    print('We think you\'ll love these artists:  ') # enter rap/hiphop artists




  








