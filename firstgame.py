game_start_yes = "yes"
game_start_no = "no"
name = input("What is your name? ")

print(" ")

game_start = input("Would you like to start the game, yes or no? ")

print(" ")

if game_start == game_start_yes:
  print(f"Welcome {name} lets start the game")
elif game_start == game_start_no:
  print(f"Okay {name} maybe we will play next time. Have a nice day!")
  exit()
else:
  print("ANSWER THE QUESTIONS CORRECTLY! USE THE OPTIONS GIVEN. GAME TERMINATED!")
  exit()
  
print(" ")

answer_1_left = "left"
answer_1_right = "right"
question_1 = input("You are at a split in the road. Will you go left or right? ")

print(" ")

if question_1 == answer_1_left:
  print(f"You fell in a pit and died {name} game over!")
elif question_1 == answer_1_right:
  print(f"You found a path to the castle {name}")
else:
  print("ANSWER THE QUESTIONS CORRECTLY! USE THE OPTIONS GIVEN. GAME TERMINATED!")
  exit()
  
print(" ")

answer_2_red = "red"
answer_2_blue = "blue"
answer_2_green = "green"
question_2 = input("You find a mystical key and hear a voice tell you, that this key can open three chests, but you can only open one chest with it before the key disappears. You see a red, blue and green treasure chest. Which one do you open? ")

print(" ")

if question_2 == answer_2_red:
  print(f"You aquired the sword of Barzabal!")
elif question_2 == answer_2_blue:
  print(f"You aquired the armour of Golbezul!")
elif question_2 == answer_2_green:
  print(f"You aquired the bow of Alial!")
else:
  print("ANSWER THE QUESTIONS CORRECTLY! USE THE OPTIONS GIVEN. GAME TERMINATED!")

print(" ")

answer_3_a = "a"
answer_3_b = "b"
answer_3_c = "c"
answer_3_d = "d"
question_3 = input("After opening the chest, two goblins rushed you from behind. The first one has a mace and the other one has a poisoned dagger. Do you a) Attack the first goblin? b) Dodge the first goblin and attack the second? c) Try to dodge both goblins d) Run away ")

print(" ")

#The following are answers based on previously picking the sword

if question_3 == answer_3_a and question_2 == answer_2_red:
  print(f"You pulled out the sword of Barzabal and stabbed the first goblin through the heart, instantly killing him. But before you could react, the second goblin threw his poisoned dagger at you grazing your arm. You managed to pull your sword out of your first attacker and behead your second one. {name} is poisoned! ")
elif question_3 == answer_3_b and question_2 == answer_2_red:
  print(f"You quickly dodge the incoming mace that was aimed at your head by rolling forward. Mid roll you pulled out the sword of Barzabal and hurrled it at your second attacker. The sword impaled the goblin through the head before he could throw his dagger. But before you could retrieve your sword the first goblin struck you with his mace on your arm, opening up a deep wound. Before he could strike you again you managed to pull out the sword, cleaving both his legs off in one swing and aiming you sword at his heart as he fell onto it and died. {name} is wounded! ")
elif question_3 == answer_3_c and question_2 == answer_2_red:
  print(f"You quickly dodged your first attacker by jumping to your left, but sadly your second attacker threw his dagger right in your path. It struck you right in your upper thigh causing you to flinch. The first goblin then landed a death blow to your skull with his mace. {name} is dead! ")
elif question_3 == answer_3_d and question_2 == answer_2_red:
  print(f"You scream loudly out of fear and started to run. The first goblin gave chase. You were faster, but not faster than the dagger the second goblin hurled in your direction. The dagger struck home, landing in your neck and slicing open your jugular vein. You lay there dying, your last moments to be lived as a coward. {name} is dead! ")
else:
  print("ANSWER THE QUESTIONS CORRECTLY! USE THE OPTIONS GIVEN. GAME TERMINATED!")

print(" ")