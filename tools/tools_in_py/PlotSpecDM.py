import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import griddata
from matplotlib import rc
import os
from matplotlib import ticker

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-2,2))

def plot_Spectra(filename,case,marker):

    data = np.genfromtxt(filename,unpack=True)
    energy = data[0]
    flux = data[1]
    energy = energy[flux>1e-60]
    flux = flux[flux>1e-60]
    plt.plot(energy,flux,marker,label=case,linewidth=2)

if __name__ == '__main__':
    # Filepath to results
    path = "/afs/ciemat.es/user/b/bernardos/GitHub/LMC/spectra/DM/"
    masses = [0.2,0.5,1,10,50,100]
    particle="W"

    for dm_mass in masses:
        # Build wisely the name of the file
        if (dm_mass < 1.0):
            masstr = str(int(dm_mass*1000))+"GeV";      
        else:
            masstr = str(int(dm_mass))+"TeV";
        
        filename = "flux"+particle+masstr+".txt"
        plot_Spectra(path+filename,masstr,"-")
        #plt.title("Spectrum of "+source)
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('Energy (MeV)')
        plt.ylabel('Flux $phcm^{-2}s^{-1}MeV^{-1}$')
        #plt.title("$b\overline{b}$ annihilation channel")
        plt.title("$W^{+}W^{-}}$ annihilation channel")
        plt.legend()
    plt.show()
