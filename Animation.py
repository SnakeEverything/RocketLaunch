from Focus_Roots import *

rocket_body_y = 225
left_wing_first = 255
left_wing_second = 350
left_wing_third = 350
right_wing_first = 255
right_wing_second = 350
right_wing_third = 350
head_1 = 225
head_2 = 175
head_3 = 225
window_1 = 250
window_2 = 285
window_3 = 320


def change():
    global rocket_body_y, left_wing_first, left_wing_second, left_wing_third, right_wing_first, right_wing_second, right_wing_third, head_1, head_2, window_1, window_2, window_3
    set_background(color_black)#This will set the background
    draw_circle(250,600,300,0,color = color_blue)
    draw_rect(225, rocket_body_y, 50, 125, 0, color = color_firebrick)# Body of the Rocket
    draw_polygon([[225,left_wing_first],[225,left_wing_second],[170,left_wing_third]],0,color = color_sky_blue)#Left Wing
    draw_polygon([[275,right_wing_first],[275,right_wing_second],[330,right_wing_third]],0,color = color_sky_blue)#Right Wing
    draw_polygon([[200,head_1],[250,head_2],[300,head_1]],0,color = color_sky_blue)#Rocket Head
    draw_circle(250,window_1,10,0,color = color_banana)#Top Window
    draw_circle(250,window_2,10,0,color = color_banana)#Middle Window
    draw_circle(250,window_3,10,0,color = color_banana)#Bottom Window
    write_text("Rocket is about to Launch!", 250, 420, 30, color = color_antiquewhite1)
    draw_circle(400, 290, 20, 0, color = color_emeraldgreen)#Planet

    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/star.png",25,25,100,100)#Star 1
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/star.png",25,25,233,134)#Star 2
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/star.png",25,25,385,160)#Star 3
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/star.png",25,25,452,249)#Star 4
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/star.png",25,25,94,200)#Star 5
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/star.png",25,25,300,169)#Star 6
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/planet.png",50,50,400,100)#planet 1
    image("C:/Users/snake/OneDrive/Desktop/Focus Roots/Python/Creative/Images/Ring_Planet.png",50,50,69,69)#planet 2

    rocket_body_y = rocket_body_y -1

    left_wing_first -=1
    left_wing_second -=1
    left_wing_third -=1

    right_wing_first -=1
    right_wing_second -=1
    right_wing_third -=1

    head_1 -=1
    head_2 -=1

    window_1 -=1
    window_2 -=1
    window_3 -=1

draw(change)