import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

timmy = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(timmy.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with a car
    for car in car_manager.all_cars:
        if car.distance(timmy) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Reach next level
    if timmy.ycor() > 270:
        scoreboard.level_up()
        timmy.go_to_start()
        car_manager.speed_up()


screen.exitonclick()
