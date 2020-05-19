#!/usr/bin/env python

import random


user1_fave = raw_input("User 1: Enter your favorite color: ")
user2_fave = raw_input("User 2: Enter your favorite color: ")

crayons = ["red","blue","green","purple","black","white","pink","yellow"]
#faves = ["red","blue","purple","green","black","pink"]
lucky_color = random.choice(crayons)

if user1_fave in crayons:
    print("User 1: {} is one of our favorites colors.").format(user1_fave)
else:
    print("User 1: {} is not one of favorite colors.").format(user1_fave)

if user2_fave in crayons:
    print("User 2: {} is one of our favorites colors.").format(user2_fave)
else:
    print("User 2: {} is not one of favorite colors.").format(user2_fave)

if lucky_color in user1_fave:
    print("User 1: Your favorite color {} is the same as today's lucky color {}.You win!").format(user1_fave,lucky_color)
elif lucky_color in user2_fave:
    print("User 2: Your favorite color {} is the same as today's lucky color {}. You win!").format(user2_fave,lucky_color)
