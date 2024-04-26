from karen.Karen import Karen
import time


def main():
    karen = Karen(speaking=True, showing_window=True, displaying_oled=True, logging_messages=True)
    karen.start()

    karen.print_adapters()

    time.sleep(5)

    karen.stop()


if __name__ == "__main__":
    main()
