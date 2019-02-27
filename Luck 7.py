import random
current_money =15
playing = True
total_roles = 0
top_money = 15
top_roles = 0

while current_money > 0 and playing:
    dice_roll1 = random.randint(1, 6)
    dice_roll2 = random.randint(1, 6)
    print(dice_roll1, dice_roll2)
    role = dice_roll1 + dice_roll2
    if role == 7:
        current_money += 4
        print("You rolled a 7")
        top_roles += 1
        top_money += 4
        top_roles += 1
        if current_money > top_money:
            current_money = top_money
            total_roles = top_roles
    else:
        current_money -= 1
        print("You lose.Roll Again")
        top_roles += 1

print("You lose try again.")
print("You did %d rounds" % top_roles)
print("You have lose %s dollars" % top_money)
