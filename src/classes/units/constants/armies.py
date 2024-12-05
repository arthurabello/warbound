import os

class Armies:

    """
    Armies for the game.
    """
    
    DEFAULT = [
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################",
        "##############################"
    ]
    
    ALEXANDER = [
        "##############################",
        "#######IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHC##IIII###################",
        "##############################",
        "##############################",
        "#AAHC##IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "#AAHCC#IIII###################",
        "##############################"
    ]
    
    EDWARD = [
        "##############################",
        "#AAAA#MMMM####################",
        "#AAAA#MMMM#C##################",
        "#AAAA#MMMM#C##################",
        "#AAAA#MMMM#C##################",
        "#AAAA######C##################",
        "###########C##################",
        "#AAAA##CC##C##################",
        "#AAAA######C##################",
        "#AAAA#CCCC#C##################",
        "#AAAA#CCCC#C##################",
        "#AAAA######C##################",
        "#AAAA##CC##C##################",
        "###########C##################",
        "#AAAA#MMMM#C##################",
        "#AAAA#MMMM#C##################",
        "#AAAA#MMMM#C##################",
        "#AAAA#MMMM#C##################",
        "#AAAA#MMMM####################",
        "##############################"
    ]
    
    CHARLEMAGNE = [
        "##############################",
        "#MMM###PPP####################",
        "#MMMM##PPPP###################",
        "#MMMM##PPPP###################",
        "#MMMM##PPPP###################",
        "#MMMM##PPPP###################",
        "#######PPPP###################",
        "#CCAA##PPPP###################",
        "#CCAA##PPPP###################",
        "#CCAA##PPPP###################",
        "#CCAA##PPPP###################",
        "#CCAA##PPPP###################",
        "#CCAA##PPPP###################",
        "#######PPPP###################",
        "#MMMM##PPPP###################",
        "#MMMM##PPPP###################",
        "#MMMM##PPPP###################",
        "#MMMM##PPPP###################",
        "#MMM###PPP####################",
        "##############################"
    ]
    
    HARALD = [
        "##############################",
        "#AAA##########################",
        "#AAA#VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#####VVV#CCC##################",
        "#VVV#####CCC##################",
        "#VVV#VVV#CCC##################",
        "#VVV#VVV######################",
        "#VVV#VVV######################",
        "#VVV#VVV#CCC##################",
        "#VVV#####CCC##################",
        "#####VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#AAA#VVV#CCC##################",
        "#AAA##########################",
        "##############################"
    ]
    
    JULIUS = [
        "##############################",
        "#AAA#####LLL##################",
        "#AAA#####LLL##################",
        "#AAA#CCC#LLL##################",
        "#AAA#CCC#LLL##################",
        "#AAA#CCC#LLL##################",
        "#####CCC######################",
        "#LLL#CCC#LLL##################",
        "#LLL#CCC#LLL##################",
        "#LLL#####LLL##################",
        "#LLL#####LLL##################",
        "#LLL#CCC#LLL##################",
        "#LLL#CCC#LLL##################",
        "#####CCC######################",
        "#AAA#CCC#LLL##################",
        "#AAA#CCC#LLL##################",
        "#AAA#CCC#LLL##################",
        "#AAA#####LLL##################",
        "#AAA#####LLL##################",
        "##############################"
    ]
    
    LEONIDAS = [
        "##############################",
        "#AA#HHHHH#####################",
        "#AA#HHHHH#####################",
        "####HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "####HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "####HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "#AA#HHHHHH####################",
        "####HHHHHH####################",
        "#AA#HHHHH#####################",
        "#AA#HHHHH#####################",
        "##############################"
    ]
