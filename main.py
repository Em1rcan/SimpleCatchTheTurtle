import turtle
import random
import time

end_time = 0
game_over = True
duration = 15

def start_game():
    global score, end_time, game_over
    score = 0
    end_time = time.time() + duration
    score_display.clear()  # Skor etiketini temizle / Clear the score label
    score_display.write("Skor\Score: {}".format(score), align="center", font=("Bold", 24, "normal")) # Score: {}".format(score), align="center", font=("Bold", 24, "normal"))
    window.update()
    game_over = False

    while time.time() < end_time and not game_over:
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.hideturtle()
        t.goto(x, y)
        t.showturtle()
        time.sleep(0.7)
        t.onclick(increase_score)

    if not game_over:
        score_display.clear()  # Skor etiketini temizle / Clear the score label
        score_display.write("Oyun Bitti./Game Over. Skor: {}".format(score), align="center", font=("Bold", 28, "normal")) # Game Over. Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        window.update()
        show_restart_button()

def show_restart_button():
    restart_button.penup()
    restart_button.goto(0, -50)
    restart_button.color("green")
    restart_button.write("Yeniden Başlat (R)", align="center", font=("Sans", 18, "normal"))

def hide_restart_button():
    restart_button.clear()

def on_click(x, y):
    if -50 <= x <= 50 and -95 <= y <= -65:
        restart_game()
        hide_restart_button()
    elif -50 <= x <= 50 and -125 <= y <= -95:
        turtle.bye()

def increase_score(x, y):
    if time.time() < end_time:
        global score
        score += 1
        score_display.clear()  # Skor etiketini temizle / Clear the score label
        score_display.write("Skor: {}".format(score), align="center", font=("Bold", 24, "normal")) # Score: {}".format(score), align="center", font=("Bold", 24, "normal"))

def restart_game():
    global game_over
    t.clear()  # Kaplumbağa çizimini temizle / Clear the turtle drawing
    score_display.clear()  # Skor etiketini temizle / Clear the score label
    hide_restart_button()
    game_over = True
    start_game()

def end_game():
    global game_over
    game_over = True

window = turtle.Screen()
window.setup(width=800, height=600)

t = turtle.Turtle()
t.shape("turtle")
t.turtlesize(stretch_wid=3, stretch_len=3)
t.speed(0)
t.color("green")
t.penup()

score_display = turtle.Turtle()
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

score = 0

restart_button = turtle.Turtle()
restart_button.hideturtle()
restart_button.penup()

# Yeniden başlatma için "r" tuşuna bas / Press for "r" key for restarting
window.onkey(restart_game, "r")
window.listen()

start_game()

# Oyun bittiğinde ekranı temizle / Clear the screen when the game is over
end_game()

turtle.mainloop()
