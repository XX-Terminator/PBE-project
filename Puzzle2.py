import gi
import sys 
import Print_LCD
import lcddriver

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib


class Window(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Puzzle 2")
        self.set_size_request(400, 200)
        self.timeout_id = None
        esp = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        
        self.add(esp)
        write = Gtk.Label(label="Escriba un texto de hasta 4 líneas(max 20 caracteres/línea)")
        esp.pack_start(write, True, True, 0)
        
        self.entry = Gtk.TextView()
        esp.pack_start(self.entry, True, True, 0)

        wind = Gtk.Box(spacing=2)
        esp.pack_start(wind, True, True, 0)

        self.button = Gtk.Button(label="Print LCD")
        self.button.connect("clicked", self.click)
        wind.pack_start(self.button, True, True, 0)
        
    def click(self, widget):
            Print_LCD.message(self.entry.get_buffer().get_text(self.entry.get_buffer().get_start_iter(), self.entry.get_buffer().get_end_iter(), True))
            print(self.entry.get_buffer().get_text(self.entry.get_buffer().get_start_iter(), self.entry.get_buffer().get_end_iter(), True))    

if __name__ == '__main__':
    final = Window()
    final.connect("destroy", Gtk.main_quit)
    final.show_all()
    Gtk.main()
    lcd = lcddriver.lcd()
    lcd.lcd_clear()
