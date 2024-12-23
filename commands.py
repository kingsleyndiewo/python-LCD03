# -*- coding: utf-8 -*-
# Part of python-LCD03. See LICENSE file for full copyright and licensing details.

""" I2C Commands for the LCD03 module """

NO_OP = 0x00
CURSOR_HOME = 0x01

# 0x01 is the top left corner
# 0x50 is the bottom right corner
SET_CURSOR = 0x02 # next byte should be position index

# line is 1 - 4, column is 1 - 20
SET_CURSOR_XY = 0x03 # next two bytes should be line and column

HIDE_CURSOR = 0x04
SHOW_UNDERLINE_CURSOR = 0x05
SHOW_BLINKING_CURSOR = 0x06
BACKSPACE = 0x08
HORIZ_TAB = 0x09
SMART_LINE_FEED = 0x0A # vertically down one row
VERT_TAB = 0x0B # vertically up one row
CLEAR_SCREEN = 0x0C # clear screen and home cursor
CARRIAGE_RETURN = 0x0D # move cursor to start of next row
CLEAR_COLUMN = 0x11 # clear current column and move cursor right
TAB_SET = 0x12 # set tab size, next byte is tab size between 1 and 10
BACKLIGHT_ON = 0x13 
BACKLIGHT_OFF = 0x14
DISABLE_STARTUP_MSG = 0x15
ENABLE_STARTUP_MSG = 0x16

# change address sequence
CHANGE_ADDR_1 = 0x19 # step 1
CHANGE_ADDR_2 = 0xA0 # step 2
CHANGE_ADDR_3 = 0xAA # step 3
CHANGE_ADDR_4 = 0xA5 # step 4
LCD_ADDRESS_RANGE = range(0xC6, 0xCE, 2)

CUSTOM_CHAR = 0x1B

DOUBLE_KEYPAD_SCAN_RATE = 0x1C # Increases scan frequency to 20Hz
NORMAL_KEYPAD_SCAN_RATE = 0x1D # Returns scan frequency to 10Hz
