# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for monochromatic character LCD - Modified for Pico 2W"""

import time
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# LCD size
lcd_columns = 16
lcd_rows = 2

# Pico 2W Pin Config (based on your wiring):
lcd_rs = digitalio.DigitalInOut(board.GP0)
lcd_en = digitalio.DigitalInOut(board.GP1)
lcd_d4 = digitalio.DigitalInOut(board.GP2)
lcd_d5 = digitalio.DigitalInOut(board.GP3)
lcd_d6 = digitalio.DigitalInOut(board.GP4)
lcd_d7 = digitalio.DigitalInOut(board.GP5)

# Note: No backlight control pin - backlight is hardwired to 3.3V

# Initialise the LCD class (no backlight parameter)
lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

# Your custom heart character data (8 rows, 5 bits each)
# Here's a website that lets you draw a character & gives you the row values:
# https://www.quinapalus.com/hd44780udg.html
heart_char = [
    0b00000,  # Row 1: %00000 (0)
    0b01010,  # Row 2: %01010 (10)
    0b10101,  # Row 3: %10101 (21)
    0b10001,  # Row 4: %10001 (17)
    0b01010,  # Row 5: %01010 (10)
    0b00100,  # Row 6: %00100 (4)
    0b00000,  # Row 7: %00000 (0)
    0b00000   # Row 8: %00000 (0)
]

lcd.create_char(0, heart_char)

print("Starting the LCD test...")

def basic_message():
    lcd.clear()
    lcd.cursor = False
    # Print a two line message
    print("Test 1: Basic message")
    lcd.message = f"Hello,\nHatchery!"
    # Wait 5s
    time.sleep(5)
    lcd.clear()

def right_to_left():
    # Print two line message right to left
    print("Test 2: Right to left text")
    lcd.text_direction = lcd.RIGHT_TO_LEFT
    lcd.message = "Can you\nread backwards?"
    # Wait 5s
    time.sleep(5)

    # Return text direction to left to right
    lcd.text_direction = lcd.LEFT_TO_RIGHT

def line_cursor():
    # Display cursor
    print("Test 3: Cursor display")
    lcd.clear()
    lcd.cursor = True
    lcd.message = "Line Cursor! "
    # Wait 5s
    time.sleep(5)

def blink_cursor():
    # Display blinking cursor
    print("Test 4: Blinking cursor")
    lcd.clear()
    lcd.blink = True
    lcd.message = "Blinky Cursor!"
    # Wait 5s
    time.sleep(5)
    lcd.blink = False
    lcd.cursor = False
    lcd.clear()

def scrll_test():
    # Create message to scroll
    print("Test 5: Scrolling text")
    scroll_msg = "<-- Join MakeBC & Take Physical Computing!"

    # Proper single-line scrolling - show 16-character window of long message
    # for i in range(len(scroll_msg) - 15):
    for i in range(len(scroll_msg)):
        lcd.clear()
        # Show 16 characters starting at position i
        window = scroll_msg[i:i+16]
        lcd.message = window
        time.sleep(0.25)

def closing_messages():
    lcd.clear()
    lcd.message = "16x2 characters\nKnob = contrast"
    time.sleep(4)
    lcd.clear()
    lcd.message = "Always on?\nFine with me!"
    time.sleep(4)

    # Final message
    lcd.clear()
    lcd.message = f"{chr(0)} Make Awesome {chr(0)}\n  {chr(0)} Hack On! {chr(0)}"

    time.sleep(3)

while True:
    basic_message()
    right_to_left()
    line_cursor()
    blink_cursor()
    scrll_test()
    closing_messages()