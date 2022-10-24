import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as plt
from tqdm import trange



class Mikrobe:
    def __init__(self, x=None, y=None, start_energi=100, genom=None):
        self._x = x
        self._y = y
        self._retning = np.random.randint(0, 8)

        if genom is None:
            tmp = np.random.uniform(0, 1, size=(7,))
            tmp /= np.sum(tmp)
            kumulativ_sum = 0
            self._genom = np.zeros_like(tmp)
            for i, p in enumerate(tmp):
                kumulativ_sum += p
                self._genom[i] = kumulativ_sum
        else:
            self._genom = genom

        self._alder = 0
        self._energi = start_energi


        self.posisjonsendring = [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
        ]

        self.energikostnader = [
                0,
                -1,
                -2,
                -4,
                -8,
                -4,
                -2,
                -1,
        ]
        
    @property
    def x(self):
        return self._x
        
    @x.setter
    def x(self, ny_x):
        self._x = ny_x
        
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, ny_y):
        self._y = ny_y
        
    @property
    def posisjon(self):
        return (self._x, self._y)
        
    @posisjon.setter
    def posisjon(self, ny_posisjon):
        x, y = ny_posisjon
        self._x = x
        self._y = y
        
    @property
    def alder(self):
        return self._alder
        
    @alder.setter
    def alder(self, ny_alder):
        self._alder = ny_alder

    @property
    def genom(self):
        return self._genom
        
    @property
    def retning(self):
        return self._retning

    @retning.setter
    def retning(self, ny_retning):
        self._retning = ny_retning
    
    @property
    def energi(self):
        return self._energi
    
    @energi.setter
    def energi(self, ny_energi):
        self._energi = ny_energi

def main():
    n_celler = 10
    mikrobe = Mikrobe(
            x=np.random.randint(0, n_celler),
            y=np.random.randint(0, n_celler),
    )

    print("posisjon =", mikrobe.posisjon)
    print("x =", mikrobe.x)
    print("y =", mikrobe.y)
    print("energi =", mikrobe.energi)
    print("alder =", mikrobe.alder)
    print("genom =", mikrobe.genom)


if __name__ == "__main__":
    main()
