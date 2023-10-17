from turtle import Turtle
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-290, 260)
        self.write(f"level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", align="left", font=FONT)
            
    def game_over(self):
        self.goto(-60, 0)
        self.write(f"GAME OVER", align="left", font=FONT)
        self.goto(-140, -30)
        self.write(f"Your final score is: {self.level}", align="left", font=FONT)
        
