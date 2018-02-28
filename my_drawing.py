from shapes import Triangle, Rectangle, Oval

rect1 = Rectangle()

rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()


rec2 = Rectangle()

rec2.set_width(50)
rec2.set_height(150)
rec2.set_color("yellow")
rec2.draw()
rec2.set_x(100)
rec2.set_y(100)

ov1 = Oval()

ov1.randomize(20)
ov1.draw()

tri1 = Triangle(5,10, 100,5, 100,200)
tri1.draw()
