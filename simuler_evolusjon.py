from mikrobe import Mikrobe
from petriskive import Petriskive
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import trange

def tidsevolusjon(n_tidssteg, n_mikrober=5, n_celler=100, dE=10, time_delay=10, matfordeling="uniform"):
    petriskive = Petriskive(
        n_mikrober=n_mikrober,
        n_celler=n_celler,
        dE=dE,
        matfordeling=matfordeling,
    )
    x = []
    y = []
    n_mat = []
    n_mikrober = []
    tidssteg = []

    it = trange(n_tidssteg, leave=True)
    for t in it:
        it.set_description(f"antall mikrober = {len(petriskive.mikrober)}")
        x_tmp = []
        y_tmp = []
        mikrober = petriskive.mikrober
        for mikrobe in mikrober:
            x_tmp.append(mikrobe.x)
            y_tmp.append(mikrobe.y)
        x.append(x_tmp)
        y.append(y_tmp)
        petriskive.evolver_ett_tidssteg()

        if t % time_delay == 0:
            petriskive.distribuer_mat()

        n_mat.append(np.sum( 1.0 * (petriskive.mat > 0)))

        n_mikrober.append(len(petriskive.mikrober))
        tidssteg.append(t)
    return x, y, n_mat, n_mikrober, tidssteg
        
def create_images(x, y, n_celler):
    fig, ax = plt.subplots()
    imgs = []
    for n, (i, j) in enumerate(zip(x, y)):
        R = np.zeros(shape=(n_celler, n_celler))
        for k, l in zip(i, j):
            R[k, l] = 1

        if n == 0:
            imgs.append([ax.imshow(R, cmap="gray")])
        else:
            imgs.append([ax.imshow(R, animated=True, cmap="gray")])
    return fig, ax, imgs


def create_animation(fname, n_celler, x, y):
    fig, ax, imgs = create_images(x=x, y=y, n_celler=n_celler)
    ani = animation.ArtistAnimation(fig, imgs, blit=True)
    ani.save(fname, fps=60, writer="ffmpeg")
    plt.close()


def main(n_tidssteg, n_mikrober, dE, n_celler, time_delay):
    # petriskive.tidsevolusjon(n_tidssteg=10000)
    x, y, n_mat, n_mikrober, tidssteg = tidsevolusjon(n_tidssteg=n_tidssteg, n_mikrober=n_mikrober, dE=dE, n_celler=n_celler, matfordeling="garden_of_eden", time_delay=time_delay)
    create_animation(fname="animations/garden_of_eden_sim_500x500.mp4", n_celler=n_celler, x=x, y=y)
    plt.plot(tidssteg, n_mikrober, label="antall mikrober", color="red") 
    plt.plot(tidssteg, n_mat, label="antall bakterier (mat)", color="blue")
    plt.legend()
    plt.xlabel("tid")
    plt.ylabel("Antall")
    plt.savefig("rovdyr_vs_bytte.pdf")
    plt.close()
    # petriskive = Petriskive(n_mikrober=15, n_celler=500, matfordeling="garden_of_eden", dE=10) 
    # mat = petriskive._mat
    # plt.imshow(mat, cmap="gray")
    # plt.savefig("mat.pdf")
    # plt.close()

if __name__ == "__main__":
    # main(n_tidssteg=500, n_mikrober=2500, dE=40, n_celler=1000, time_delay=50)
    np.random.seed(101)
    main(
        n_tidssteg=2500,
        n_mikrober=1,
        dE=40,
        n_celler=500,
        time_delay=20,
    )

