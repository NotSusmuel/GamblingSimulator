import turtle
import blackjack
import slotmachine

# Setup Screen
screen = turtle.Screen()
screen.title("Gambling Simulator")
screen.bgcolor("#1a1a2e")  # Dark blue-purple background
screen.setup(width=800, height=600)
turtle.tracer(0)

# Draw title
def draw_title():
    title = turtle.Turtle()
    title.hideturtle()
    title.penup()
    title.goto(0, 200)
    title.color("#eef4ed")
    title.write("🎰 CASINO ROYALE 🎰", align="center", font=("Arial", 36, "bold"))
    title.goto(0, 160)
    title.color("#16213e")
    title.write("━━━━━━━━━━━━━━━━━━━━", align="center", font=("Arial", 20, "bold"))

# Button zeichnen with rounded corners
def draw_button(x, y, width, height, text, color="#e94560"):
    btn = turtle.Turtle()
    btn.hideturtle()
    btn.penup()
    btn.goto(x, y)
    btn.pendown()
    btn.pensize(3)
    btn.color("#0f3460")  # Border color
    btn.begin_fill()
    btn.fillcolor(color)
    
    # Draw rounded rectangle
    radius = 15
    for _ in range(2):
        btn.forward(width - 2*radius)
        btn.circle(-radius, 90)
        btn.forward(height - 2*radius)
        btn.circle(-radius, 90)
    
    btn.end_fill()
    btn.penup()
    btn.goto(x + width/2, y - height/2 - 10)
    btn.color("#ffffff")
    btn.write(text, align="center", font=("Arial", 20, "bold"))
    return (x, x+width, y-height, y)  # Button-Region

# Draw title
draw_title()

# Buttons erzeugen
blackjack_btn = draw_button(-100, 80, 200, 50, "♠️ Blackjack ♠️", "#e94560")
slot_btn = draw_button(-100, 10, 200, 50, "🎰 Slot Machine", "#e94560")
exit_btn = draw_button(-100, -60, 200, 50, "Exit Game", "#533483")

turtle.update()

# Hilfsfunktion: Einsatz abfragen
def get_bet_amount():
    try:
        bet = turtle.textinput("💰 Place Your Bet", "Enter bet amount (max $5,000):")
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
