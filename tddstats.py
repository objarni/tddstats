import colors
import time

RED, GREEN, BLUE = range(3)


class TDDSession:
    def __init__(self, timer=None):
        self.timer = timer or time.time
        self.session_log = None

    def total_time(self):
        return sum(t[1] for t in self.session_log.get_log())

    def click(self):
        if self.session_log is None:
            self.session_log = SessionLog(start_time=self.timer())
        else:
            self.session_log.switch(time=self.timer())

    def sum_red_green_blue(self):
        log = self.session_log.get_log()
        sums = [sum(t[1] for t in log
                    if t[0] == value)
                for value in range(3)]
        return tuple(sums)

    def percents(self):
        total = self.total_time()
        percents = [int(value / total * 100)
                    for value in self.sum_red_green_blue()]
        return tuple(percents)

    def report(self):
        (r, g, b) = self.sum_red_green_blue()
        (pr, pg, pb) = self.percents()
        return f"""--- SESSION SUMMARY ---
Total time:        {self.total_time():1.1f} s
Adding tests:      {b:1.1f} s ({pb}%)
Making them pass:  {r:1.1f} s ({pr}%)
Refactoring:       {g:1.1f} s ({pg}%)
"""


class SessionLog:
    def __init__(self, start_time):
        self.mode = BLUE
        self.time = start_time
        self.log = []

    def switch(self, time):
        dt = time - self.time
        self.time = time
        self.log.append((self.mode, dt))
        self.mode = (self.mode + 1) % 3

    def get_log(self):
        return self.log


if __name__ == '__main__':
    session = TDDSession()
    print("TDD stats session.")
    print("Press enter to start session (in blue, add a test).")
    print("Press enter to switch state (to red, then green, then blue again etc.).")
    print("Type Q and press enter at any time to stop session.")
    input("[waiting for first enter]")
    mode = BLUE
    mode_names = "BLUE RED GREEN".lower().split()
    mode_desc = ["add a test, the fox says", "quickly make all tests pass, says the rabbit and runs", "enjoy refactoring, cat meows"]
    while True:
        session.click()
        mode = (mode + 1) % 3
        color = mode_names[mode]
        desc = mode_desc[mode]
        print(colors.color(f"In mode: {color} ({desc})", bg=color))
        ans = input().upper()
        if ans == "Q":
            print(session.report())
            break
