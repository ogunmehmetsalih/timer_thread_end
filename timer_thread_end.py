import threading
import time

class TimerThread(threading.Thread):
    def __init__(self, thread_id, timer, timeout_value):
        super().__init__()
        self.thread_id = thread_id
        self.timer = timer
        self.timeout_value = timeout_value
        self.timeout = False

    def run(self):
        stime = time.time()
        print("Thread {} -> Başladı.".format(self.thread_id))

        while True:
            etime = time.time()
            if etime - stime >= self.timer:
                break
            if etime - stime >= self.timeout_value:
                self.timeout = True
                break

        print("Thread {} -> Bitti. TimeOut: {}".format(self.thread_id, self.timeout))


def sthread(threads):
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    thId_thsecond_timeout = [(1, 5,10), (2, 8, 9), (3, 10,5)]

    listThread = []
    for thread_id, timer, timeout_value in thId_thsecond_timeout:
        thread = TimerThread(thread_id, timer, timeout_value)
        listThread.append(thread)

    sthread(listThread)
    print("Tüm threadler tamamlandı.")

    for thread in listThread:
        if thread.timeout:
            print("Thread {} TimeOut oldu.".format(thread.thread_id))
