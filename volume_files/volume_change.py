import win32con
import win32api
import time
class Volume_change:
    def __init__(self):
        pass
    
    def volume_up(self):
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
        win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)
    def volume_down(self):
        win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0)
        win32api.keybd_event(win32con.VK_VOLUME_DOWN, 0, win32con.KEYEVENTF_KEYUP)

    def set_volume_value(self, value: int) -> None:
        for _ in range(100):
            self.volume_down()
        self.mute()
        for i in range(int(value / 2)):
            win32api.keybd_event(win32con.VK_VOLUME_UP, 0)
            win32api.keybd_event(win32con.VK_VOLUME_UP, 0, win32con.KEYEVENTF_KEYUP)

    def mute(self):
        win32api.keybd_event(win32con.VK_VOLUME_MUTE, 0)
        