#Import LCD library
from RPLCD import i2c
#Import sleep library
from time import sleep

class LCD:
  def imprimir_pantalla(self):
    #constants to initialise the LCD
    lcdmode= 'i2c'
    cols=20
    rows=4
    charmap='A00'
    address=0*27
    port= 1
    i=0
    
    #Initialise the LCD
    lcd= i2c.CharLCD(i2c_expander,address,port=port, charmap=charmap, cols=cols, rows=rows)
    
    #Write a string on first line and move to the next line
    lcd.write_string('Escribe algo:')
    while i<4:
      txt=input("Escribe algo: ")
      length=len(txt)
      if i==0:
        lcd.clear()
      if length <=cols:
        lcd.write_string(txt)
        lcd.crlf()
        i=i+1
      else:
        print("Frase muy larga")
    sleep(5)
    #Switch off blacklight
    lcd.blacklight_enabled= False
  
    #Clear the LCD screen
    lcd.close(clear=True)
    
if __name__=="__main__":
  lcd=LCD()
  lcd.imprimir_pantalla()

  
