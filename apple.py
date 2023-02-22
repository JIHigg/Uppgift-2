from time import sleep

weight = 5

while weight > 0:
    print(f'My apple pie weighs {weight}kgs')
    sleep(1)

    print('I eat some of my pie')
    weight -= 1
    
    if weight < 2:
        print('The pie is soon is eaten')
    sleep(2)