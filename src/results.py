import matplotlib.pyplot as plt
import numpy as np

def calc_results(port, sim_path, frequency_range):
    port.CalcPort(sim_path, frequency_range)

    s11 = port.uf_ref / port.uf_inc

    plt.plot(frequency_range/1e9, 20*np.log10(np.abs(s11)))
    plt.xlabel("Frequency (GHz)")
    plt.ylabel("S11 (dB)")
    plt.grid()
    plt.show()

    return