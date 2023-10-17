import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Cross Game")
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

car.make_car()
screen.listen()
screen.onkey(fun=player.move_up, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.make_car()
    car.car_motion()
    
    for each_car in car.all_cars:
        if each_car.distance(player) < 24.5:
            scoreboard.clear()
            scoreboard.game_over()
            game_is_on = False
            
    if player.is_at_finish_line():
        player.reset_position()
        car.new_level()
        scoreboard.increase_level()
            
screen.exitonclick()