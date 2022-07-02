import time
from turtle import Screen

import car_manager
import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

little_t = Player()
car_creator = car_manager.CarManager()
level_system = Scoreboard(-80, 200)

screen.listen()
screen.onkeypress(little_t.move, "Up")

playing = True
while playing:
    time.sleep(0.1)
    screen.update()

    car_creator.make_car()
    car_creator.move_cars()
    for car in car_creator.all_cars:
        if car.distance(little_t) < 20:
            level_system.restart()
            little_t.restart()
            car_creator.speed_restart()

    if little_t.ycor() > 200:
        level_system.level_up()
        car_creator.speed_up()
        little_t.finish()


screen.exitonclick()