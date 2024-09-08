#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(1000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)


DS5 = 622
GS5 = 830
FS5 = 739
E5 = 659
B4 = 494
A4 = 440
FS4 = 370
CS5 = 554
D4 = 294
CS4 = 277
F4 = 349
D5 = 587
GS4 = 415
G4 = 392

b_d = 60 / 114
DURATIONS = {
    '1': b_d * 4,    
    '2': b_d * 2,    
    '-4': b_d * 1.5, 
    '4': b_d * 1,    
    '8': b_d * 0.5  
}

melody = [
    (FS4, DURATIONS['8']), (A4, DURATIONS['8']), (CS5, DURATIONS['8']),
    (A4, DURATIONS['8']), (FS4, DURATIONS['8']), (D4, DURATIONS['8']),
    (D4, DURATIONS['8']), (D4, DURATIONS['8']),
    (CS4, DURATIONS['8']), (D4, DURATIONS['8']), (FS4, DURATIONS['8']), 
    (A4, DURATIONS['8']), (CS5, DURATIONS['8']), (A4, DURATIONS['8']),
    (F4, DURATIONS['8']), (E5, DURATIONS['-4']), (DS5, DURATIONS['8']), (D5, DURATIONS['8']),
    (GS4, DURATIONS['8']), (CS5, DURATIONS['8']), (FS4, DURATIONS['8']),
    (CS5, DURATIONS['8']), (GS4, DURATIONS['8']), (CS5, DURATIONS['8']),
    (G4, DURATIONS['8']), (FS4, DURATIONS['8']),              
]

print("Playing frequency (Hz):")

#(wii theme song)
for freq, duration in melody:
    print(freq)
    playtone(freq, duration)
    quiet()
    utime.sleep(0.05) 
# Turn off the PWM
quiet()
