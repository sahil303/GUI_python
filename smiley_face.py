import  arcade

w,h = 800,800

arcade.open_window(w,h, "SMILEY FACE")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

# Face Circle
x,y,radius = 400,400, 250
arcade.draw_circle_filled(x,y,radius,arcade.color.YELLOW)

# Left eye circle
x,y,radius = 310,500, 20
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

# right eye circle
x,y,radius = 480,500, 20
arcade.draw_circle_filled(x,y,radius,arcade.color.BLACK)

# Smile line
x,y,w,h,start_angle,end_angle = 400, 350, 100, 100, 190,350
arcade.draw_arc_outline(x,y,w,h,arcade.color.BLACK,start_angle,end_angle,15)
arcade.finish_render()
arcade.run()
