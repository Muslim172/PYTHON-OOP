class BigBell:
    def init(self):
        self.soundtype = "ding"
    def sound(self):
        if self.soundtype == "ding":
            print("ding")
            self.soundtype = "dong"
        else:
            print("dong")
            self.soundtype = "ding"

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
bell.sound()