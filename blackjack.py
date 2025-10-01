import turtle
import random
import time
import os

def blackjack(bet_amount):
    global balance_amount, startbutton, deck, old_card_value, card_value, total
    # Function to load balance from a file
    def load_balance():
        if os.path.exists("balance.txt"):
            with open("balance.txt", "r") as f:
                try:
                    return int(f.read())
                except:
                    return 1000
        else:
            return 1000
    # Function to save balance to a file
    def save_balance(amount):
        with open("balance.txt", "w") as f:
            f.write(str(amount))

    # Set up the screen
    screen = turtle.Screen()
    screen.title("♠️ Blackjack ♠️")
    screen.bgcolor("#0f3460")  # Dark blue background
    screen.setup(width=800, height=600)
    turtle.tracer(0)
    # Render the Balance
    balance_amount = load_balance()
    balance = turtle.Turtle()
    balance.color("#eef4ed")
    balance.penup()
    balance.goto(-350, 250)
    balance.pendown()
    balance.hideturtle()
    balance.clear()
    balance.write("💰 Balance: $"+str(balance_amount), align="left", font=("Arial", 20, "bold"))
    def update_balance(amount):
        global balance_amount
        balance_amount += amount
        save_balance(balance_amount)
        balance.clear()
        balance.write("💰 Balance: $"+str(balance_amount), align="left", font=("Arial", 20, "bold"))
    def update_negative_balance(amount):
        global balance_amount
        balance_amount -= amount
        save_balance(balance_amount)
        balance.clear()
        balance.write("💰 Balance: $"+str(balance_amount), align="left", font=("Arial", 20, "bold"))

    # Set up the game area
    game_area = turtle.Turtle()
    game_area.color("#16213e")
    game_area.penup()
    game_area.goto(-350, 200) # durchmesser halbkreis 700
    game_area.pensize(5)
    game_area.pendown()
    game_area.setheading(270)
    game_area.circle(350, 180)
    game_area.hideturtle()
    game_area.penup()
    # start button
    def draw_start_button():
        global startbutton, start_button
        start_button = turtle.Turtle()
        start_button.hideturtle()
        start_button.penup()
        start_button.goto(-60, -250) # linke untere ecke
        start_button.pendown()
        start_button.pensize(3)
        start_button.color("#16213e")
        start_button.begin_fill()
        start_button.fillcolor("#e94560")
        # Draw rounded rectangle
        radius = 10
        for _ in range(2):
            start_button.forward(120 - 2*radius)
            start_button.circle(-radius, 90)
            start_button.forward(40 - 2*radius)
            start_button.circle(-radius, 90)
        start_button.end_fill()
        start_button.penup()
        start_button.goto(0, -250)
        start_button.color("#ffffff")
        start_button.write("▶️ Start", align="center", font=("Arial", 18, "bold"))
        start_button.penup()
        startbutton=True

    def draw_draw_card_button():
        global draw_card_button
        draw_card_button = turtle.Turtle()
        draw_card_button.hideturtle()
        draw_card_button.penup()
        draw_card_button.goto(80, -250) # starting point
        draw_card_button.pendown()
        draw_card_button.pensize(3)
        draw_card_button.color("#16213e")
        draw_card_button.begin_fill()
        draw_card_button.fillcolor("#e94560")
        # Draw rounded rectangle
        radius = 10
        for _ in range(2):
            draw_card_button.forward(180 - 2*radius)
            draw_card_button.circle(-radius, 90)
            draw_card_button.forward(40 - 2*radius)
            draw_card_button.circle(-radius, 90)
        draw_card_button.end_fill()
        draw_card_button.penup()
        draw_card_button.goto(170, -250)
        draw_card_button.color("#ffffff")
        draw_card_button.write("🎴 Draw Card", align="center", font=("Arial", 18, "bold"))
        draw_card_button.penup()

    def draw_reveal_dealer_button():
        global reveal_dealer_button
        reveal_dealer_button = turtle.Turtle()
        reveal_dealer_button.hideturtle()
        reveal_dealer_button.penup()
        reveal_dealer_button.goto(-110, 250) # starting point
        reveal_dealer_button.pendown()
        reveal_dealer_button.pensize(3)
        reveal_dealer_button.color("#16213e")
        reveal_dealer_button.begin_fill()
        reveal_dealer_button.fillcolor("#e94560")
        # Draw rounded rectangle
        radius = 10
        for _ in range(2):
            reveal_dealer_button.forward(220 - 2*radius)
            reveal_dealer_button.circle(-radius, 90)
            reveal_dealer_button.forward(40 - 2*radius)
            reveal_dealer_button.circle(-radius, 90)
        reveal_dealer_button.end_fill()
        reveal_dealer_button.penup()
        reveal_dealer_button.goto(0, 210)
        reveal_dealer_button.color("#ffffff")
        reveal_dealer_button.write("🎲 Reveal Dealer", align="center", font=("Arial", 18, "bold"))
        reveal_dealer_button.penup()

    def draw_onscreen_text(text):
        onscreen_text = turtle.Turtle()
        onscreen_text.hideturtle()
        onscreen_text.penup()
        onscreen_text.goto(0, 0)
        onscreen_text.pendown()
        onscreen_text.color("#eef4ed")
        onscreen_text.write(text, align="center", font=("Arial", 42, "bold"))
        turtle.update()
        onscreen_text.penup()
        time.sleep(2)
        onscreen_text.clear()
        turtle.update()

    draw_start_button()
    card = turtle.Turtle()
    card.hideturtle()
    def draw_card(x, y, card_value):
        colorofnumber = random.choice(["#e94560", "#16213e"])
        card.penup()
        card.goto(x, y)
        card.pendown()
        card.pensize(3)
        card.color("#16213e")
        card.fillcolor("#eef4ed")
        card.begin_fill()
        # Draw rounded rectangle for card
        radius = 8
        for _ in range(2):
            card.forward(60 - 2*radius)
            card.circle(-radius, 90)
            card.forward(90 - 2*radius)
            card.circle(-radius, 90)
        card.end_fill()
        card.penup()
        card.goto(x + 30, y - 60)
        card.color(colorofnumber)
        card.write(str(card_value), align="center", font=("Arial", 28, "bold"))
        card.color("#16213e")
        card.hideturtle()
        turtle.update()

    # Declare these as globals at the top
    deck = []
    old_card_value = 0
    card_value = 0

    def start_game():
        global startbutton, deck, old_card_value, card_value
        start_button.clear()
        startbutton = False
        turtle.update()
        # define first two cards
        totalcards = 2
        cards = []
        deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
        random.shuffle(deck)
        card_value = random.choice(deck)
        draw_card(-200, -190, card_value)
        deck.remove(card_value)
        draw_draw_card_button()
        old_card_value = card_value
        card_value = random.choice(deck)
        draw_card(-120, -190, card_value)
        deck.remove(card_value)
        draw_reveal_dealer_button()
        turtle.update()
        total = old_card_value + card_value
        if total > 21:
            draw_onscreen_text("You Busted!")
            newgame()
            update_negative_balance(bet_amount)
            turtle.update()
        if total == 21:
            draw_onscreen_text("Blackjack! You Win!")
            update_balance(bet_amount*2)
            newgame()

    def stackoldcards():
        global old_card_value
        card.clear()
        draw_card(-200, -190, old_card_value)


    def newgame():
        reveal_dealer_button.clear()
        draw_card_button.clear()
        card.clear()
        startbutton = True
        draw_start_button()

    def button_click(x_click, y_click):
        global deck, old_card_value, card_value, startbutton, total
        if -60 <= x_click <= 60 and -250 <= y_click <= -210 and startbutton == True:
            start_game()
        elif 80 <= x_click <= 260 and -250 <= y_click <= -210 and startbutton == False:
            old_card_value += card_value
            stackoldcards()
            card_value = random.choice(deck)
            draw_card(-120, -190, card_value)
            deck.remove(card_value)
            total = old_card_value + card_value
            if total > 21:
                draw_onscreen_text("You Busted!")
                newgame()
                update_negative_balance(bet_amount)
                turtle.update()
            if total == 21:
                draw_onscreen_text("Blackjack! You Win!")
                update_balance(bet_amount*2)
                newgame()
        elif -110 <= x_click <= 110 and 210 <= y_click <= 250 and startbutton == False:
            reveal_dealer_button.clear()
            draw_card_button.clear()
            total = old_card_value + card_value
            if total > 17 or total == 17:
                winorlose = random.randint(1, 2)
                if winorlose == 1:
                    draw_card(-70, 200, total//2 -1)
                    time.sleep(1)
                    draw_card(10, 200, total//2)
                    time.sleep(1)
                    draw_onscreen_text("You Win!")
                    time.sleep(1)
                    update_balance(bet_amount*2)
                    newgame()
                else:
                    draw_card(-70, 200, total//2 +2)
                    time.sleep(1)
                    draw_card(10, 200, total//2)
                    time.sleep(1)
                    draw_onscreen_text("You Lose!")
                    time.sleep(1)
                    update_negative_balance(bet_amount)
                    newgame()
            else:
                    draw_card(-70, 200, total//2 +2)
                    time.sleep(1)
                    draw_card(10, 200, total//2 +3)
                    time.sleep(1)
                    draw_onscreen_text("You Lose!")
                    time.sleep(1)
                    update_negative_balance(bet_amount)
                    newgame()

        

    # Klicks überwachen
    turtle.onscreenclick(button_click)

    turtle.update()

    turtle.done()