from mikrobe import Mikrobe
import numpy as np
from tqdm import trange


class Petriskive:
    def __init__(self, n_mikrober, n_celler, dE, mat_delay=10, matfordeling="uniform"):
        self._mikrober = [
                Mikrobe(
                    x=np.random.randint(0, n_celler), 
                    y=np.random.randint(0, n_celler),
                ) for _ in range(n_mikrober)
        ]
        
        self._n_celler = n_celler
        self._n_mikrober = n_mikrober
        self._matfordeling = "uniform"
        self._mat = np.zeros(shape=(self._n_celler, self._n_celler)) 
        self._dE = dE 

        self._minimums_alder = 5 
        self._minimums_energi = 1000
        self._max_alder = 40 
        self._max_energi = 1500
        self._mat_delay = mat_delay
        self._energi_per_reproduksjon = 100 

        if matfordeling == "uniform":
            self.distribuer_mat = self.distribuer_mat_uniform

        if matfordeling == "garden_of_eden":
            self.distribuer_mat = self.distribuer_mat_garden_of_eden

        if matfordeling == "linjer":
            self.distribuer_mat = self.distribuer_mat_linjer


        self.distribuer_mat()

    def distribuer_mat_linjer(self):
        self._mat[int(0.25 * self._n_celler):int(0.3 * self._n_celler), :] += 1
        self._mat[:, int(0.25 * self._n_celler):int(0.3 * self._n_celler)] += 1
        self._mat[int(0.75 * self._n_celler):int(0.8 * self._n_celler), :] += 1
        self._mat[:, int(0.75 * self._n_celler):int(0.8 * self._n_celler)] += 1


    def distribuer_mat_uniform(self):
        self._mat += np.random.randint(0, 2, size=(self._n_celler, self._n_celler))
        return None

    def distribuer_mat_garden_of_eden(self): 
        # idx = np.random.randint(int(0.45 * self._n_celler), int(0.55 * self._n_celler), size=(self._n_celler, self._n_celler))
        idx = (
            np.random.randint(int(0.45 * self._n_celler), int(0.55 * self._n_celler), size=int(0.1 * self._n_celler) ** 2),
            np.random.randint(int(0.45 * self._n_celler), int(0.55 * self._n_celler), size=int(0.1 * self._n_celler) ** 2),
        )
        tmp = np.zeros(shape=(self._n_celler, self._n_celler))
        tmp[idx] = 50 
        self._mat += tmp + np.random.randint(0, 2) * np.random.randint(0, 2, size=(self._n_celler, self._n_celler))
        return None

    def neste_posisjon(self, mikrobe):
        retning = mikrobe.retning
        r = np.random.uniform()
        retningsendring = None
        for i, p in enumerate(mikrobe.genom):
            if r > p:
                retningsendring = i
                break
        if retningsendring is None:
            retningsendring = 7

        ny_retning = (retning + retningsendring) % 8
        mikrobe.retning = ny_retning
        energi_endring = mikrobe.energikostnader[abs(ny_retning - retning)]
        mikrobe.energi += energi_endring
        dx, dy = mikrobe.posisjonsendring[mikrobe.retning]
        mikrobe.x = (mikrobe.x + dx) % self._n_celler
        mikrobe.y = (mikrobe.y + dy) % self._n_celler
        return mikrobe


    def evolver_ett_tidssteg(self):
        # tmp = self._mikrober[:]
        for mikrobe in self._mikrober:
            if self._mat[mikrobe.posisjon] > 0 and mikrobe.energi < 1500:
                mikrobe.energi += self._dE
                self._mat[mikrobe.posisjon] -= 1
            mikrobe = self.neste_posisjon(mikrobe)
            mikrobe.alder += 1
        
        # Sjekk om mikrobene kan reprodusere eller skal dø
        for mikrobe in self._mikrober:
            self.mikrobe_reproduksjon(mikrobe)
            if mikrobe.alder >= self._max_alder or mikrobe.energi <= 0:
                self._mikrober.remove(mikrobe) # Mikrober dør av alderdom eller næringsmangel
    
    def mikrobe_reproduksjon(self, mikrobe):
        if mikrobe.alder > self._minimums_alder and mikrobe.energi > self._minimums_energi:
            mikrobe.energi -= self._energi_per_reproduksjon
            if np.random.uniform() >= 0.5:
                self._mikrober.append(
                    Mikrobe(
                        x=mikrobe.x,
                        y=mikrobe.y,
                        genom=mikrobe.genom,
                    )
                )
            else:
                self._mikrober.append(
                    Mikrobe(
                        x=mikrobe.x,
                        y=mikrobe.y,
                        genom=None,
                    )
                )
    


    @property
    def mikrober(self):
        return self._mikrober


            
            
            
            
