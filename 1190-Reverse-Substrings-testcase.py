import random

def generate_testcases():
    chars = "abcdefghijklmnopqrstuvwxyz"
    randomcharlength = random.randint(1,2000)
    randomParenthesis = random.randint(1,2000-randomcharlength)

    if randomParenthesis % 2 == 1:
        randomParenthesis -= 1
    openedUse = randomParenthesis//2
    closeUse = randomParenthesis//2
    arr1 = []
    while randomcharlength > 0 or randomParenthesis > 0:
        perform = random.randint(0, 2)
        if perform == 0 and randomcharlength:
            arr1.append(random.choice(chars))
            randomcharlength -= 1
        if perform == 1 and randomParenthesis and openedUse > 0:
            arr1.append('(')
            randomParenthesis -= 1
            openedUse -= 1
        if perform == 2 and randomParenthesis and openedUse < closeUse:
            arr1.append(')')
            randomParenthesis -= 1
            closeUse -= 1
    return "".join(arr1)

for i in range(8):
    print(f'{i+1}',generate_testcases())