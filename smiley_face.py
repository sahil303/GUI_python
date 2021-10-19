import  arcade

w  = 800
h = 800
arcade.open_window(w,h, "SMILEY FACE")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

# Face Circle
x = 400
y = 400
radius = 250
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

# Left eye circle
x = 310
y = 500
radius = 20
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

# right eye circle
x = 480
y = 500
radius = 20
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK) 
arcade.finish_render()
arcade.run()
