import threading
from queue import Queue


# for customization-purposes we'll use the strategy-pattern: https://www.oodesign.com/strategy-pattern/
class Adapter:
    def __init__(self):
        self.message_queue = Queue()

    def __str__(self):
        return 'Adapter'

    def start(self):
        pass

    def stop(self):
        pass


class SpeakingAdapter(Adapter):
    def start(self):
        pass

    def stop(self):
        pass

    def __str__(self):
        return 'SpeakingAdapter'


class LoggingAdapter(Adapter):
    def start(self):
        while True:
            message = self.message_queue.get()
            if message == "speak":
                print("Caren started logging...")
            elif message == "stop":
                break

    def __str__(self):
        return 'LoggingAdapter'


class OLEDDisplayAdapter(Adapter):
    def start(self):
        while True:
            message = self.message_queue.get()
            if message == "display":
                print("OLED DISPLAY started...")
            elif message == "stop":
                break

    def __str__(self):
        return 'OLEDDisplayAdapter'


class ShowWindowAdapter(Adapter):
    def start(self):
        while True:
            message = self.message_queue.get()
            if message == "show":
                print("Main window gets displayed...")
            elif message == "stop":
                break

    def __str__(self):
        return 'ShowWindowAdapter'


class Karen:
    def __init__(self, speaking=False, showing_window=False, displaying_oled=False, logging_messages=False):
        self._message_queue = Queue()
        self._adapters = []

        if speaking:
            self._adapters.append(SpeakingAdapter())
        if showing_window:
            self._adapters.append(ShowWindowAdapter())
        if displaying_oled:
            self._adapters.append(OLEDDisplayAdapter())
        if logging_messages:
            self._adapters.append(LoggingAdapter())

    def start(self):
        print("Starting Karen...")
        for adapter in self._adapters:
            threading.Thread(target=adapter.start, daemon=True).start()

    def print_adapters(self):
        for adapter in self._adapters:
            print(adapter.__str__())

    def stop(self):
        for _ in self._adapters:
            self._message_queue.put("stop")

