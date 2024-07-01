import random
from data import data
from art import logo, vs

print(logo)



def get_random_account():
    choice = random.choice(data)
    return choice


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}: {description}: {country}"


def check_ans(guess,a_followers,b_followers):
    if a_followers > b_followers:
       return guess=="a"
    else:
        return guess==" b"

def game():
    score=0
    account_a = get_random_account()
    account_b = get_random_account()
    game_on=True
    while game_on:
        account_a=account_b
        account_b=get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(f"compare A :{format_data(account_a)}")
        print(vs)
        print(f"against B:{format_data(account_b)}")
        guess=str(input("who has more followers A or B?").lower())
        a_followers = account_a['follower_count']
        b_followers = account_b['follower_count']
        is_ans=check_ans(guess,a_followers,b_followers)

        if is_ans:
            score+=1
            print(f"your guess is right move on! total score:{score}")
        else:
            game_on= False
            print(f"your guess is wrong  total score:{score}")

game()
print("exiting the game")






