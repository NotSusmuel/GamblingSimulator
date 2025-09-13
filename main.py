import turtle
import blackjack
import slotmachine

# Setup Screen
screen = turtle.Screen()
screen.title("Gambling Simulator")
screen.bgcolor("green")
screen.setup(width=800, height=600)
turtle.tracer(0)

# Button zeichnen
def draw_button(x, y, width, height, text):
    btn = turtle.Turtle()
    btn.hideturtle()
    btn.penup()
    btn.goto(x, y)
    btn.pendown()
    btn.begin_fill()
    btn.fillcolor("lightblue")
    for _ in range(2):
        btn.forward(width)
        btn.right(90)
        btn.forward(height)
        btn.right(90)
    btn.end_fill()
    btn.penup()
    btn.goto(x + width/2, y - height/2 - 10)
    btn.write(text, align="center", font=("Arial", 24, "bold"))
    return (x, x+width, y-height, y)  # Button-Region

# Buttons erzeugen
blackjack_btn = draw_button(-100, 100, 200, 60, "Blackjack")
slot_btn = draw_button(-100, 0, 200, 60, "Slot Machine")
exit_btn = draw_button(-100, -100, 200, 60, "End Game")

turtle.update()

# Hilfsfunktion: Einsatz abfragen
def get_bet_amount():
    try:
        bet = turtle.textinput("Select Bet", "Please select bet amount(5'000 max.):")
        if bet is None:
            return None
        elif int(bet) > 5000:
            return get_bet_amount()
        return int(bet)
    except:
        return None

# Klick-Logik
def on_click(x, y):
    if blackjack_btn[0] <= x <= blackjack_btn[1] and blackjack_btn[2] <= y <= blackjack_btn[3]:
        bet = get_bet_amount()
        if bet is not None:
            screen.clearscreen()
            blackjack.blackjack(bet)
    elif slot_btn[0] <= x <= slot_btn[1] and slot_btn[2] <= y <= slot_btn[3]:
        bet = get_bet_amount()
        if bet is not None:
            screen.clearscreen()
            slotmachine.slotmachine(bet)
    elif exit_btn[0] <= x <= exit_btn[1] and exit_btn[2] <= y <= exit_btn[3]:
        turtle.bye()

screen.onclick(on_click)

turtle.done()
