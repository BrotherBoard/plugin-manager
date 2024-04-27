import babase
import bauiv1 as bui
import bauiv1lib.party
import random
import bascenev1 as bs

lmao = [
    "My bad",
    "Oops sry",
    "Sry didn't mean to",
    "My apologize sorry",
    "My mistake",
    "Oops, my bad!",
    "Sorry, that happens",
    "My fault, apologies!",
    "Oops, my mistake",
    "Ah I slipped",
    "My bad, didn't mean to.",
    "Ah, sry about that",
    "A- I did that my bad",
    "Sry u know I am",
    "Never did that on purpose, sry",
    "Sorry, my fault",
    "Sry lol",
    "Oops, forgive me sry",
    "Sorry, will try to do less",
    "Clearly didn't mean to, sry",
    "Sorry I oversighted",
    "Oops, my fault, my bad",
    "Sorry, didn't mean to.",
    "My bad, forgive the slip",
    "Sorry, didn't mean to mess up",
    "Oops, sorry lol",
    "Sorry and hoping for a np",
    "Ah sry sry my bad",
    "My bad, forgive the error",
    "Sorry, my fault entirely"]

class TheBrandNewUltraProMaxPartyWindow(bauiv1lib.party.PartyWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._last_sorry: float = 0.0
        self._shut_up_interval: float = 0
        bui.buttonwidget(
            parent=self._root_widget,
            size=(50, 35),
            scale = 0.7,
            label='Sorry',
            button_type='square',
            position=(self._width - 60, self._height - 83),
            on_activate_call=self._apologize
        )

    def _apologize(self):
        still = babase.apptime() - self._last_sorry
        if (still < self._shut_up_interval):
            bs.screenmessage(f"too fast, wait {str(self._shut_up_interval - still)[:5]}s")
            return
        bs.chatmessage(random.choice(lmao))
        self._last_sorry = babase.apptime()

# ba_meta require api 8
# ba_meta export plugin
class byBordd(babase.Plugin):
    def __init__(self):
        bauiv1lib.party.PartyWindow = TheBrandNewUltraProMaxPartyWindow
