Excercise 1:
Min_Bright: 43,000
Max_Bright: 1,300
First, we connected the 10k ohm resistor to the 3V3 and ADC2 pins, and following that we connected the photoresistor to ADC2 and GND. Then, after making sure the code is running on the Raspberry Pi, we used a flashlight and a hand to find the maximum and minimum brightness values respectively.

Excercise 2: Wii Mii Theme Song 
We first connected the speaker to GND (black wire) and to the PWM pin GP16 (red wire). After, we modified the provided code to play the Wii Mii Theme Song, using an online resource for the correct musical notes and their corresponding frequencies.

Excercise 3: Response Time Measurement Game and Cloud Upload
We first edited the code to compute the average, minimum and maximum response time for the flashes, and then changed the number  of flashes to 10. We also stored the values in the data dictionary in the function. We then decided to use firebase and their real time database in order to send the http request json object of our response times. We then connected our Pi Pico to the network so it would be able to send the json object over the http request. In order to send a post to our real time database we used the urequests package and our real time database url. 
