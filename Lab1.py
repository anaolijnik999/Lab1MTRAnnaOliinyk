def utility1(r, homeR, picnicR):
    return (float(r) * int(homeR) + ((1 - float(r)) * int(picnicR)))

def utility2(r, homeS, picnicS):
    return (float(r) * int(homeS) + ((1 - float(r)) * int(picnicS)))


print("Is it worth going for a picnic?")

print("enter the probability of rain (between 0 and 1): ")
rain = input()
print("enter a rating of how it feels to be at home in the rain (between 1 and 10): ")
homeR = input()
print("enter a rating of how it feels to be at a picnic in the rain (between 1 and 10): ")
picnicR = input()
print("Rate how you feel when you are at home in sunny weather. (between 1 and 10): ")
homeS = input()
print("Rate how you feel when you are at a picnic in sunny weather. (between 1 and 10): ")
picnicS = input()

u1 = utility1(rain, homeR, picnicR)
u2 = utility2(rain, homeS, picnicS)

if u1 > u2:
    print("You should stay home.")
else:
    print("You should go for a picnic.")

print("The utility of staying home is: ", u1)
print("The utility of going for a picnic is: ", u2)