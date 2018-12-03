import threading
import time

class KSNonceTimestampManipulator:
    def __init__(self):
        self.current_timestamp = int(time.time())
        self.current_nonce = 1
        self.destroyed = False
        threading._start_new_thread(self.change_timestamp_and_reset_nonce_thread, ())

    def get_next_nonce(self):
        self.current_nonce += 1
        return self.current_nonce

    def get_current_nonce(self):
        return self.current_nonce

    def get_current_timestamp(self):
        return self.current_timestamp

    def destroy(self):
        self.destroyed = True

    def change_timestamp_and_reset_nonce_thread(self):
        while not self.destroyed:
            self.current_timestamp = int(time.time())
            self.current_nonce = 1
            time.sleep(1)