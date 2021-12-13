import random as r
computer=['rock', 'paper', 'scissor']
name=input("Enter Player Name: ")
choice=input("Choose one from three>> rock, paper, scissor:  ")
b=r.choice(computer)
if choice==b:
    print("The result is Draw:",name," choosen",choice,"computer choosen: ",b)
elif choice=='rock' and b=='paper':
    print("You Lose: ",name," choosen",choice,"Computer choosen: ",b)
elif choice=='paper' and b=='rock':
    print("you won, ",name," choosen: ",choice,"Computer choosen: ",b)
elif choice=='paper' and b=='scissor':
    print("you Lose,",name," choosen: ",choice,"Computer choosen: ",b)
elif choice=='scissor' and b=='paper':
    print("you won,",name," choosen: ",choice,"Computer choosen: ",b)
elif choice=='rock' and b=='scissor':
    print("you won, ",name," choosen: ",choice,"Computer choosen: ",b)
elif choice=='scissor' and b=='rock':
    print("you Lose, ",name," choosen: ",choice,"Computer choosen: ",b)
else:
    print(name,"Please choose valid selection Thank you")
    