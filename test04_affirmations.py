import random

repeat = random.randint(2,5)

variations = [
' with your eyes closed and your heart open.',
' with your eyes unfocused and your mind open.',
' with your eyes unfocused and your heart open.',
' with your eyes closed and your mind open.',
' your eyes closed and your heart open.',
' your eyes unfocused and your mind open.',
' your eyes unfocused and your heart open.',
' your eyes closed and your mind open.',
]

suffix = ' is your daily affirmation. Please slowly repeat it '+str(repeat)+' times to yourself,'
suffix += variations[random.randint(0,7)]

print suffix
