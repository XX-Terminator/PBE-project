import sys
import i2c_lib
import lcddriver


def message(str):
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
    mgs=str.split('\n')
    lcd.lcd_display_string(mgs[0], 1)
    if len(mgs)>1:
        lcd.lcd_display_string(mgs[1], 2)
    if len(mgs)>2:
        lcd.lcd_display_string(mgs[2], 3)
    if len(mgs)>3:
        lcd.lcd_display_string(mgs[3], 4)
    if len(mgs)>4:
        print("El mensaje tienen mas de 4 líneas")
    
        
if __name__ == '__main__':

    message(str)
