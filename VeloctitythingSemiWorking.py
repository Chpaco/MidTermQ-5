# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 18:18:11 2022

@author: spltd
"""
import math
theta =45
vinitial = 35

g = 9.81

while  theta < 80:
    
    vinitial = 15
    while vinitial< 45:
         xmax = (((2*(vinitial*vinitial))* (math.sin(math.radians(theta))* math.cos(math.radians(theta))) ))/g
        #vx = vinitial*math.cos(theta)
       #xmax = ((vinitial*vinitial)*(math.sin(2*theta)))/g
         vx = vinitial*(math.cos(math.radians(theta)))  # x compontent velocity
         vy = vinitial*(math.sin(math.radians(theta)))  # y compontent veloctiy
         t =vy/g# time
         xp = vx*t # x position
        # causes erros for some reason ntoxtf = 25 / (vinitial*math.cos(math.radians(theta))
         timeof25 = (25/(vinitial* math.cos(math.radians(theta))))
         
         tox = xp/vx
         yatx25 = (vy*timeof25) - (.5*(g*(timeof25*timeof25)))
          
         #print('theta',theta, 'v',vinitial, 'xmax',xmax)
         #print('theta',theta, 'v',vinitial, 'xmax',xmax, 'yatx25', yatx25)
         if  79.8 <= xmax <= 80.2 and yatx25 >=35.1:
             
                 print('works','theta',theta, 'v',vinitial, 'xmax',xmax, "yatx25", yatx25)
             #values.append('theta', theta, 'v', vinitial, xmax)
                 #print('theta',theta, 'v',vinitial, 'xmax',xmax)
             #print('degrees',math.radians(theta))
             #break
         vinitial +=.001 
         continue
    theta +=.001  
             
    continue
#print(xmax)     
math.sin(math.radians(60.794))  # notation for degrees answer
math.cos(math.radians(60.794))    
#while theta < 90:
  # i = 0.0
   #x = 0.0
  # while i < theta:
      #  while x < vinitial:
   
         #   xmax = (2*((x**2)* math.sin(i)* math.cos(i) ))/g
        #    if xmax == 80:
           #     break
         #   x = x +.1
       # i = i+.1    

#print(xmax)