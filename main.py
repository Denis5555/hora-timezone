import kivy as kv  # Acrecentei depois como referência para não mostrar erro no PyCharm
from kivy.config import Config
Config.set("graphics", "resizable", True)
from kivy.utils import platform  # Acrecentei depois como referência para não mostrar erro no PyCharm
from kivy.app import App
from kivy.clock import Clock
from time import strftime
from kivy.core.window import Window
from kivy.lang import Builder
from datetime import datetime
from pytz import timezone
import pytz

# ===caso eu queira saber o formato das timezones:====
# import pytz
# for tz in pytz.all_timezones:
#     print(tz)
# =====================================================


Builder.load_file('clocklanguage.kv')
Window.size = (300, 600)
# Set the app size
def build(self):
    if (platform == 'android' or platform == 'ios'):  # Usei o or em vez de | para não mostrar erro no PyCharm
        Window.maximize()
    else:
        Window.size = (620, 1024)
    return kv


class Clocklanguage(App):
    def on_start(self):
        Clock.schedule_interval(self.update, 0)

    def update(self, tick):
        utc_time = datetime.utcnow()
        tz = timezone('Europe/Warsaw')
        hora = utc_time.replace(tzinfo=pytz.utc).astimezone(tz)

        horapl = hora.astimezone(timezone('Europe/Warsaw'))
        horapl = str(horapl)
        datahorapl = horapl[:-22]
        horapl = horapl[10:-13]
        self.root.ids.timepl.text = '\n' + f'[size=30]{horapl}[/size]' + ' ' + f'[size=15]\n{datahorapl}[/size]'

        horabr = hora.astimezone(timezone('Brazil/East'))
        horabr = str(horabr)
        datahorabr = horabr[:-22]
        horabr = horabr[10:-13]
        self.root.ids.timebr.text = '\n' + f'[size=30]{horabr}[/size]' + ' ' + f'[size=15]\n{datahorabr}[/size]'

        horaauq = hora.astimezone(timezone('Australia/Brisbane'))
        horaauq = str(horaauq)
        datahoraauq = horaauq[:-22]
        horaauq = horaauq[10:-13]
        self.root.ids.timeauq.text = '[size=15]Qld[/size]\n' + f'[size=30]{horaauq}[/size]' + ' ' + f'[size=15]\n{datahoraauq}[/size]'

        horaausyd = hora.astimezone(timezone('Australia/Sydney'))
        horaausyd = str(horaausyd)
        datahoraausyd = horaausyd[:-22]
        horaausyd = horaausyd[10:-13]
        self.root.ids.timeausyd.text = '[size=15]Syd/Mel[/size]\n' + f'[size=30] {horaausyd} [/size]' + ' ' + f'[size=15]\n{datahoraausyd}[/size]'


if __name__ == "__main__":
    Clocklanguage().run()









