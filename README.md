# python-LCD03

Python 3.x driver for the LCD03 20x4 display with 12C shield. Usable on Raspberry Pi and other similar devices.
[Device Reference](http://www.robot-electronics.co.uk/htm/Lcd03tech.htm)

## Usage

```
from LCD03.driver import LCD03Driver

lcd03 = LCD03Driver(address=0x63) # backlight is on by default
lcd03.clear()
lcd03.write_ascii("Hello Mars!")
```

## Credits
* Developed by Kingsley Ndiewo