# -*- coding: utf-8 -*-
# Part of python-LCD03. See LICENSE file for full copyright and licensing details.

import LCD03.commands as lcd_cmd
import smbus
from time import sleep

DEVICE_ADDRESS = 0x63
COMMAND_REGISTER = 0x00

class LCD03Driver:

    def __init__(self, address = DEVICE_ADDRESS, backlight = True):
        self.address = address
        self.bus = smbus.SMBus(1)
        self.backlight = backlight
        if self.backlight:
            self.backlight_on()
        sleep(2)
        self.clear()

    def write(self, cmd):
        self.bus.write_byte_data(self.address, COMMAND_REGISTER, cmd)

    def write_ascii(self, input_str):
        for a in input_str:
            self.write(ord(a))

    def clear(self):
        self.write(lcd_cmd.CLEAR_SCREEN)

    def home(self):
        self.write(lcd_cmd.CURSOR_HOME)

    def set_cursor_index(self, position):
        if position < 0x01 or position > 0x50:
            raise ValueError("Position must be between 0x01 and 0x50")
        self.write(lcd_cmd.SET_CURSOR)
        self.write(position)

    def set_cursor_xy(self, x, y):
        if x < 1 or x > 4:
            raise ValueError("Row must be between 1 and 4")
        if y < 1 or y > 20:
            raise ValueError("Column must be between 1 and 20")
        
        self.write(lcd_cmd.SET_CURSOR_XY)
        self.write(x)
        self.write(y)

    def hide_cursor(self):
        self.write(lcd_cmd.HIDE_CURSOR)

    def show_underline_cursor(self):
        self.write(lcd_cmd.SHOW_UNDERLINE_CURSOR)

    def show_blinking_cursor(self):
        self.write(lcd_cmd.SHOW_BLINKING_CURSOR)

    def backspace(self):
        self.write(lcd_cmd.BACKSPACE)

    def tab(self):
        self.write(lcd_cmd.HORIZ_TAB)

    def one_row_down(self):
        self.write(lcd_cmd.SMART_LINE_FEED)

    def one_row_up(self):
        self.write(lcd_cmd.VERT_TAB)

    def enter(self):
        self.write(lcd_cmd.CARRIAGE_RETURN)

    def clear_column(self):
        """ Clear the current column and move the cursor right """
        self.write(lcd_cmd.CLEAR_COLUMN)

    def set_tab_size(self, size):
        if size < 1 or size > 10:
            raise ValueError("Tab size must be between 1 and 10")
        self.write(lcd_cmd.TAB_SET)
        self.write(size)

    def backlight_on(self):
        self.write(lcd_cmd.BACKLIGHT_ON)
        self.backlight = True

    def backlight_off(self):
        self.write(lcd_cmd.BACKLIGHT_OFF)
        self.backlight = False

    def disable_startup_msg(self):
        self.write(lcd_cmd.DISABLE_STARTUP_MSG)

    def enable_startup_msg(self):
        self.write(lcd_cmd.ENABLE_STARTUP_MSG)

    def change_addr(self, new_addr):
        if new_addr not in lcd_cmd.LCD_ADDRESS_RANGE:
            raise ValueError("Address must be in the even range 0xC6 to 0xCE")
        # command sequence to change the address
        self.write(lcd_cmd.CHANGE_ADDR_1)
        self.write(lcd_cmd.CHANGE_ADDR_2)
        self.write(lcd_cmd.CHANGE_ADDR_3)
        self.write(lcd_cmd.CHANGE_ADDR_4)
        # write the new address
        self.write(new_addr)

    def custom_char(self, char_pos, data):
        if char_pos < 128 or char_pos > 135:
            raise ValueError("Character position must be between 128 and 135")
        self.write(lcd_cmd.CUSTOM_CHAR)
        self.write(char_pos)
        # eight bytes of data
        # highest bit (7) is masked on
        # bit 5 and 6 are ignored
        # bits 0 to 4 are the line data
        for byte in data:
            # mask the highest bit
            byte = byte | 0x80
            self.write(byte)

    def keypad_scan_20hz(self):
        self.write(lcd_cmd.DOUBLE_KEYPAD_SCAN_RATE)

    def keypad_scan_10hz(self):
        self.write(lcd_cmd.NORMAL_KEYPAD_SCAN_RATE)