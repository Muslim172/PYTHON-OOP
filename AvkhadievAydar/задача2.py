class Button:
    def __init__(self):
        self.clicks = 0
    def click(self):
        self.clicks += 1
    def click_count(self):
        return self.clicks
    def reset(self):
        self.clicks = 0

btn = Button()
btn.click()
btn.click()
btn.click()
print(btn.click_count())
btn.reset()
print(btn.click_count())