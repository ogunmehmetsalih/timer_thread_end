import threading
import time

class Timer(threading.Thread):
    def __init__(self, timeout_value):
        super().__init__()
        self.timeout_value = timeout_value
        self.timeout = False
        self.thread = threading.Thread(target=self.run, args=(self.timeout_value))

    def run(self, timeout_value):
        stime = time.time()
        print("Timer runned. Timeout: {} second".format(timeout_value))

        while True:
            etime = time.time()
            if etime - stime >= timeout_value:
                self.timeout = True
                break

        print("Timer Completed. Timeout: {}".format(timeout_value))

if __name__ == "__main__":
    timer1 = Timer(timeout_value=5)
    timer2 = Timer(timeout_value=10)
    timer3 = Timer(timeout_value=15)

    timer_threads = [timer1.thread, timer2.thread, timer3.thread]

    for timer_thread in timer_threads:
        timer_thread.start()

    for timer_thread in timer_threads:
        timer_thread.join()

    if timer1.timeout:
        print("Timer 1 -> Timeout")
    if timer2.timeout:
        print("Timer 2 -> Timeout")
    if timer3.timeout:
        print("Timer 3 -> Timeout")

