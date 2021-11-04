import turtle                               # Import the necessary modules so that you can work with the tools you need.
import time                                 # Without these imports, Python wouldn't know what to do when you tried
                                            # to start drawing stuff, or monkeying around with time.
# Screen setup

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Analog Clock Project')
screen.tracer(0)                            # The tracer element turns off animation. This'll make sense later.


# Making the 'pencil' that we'll use to draw the clock.
pencil = turtle.Turtle()
pencil.pensize(3)
pencil.speed(0)
pencil.hideturtle()
pencil.goto(0, 0)

def clockwork(h, m, s, pencil):                      # We'll make this whole thing a function with various arguments.

    # The face of the clock, including the circle and the marks for hours/minutes.

    # The circle

    pencil.penup()                          # Off the page.
    pencil.goto(0, 300)                     # The coordinates we'll go to.
    pencil.setheading(180)                  # The direction that the pencil will face (left).
    pencil.color('Lime')                 # The color of the pencil? Magenta.  It stands out.
    pencil.pendown()                        # Putting the pencil to the paper.
    pencil.circle(300)                      # Draw the circle with a radius of 300 pixels.

    # At this point, when the program runs, a magenta circle appears on a black screen.

    # The hour marks.

    pencil.penup()                          # Off the page.
    pencil.goto(0, 0)                       # Back to the center.
    pencil.setheading(90)                   # Facing directly up.

    for hour in range(12):                  # Using a for loop to execute the same lines for every hour.
        pencil.fd(250)                      # From the center, up 250 pixels.
        pencil.pendown()                    # Down on the page, ready to draw stuff.
        pencil.fd(35)                       # Forward (in this case, up) 30 pixels.
        pencil.penup()                      # Off the page, as we have made our mark.
        pencil.goto(0, 0)                   # Back to the center.
        pencil.rt(30)                       # Repeat this every 30 degrees (360 deg. / 12 hours = 30 degrees per hour)


    # The minute marks.  Same as the hour marks, except for one key difference...

    pencil.penup()
    pencil.goto(0, 0)
    pencil.setheading(90)

    for minute in range (60):
        pencil.fd(250)
        pencil.pendown()
        pencil.fd(20)
        pencil.penup()
        pencil.goto(0, 0)
        pencil.rt(6)                        # These marks are repeated every 5 degrees (360 deg. / 60 minutes =
                                            # 5 degrees per minute)


    # The hour hand.

    pencil.penup()                          # Off the paper.
    pencil.goto(0, 0)                       # Return to the center.
    pencil.color('Blue')                    # A different color than the hour and minute marks to stand out.
    pencil.setheading(90)                   # Facing straight up.
    angle = (h / 12) * 360                  # A variable, 'angle', is established. It is equal to whatever the
                                            # argument 'h' is at the time, divided by 12, and then multiplied by
                                            # 360 to give us a certain degree for every hour.  For example: if it's
                                            # 3 pm, 'angle' will divide 3 by 12 then multiply by 360 to get 90,
                                            # setting the hand at 90 degrees, or the third hour mark.  3 pm.

    pencil.rt(angle)                        # The hand stops only at certain angles, in this case, whatever the
                                            # current hour is.  Because the angle value of 'h' is divided by 12,
                                            # the hour hand will only ever sit on hour marks, and never minute marks.
    pencil.pendown()
    pencil.fd(280)                          # 280 pixels long.
    pencil.penup()


    # The minute hand.

    pencil.penup()
    pencil.goto(0, 0)
    pencil.color('Teal')
    pencil.width(2)
    pencil.setheading(90)
    angle = (m / 60) * 360                  # Instead of dividing by 12, like the hour marks, we get the angle to
                                            # equal the argument 'm', representing the current minute in the hour.
    pencil.rt(angle)
    pencil.pendown()
    pencil.fd(260)                          # not quite as long as the hour, so that both can be seen when the
                                            # minute and hour hands briefly overlap.
    pencil.penup()


    # The second hand.

    pencil.penup()
    pencil.goto(0, 0)
    pencil.color('White')                  # Let's stand out a bit.
    pencil.width(2)
    pencil.setheading(90)
    angle = (s / 60) * 360                  # Also divided by 60, since there are 60 seconds counted in every
                                            # minute, and therefore revolution of the 'second' hand.
    pencil.rt(angle)
    pencil.pendown()
    pencil.fd(200)                          # Again, shorter so that it can always be seen.
    pencil.penup()

while True:                                 # An infinite while loop that always keeps the time current. After time
                                            # is imported at the top.

    h = int(time.strftime('%I'))            # For whatever reason, Python represents the current hour with 'I' for
                                            # 12 Hour format clocks.  It's 'H' for 24 Hour formats, like digital
                                            # clocks.
    m = int(time.strftime('%M'))            # A capital 'M' for the minutes...
    s = int(time.strftime('%s'))            # and a lowercase 's' for the seconds.


    clockwork(h, m, s, pencil)              # Call the function, add the arguments, make it happen.

    screen.update()                         # This lets the animation be seen again. Remember the .tracer from
                                            # before? While the program 'remembers' what is drawn, this .update
                                            # function lets the program update...
    time.sleep(1)                           # In one-second intervals, which is the job of the .sleep function.
                                            # The argument '1' tells the time.sleep function to draw everything,
                                            # pause for '1' second, then do it all again.

    pencil.clear()                          # Clear the screen every time the time itself changes. Without this,
                                            # you'd get a moving second hand that won't go away every time it counts
                                            # a second.  In other words, after a minute, you'd have 60 second hands.

