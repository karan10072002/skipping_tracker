# skipping_tracker

This project is to count the nunmber of skip jumps done by the person using OpenCV python.

You need python installed on your system
packages and dependencies requrired: 

numpy,
opencv-python

The algorithm
1. Detects the colour of the shirt.
2. Create mask and necessary abbrasive corrections.
3. Find highest y-coordinate (i.e. HY) of postive mask in the initial frame.
4. Make base horizontal line at HY.
5. Find higest y-cooerdinate (i.e HY1) in all consecutive frames.
6. If ( HY1 > HY then HY1 < HY ) count as 1 skip jump.

Stability in video frame increases accurecy. 



Author: 
Karan kumar chaurasia
github.com/karan10072002/skipping_tracker/ , 
instagram.com/karan10072002/
