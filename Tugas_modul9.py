import turtle

# Setup layar
s= turtle.Screen()
s.bgcolor("lightyellow")

# Objek turtle
t= turtle.Turtle()
t.speed(2)

# Fungsi menggambar persegi panjang
def draw_rectangle(t, width, height, color):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Menggambar badan kue (3 lapis)
def draw_cake():
    # Lapis bawah
    t.penup()
    t.goto(-100, -150)
    t.pendown()
    draw_rectangle(t, 200, 50, "pink")

    # Lapis tengah
    t.penup()
    t.goto(-75, -100)
    t.pendown()
    draw_rectangle(t, 150, 50, "pink")

    # Lapis atas
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    draw_rectangle(t, 100, 50, "pink")

# Menggambar lilin
def draw_candle():
    t.penup()
    t.goto(-5, 0)
    t.pendown()
    draw_rectangle(t, 10, 30, "white")

    # Api lilin
    t.penup()
    t.goto(0, 30)
    t.pendown()
    t.begin_fill()
    t.fillcolor("yellow")
    t.circle(5)
    t.end_fill()

# Happy Birthday
def ucapan():
    t.color('black')
    t.penup()
    t.goto(0, 100)
    t.write('HAPPY BIRTHDAY',align='center', font="Times 35 normal")
# Jalankan fungsi
draw_cake()
draw_candle()
ucapan()


# Selesai
t.hideturtle()
s.mainloop()
