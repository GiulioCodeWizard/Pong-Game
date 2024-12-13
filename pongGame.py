"""
Dajani Giulio
Pong Game in .py
"""

import turtle as t


def main():
    player_A_score = 0
    player_B_score = 0

    window = t.Screen()
    window.title('Pong Game')
    window.bgcolor('green')
    window.setup(width=800, height=600)
    window.tracer(0)

    left_paddle = t.Turtle()
    left_paddle.speed(0)
    left_paddle.shape('square')
    left_paddle.color('white')
    left_paddle.shapesize(stretch_wid=5, stretch_len=1)
    left_paddle.penup()
    left_paddle.goto(-350, 0)

    right_paddle = t.Turtle()
    right_paddle.speed(0)
    right_paddle.shape('square')
    right_paddle.color('white')
    right_paddle.shapesize(stretch_wid=5, stretch_len=1)
    right_paddle.penup()
    right_paddle.goto(350, 0)

    ball = t.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('red')
    ball.penup()
    ball.goto(0, 0)
    ball_x_direction = 0.2
    ball_y_direction = 0.2

    pen = t.Turtle()
    pen.speed(0)
    pen.color('blue')
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0    Player B: 0", align='center', font=('Arial', 24, 'normal'))


    def left_paddle_up():
        y = left_paddle.ycor()
        if y < 250:  # Ensure paddle stays in bounds
            left_paddle.sety(y + 20)


    def left_paddle_down():
        y = left_paddle.ycor()
        if y > -250:
            left_paddle.sety(y - 20)


    def right_paddle_up():
        y = right_paddle.ycor()
        if y < 250:
            right_paddle.sety(y + 20)


    def right_paddle_down():
        y = right_paddle.ycor()
        if y > -250:
            right_paddle.sety(y - 20)


    window.listen()
    window.onkeypress(left_paddle_up, 'w')
    window.onkeypress(left_paddle_down, 's')
    window.onkeypress(right_paddle_up, 'Up')
    window.onkeypress(right_paddle_down, 'Down')

    while True:
        window.update()

        ball.setx(ball.xcor() + ball_x_direction)
        ball.sety(ball.ycor() + ball_y_direction)

        if ball.ycor() > 290 or ball.ycor() < -290:
            ball_y_direction *= -1

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball_x_direction *= -1
            player_A_score += 1
            pen.clear()
            pen.write(f"Player A: {player_A_score}    Player B: {player_B_score}", align='center', font=('Arial',
                                                                                                         24, 'normal'))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball_x_direction *= -1
            player_B_score += 1
            pen.clear()
            pen.write(f"Player A: {player_A_score}    Player B: {player_B_score}", align='center', font=('Arial',
                                                                                                         24, 'normal'))

        if (340 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
            ball_x_direction *= -1

        if (-350 < ball.xcor() < -340) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
            ball_x_direction *= -1


if __name__ == '__main__':
    main()
