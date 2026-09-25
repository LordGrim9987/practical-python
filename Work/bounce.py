# bounce.py
#
# Exercise 1.5

init_height = 100   #initial height from which the ball is dropped in metres
rate_of_bounce = 3/5    #the ball bounces back to 3/5 of the height from which it fell
current_height = init_height

for i in range(10):
    #height in the first bounce
    current_height *= rate_of_bounce
    print(i+1, round(current_height, 4))