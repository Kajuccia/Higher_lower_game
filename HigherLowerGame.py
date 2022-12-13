import random

from HigherLowerdata import data
from art import logo, vs

def printing(compare, A):
    print(f"compare {A} : {compare['name']}, a {compare['description']}, from {compare['country']}")

def followers(compare):
    return int(compare['follower_count'])

def random_number():
    return random.choice(data)

def game():
    score = 0
    game_over = False
    compareA = random_number()
    compareB = random_number()
    print(logo)
    printing(compareA, 'A')
    print(vs)
    printing(compareB, 'B')
    guess = input("Who has more followers? A or B?")
    compareAfollowers = followers(compareA)
    compareBfollowers = followers(compareB)

    if compareBfollowers > compareAfollowers:
        win = 'b'
    else:
        win = 'a'
    if guess == win:
        score += 1
        print('You won!')
        print(f" Compare A has: {compareAfollowers} followers")
        print(f" Compare B has: {compareBfollowers} followers")
        print(f"your score is {score}")

    else:
        print('You loose!')
        print(f" Compare A has: {compareAfollowers} followers")
        print(f" Compare B has: {compareBfollowers} followers")
        print (f"Your score is {score}")
        game_over = True
    while game_over is False:
        print(logo)
        compareA = compareB
        printing(compareA, 'A')
        compareAfollowers = followers(compareA)
        print(vs)
        compareB = random.choice(data)
        printing(compareB, 'B')
        guess = input("Who has more followers? A or B?")
        compareBfollowers = followers(compareB)
        compareAfollowers = followers(compareA)
        if compareBfollowers > compareAfollowers:
            win = 'b'
        else:
            win = 'a'
        if guess == win:
            score += 1
            print('You won!')
            print(f" Compare A has: {compareAfollowers} followers")
            print(f" Compare B has: {compareBfollowers} followers")
            print(f"Your score is {score}")
        else:
            print('You loose!')
            print(f" Compare A has: {compareAfollowers} followers")
            print(f" Compare B has: {compareBfollowers} followers")
            print(f"Your score is {score}")
            game_over = True


game()