import random
import os

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        return
    
   