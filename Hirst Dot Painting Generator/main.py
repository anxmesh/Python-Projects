# import colorgram as cg
#
# # rgb_list = []
# # colours = cg.extract('image.jpg', 15)
# # for colour in colours:
# #     r = colour.rgb.r
# #     g = colour.rgb.g
# #     b = colour.rgb.b
# #     new_col = (r, g, b)
# #     rgb_list.append(new_col)
# # print(rgb_list)

import random
import turtle as t


screen = t.Screen()
timmyt = t.Turtle()
t.colormode(255)

colour_list = [(199, 175, 117), (212, 222, 215), (125, 36, 24), (167, 106, 56),
               (186, 159, 52), (6, 57, 83), (108, 68, 85), (112, 161, 175), (21, 122, 174),
               (63, 153, 138), (39, 36, 35), (76, 40, 48)]
timmyt.speed("fastest")
for _ in range(10):
    for _ in range(10):
        timmyt.dot(20, random.choice(colour_list))
        timmyt.penup()
        timmyt.fd(50)
        timmyt.pendown()
    timmyt.penup()
    timmyt.setposition(0, float(timmyt.ycor() + 50))
    timmyt.pendown()


screen.exitonclick()
