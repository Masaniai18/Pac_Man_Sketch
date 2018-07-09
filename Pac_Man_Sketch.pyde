def setup():
    size(300, 300)                                # Set the window size
    background(0, 0, 0)                           # set gray background
    fill(255, 255, 0)                             # Yellow filling
    XCoord = 50                                   #
    YCoord = 160                                  #
    With = 100                                    #
    Hight = 100                                   #
    arc(XCoord, YCoord, With, Hight, .60000000000000000000, PI+QUARTER_PI)
    arc(XCoord, YCoord, With, Hight, QUARTER_PI, TWO_PI)
    fill(255)                                     # Set fill to white
    YCoord = 160                                  #
    Hight = 35                                    #
    With = 35                                     #
    ellipse(125, YCoord, Hight, With)             # Set circle size and location
    ellipse(200, YCoord, Hight, With)             # Set circle size and location
    ellipse(300, YCoord, Hight + 40, With + 40)   # Set power pellete size and location
    strokeWeight(12.0)                            # Give line weight
    strokeCap(ROUND)                              # Give line shape
    stroke(0, 0, 255)                             # Fill line color
    line(1, 100, 300, 100)                        # Set line location and length
    stroke(0, 0, 255)                             # Give line color
    line(1, 225, 300, 225)                        # Set line location and length
    
     
    
