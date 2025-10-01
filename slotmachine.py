import turtle
import random
import time
import os

def slotmachine(bet_amount):
    global balance_amount, frame, lever, spinning, row1, row2, row3, row1ashape, row2ashape, row3ashape, row1bshape, row2bshape, row3bshape, row1cshape, row2cshape, row3cshape, a, b, c
    def load_balance():
        if os.path.exists("balance.txt"):
            with open("balance.txt", "r") as f:
                try:
                    return int(f.read())
                except:
                    return 1000
        else:
            return 1000
        
    def save_balance(amount):
        with open("balance.txt", "w") as f:
            f.write(str(amount))
    # Set up the screen
    screen = turtle.Screen()
    screen.title("🎰 Slot Machine 🎰")
    screen.bgcolor("#1a1a2e")  # Dark blue-purple background

    turtle.tracer(0)

    # Render the Balance
    balance_amount = load_balance()
    balance = turtle.Turtle()
    balance.color("#eef4ed")
    balance.penup()
    balance.goto(-290, 250)
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

    #draw the slot machine frame
    frame = turtle.Turtle()
    frame.color("#e94560")
    frame.pensize(6)
    frame.penup()
    frame.goto(-150, 100)
    frame.pendown()
    frame.fillcolor("#0f3460")
    frame.begin_fill()
    def rounded_corner():
            for _ in range(9):
                frame.right(10)
                frame.forward(10)
    for _ in range(2):
        frame.forward(300)
        rounded_corner()
        frame.forward(200)
        rounded_corner()
    frame.end_fill()
    frame.hideturtle()

    #draw lever
    lever = turtle.Turtle()
    lever.penup()
    lever.shape("circle")
    lever.color("#e94560")
    lever.shapesize(stretch_wid=2, stretch_len=2)
    lever.goto(170, 100)
    lever.pendown()

    def drawlever(h):
        lever.clear()
        lever.color("#533483")
        lever.goto(170, h)
        lever.pendown()
        lever.pensize(12)
        lever.goto(170, 0)
        lever.goto(170, h)
        lever.penup()
        lever.color("#e94560")
        turtle.update()
    drawlever(100)

    spinning=False
    def pull_lever():
        global spinning
        spinning = True
        for _ in range(10):
            drawlever(100-10 * (_ + 1))
            time.sleep(0.05)
        gamble()
        for _ in range(20):
            drawlever(5 * (_ + 1))
            time.sleep(0.05)
        spinning = False

    def on_lever_click(x, y):
        global spinning
        if not spinning:
            pull_lever()

    lever.onclick(on_lever_click)

    def winorlose():
        result=random.randint(1, 10)
        if result==10: #high chance to win jackpot
            a=1
            b=1
            c=random.randint(1, 5)
        elif result==9:
            a=random.randint(1, 5)
            b=a
            c=random.randint(1, 5)
        elif result==8:
            a=random.randint(1, 5)
            b=a
            c=random.randint(1, 5)
        elif result==7: 
            a=random.randint(1, 5)
            b=random.randint(1, 5)
            c=b
        elif result==6: # you cant win haha
            a=1
            b=1
            c=random.randint(2, 5)
        elif result==5:
            a=1
            b=random.randint(1, 5)
            c=random.randint(1, 5)
        elif result==4:
            a=random.randint(2, 5)
            b=1
            c=random.randint(1, 5)
        elif result==3:
            a=1
            b=1
            c=random.randint(2, 5)
        else:
            a=random.randint(1, 5)
            b=random.randint(1, 5)
            c=random.randint(1, 5)
        return a, b, c

    # 1=7️⃣
    # 2=🍒
    # 3=🍋
    # 4=🔔
    # 5=⭐

    row1ashape = ""
    row2ashape = ""
    row3ashape = ""
    row1bshape = ""
    row2bshape = ""
    row3bshape = ""
    row1cshape = ""
    row2cshape = ""
    row3cshape = ""

    row1=turtle.Turtle()
    row2=turtle.Turtle()
    row3=turtle.Turtle()
    row1.color("#eef4ed")
    row2.color("#eef4ed")
    row3.color("#eef4ed")
    row1.hideturtle()
    row2.hideturtle()
    row3.hideturtle()
    row2.penup()
    row3.penup()
    row2.goto(0, -90)
    row3.goto(0, -180)

    def definerandomshape(row_shape):
        shape=random.randint(1, 5)
        if shape==1:
            row_shape="7️⃣"
        elif shape==2:
            row_shape="🍒"
        elif shape==3:
            row_shape="🍋"
        elif shape==4:
            row_shape="🔔"
        elif shape==5:
            row_shape="⭐"
        return row_shape

    def numbertoshape(num):
        if num==1:
            return "7️⃣"
        elif num==2:
            return "🍒"
        elif num==3:
            return "🍋"
        elif num==4:
            return "🔔"
        elif num==5:
            return "⭐"

    def spinanimation(t, s, a, b, c):
        for _ in range(t):
            global row1ashape, row2ashape, row3ashape
            global row1bshape, row2bshape, row3bshape
            global row1cshape, row2cshape, row3cshape
            if a==True:
                row3ashape=row2ashape
            if b==True:
                row3bshape=row2bshape
            if c==True:
                row3cshape=row2cshape
            if a==True:
                row2ashape=row1ashape
            if b==True:
                row2bshape=row1bshape
            if c==True:
                row2cshape=row1cshape
            if a==True:
                row1ashape=definerandomshape(row1ashape)
            if b==True:
                row1bshape=definerandomshape(row1bshape)
            if c==True:
                row1cshape=definerandomshape(row1cshape)
            row1.clear()
            row2.clear()
            row3.clear()
            row1.write(row1ashape + " " + row1bshape + " " + row1cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
            row2.write(row2ashape + " " + row2bshape + " " + row2cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
            row3.write(row3ashape + " " + row3bshape + " " + row3cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
            turtle.update()
            time.sleep(s)

    def fakeanimation(a1, b1, c1): 
        global row1ashape, row2ashape, row3ashape
        global row1bshape, row2bshape, row3bshape
        global row1cshape, row2cshape, row3cshape
        row1.clear()
        row2.clear()
        row3.clear()
        #random shapes
        row1ashape=definerandomshape(row1ashape)
        row1bshape=definerandomshape(row1bshape)
        row1cshape=definerandomshape(row1cshape)
        row2ashape=definerandomshape(row2ashape)
        row2bshape=definerandomshape(row2bshape)
        row2cshape=definerandomshape(row2cshape)
        row3ashape=definerandomshape(row3ashape)
        row3bshape=definerandomshape(row3bshape)
        row3cshape=definerandomshape(row3cshape)
        spinanimation(20, 0.01, True, True, True)
        spinanimation(15, 0.05, True, True, True)
        spinanimation(10, 0.1, True, True, True)
        row3ashape=row2ashape
        row3bshape=row2bshape
        row3cshape=row2cshape
        row2ashape=row1ashape
        row2bshape=row1bshape
        row2cshape=row1cshape
        row1ashape=numbertoshape(a1)
        row1bshape=definerandomshape(row1bshape)
        row1cshape=definerandomshape(row1cshape)
        row1.clear()
        row2.clear()
        row3.clear()
        row1.write(row1ashape + " " + row1bshape + " " + row1cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row2.write(row2ashape + " " + row2bshape + " " + row2cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row3.write(row3ashape + " " + row3bshape + " " + row3cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        turtle.update()
        time.sleep(0.1)
        spinanimation(1, 0.1, True, True, True)
        spinanimation(5, 0.1, False, True, True)
        row3bshape=row2bshape
        row3cshape=row2cshape
        row2bshape=row1bshape
        row2cshape=row1cshape
        row1bshape=numbertoshape(b1)
        row1cshape=definerandomshape(row1cshape)
        row1.clear()
        row2.clear()
        row3.clear()
        row1.write(row1ashape + " " + row1bshape + " " + row1cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row2.write(row2ashape + " " + row2bshape + " " + row2cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row3.write(row3ashape + " " + row3bshape + " " + row3cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        turtle.update()
        time.sleep(0.1)
        spinanimation(1, 0.2, False, True, True)
        spinanimation(5, 0.5, False, False, True)
        row3cshape=row2cshape
        row2cshape=row1cshape
        row1cshape=numbertoshape(c1)
        row1.clear()
        row2.clear()
        row3.clear()
        row1.write(row1ashape + " " + row1bshape + " " + row1cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row2.write(row2ashape + " " + row2bshape + " " + row2cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row3.write(row3ashape + " " + row3bshape + " " + row3cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        turtle.update()
        time.sleep(1)
        row3cshape=row2cshape
        row2cshape=row1cshape
        row1cshape=definerandomshape(row1cshape)
        row1.clear()
        row2.clear()
        row3.clear()
        row1.write(row1ashape + " " + row1bshape + " " + row1cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row2.color("#e94560")
        row2.write(row2ashape + " " + row2bshape + " " + row2cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        row3.write(row3ashape + " " + row3bshape + " " + row3cshape, align="center", font=("Segoe UI Emoji", 48, "normal"))
        turtle.update()
        row2.color("#eef4ed")

    a, b, c = winorlose()

    def findprize(a, b, c):
        if a==1 and b==1 and c==1:
            return bet_amount*10
        elif a==1 or b==1 or c==1:
            return 0
        elif a==1 and b==1:
            return 0
        elif a==1 and c==1:
            return 0
        elif b==1 and c==1:
            return 0
        elif a==b==c:
            return bet_amount*5
        elif a==b or a==c or b==c:
            return bet_amount*2
        else:
            return 0

    def gamble():
        update_negative_balance(bet_amount) #cost to play
        global a, b, c
        a, b, c = winorlose()
        fakeanimation(a, b, c)
        update_balance(findprize(a, b, c))

    turtle.done()