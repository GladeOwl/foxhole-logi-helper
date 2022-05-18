from typing import Dict


class Test:
    def __init__(self) -> None:
        self.one = 1
        self.two = 2
        self.three = 3

    def tester(self):
        pass


for t in Test().__dict__:
    print(t)
