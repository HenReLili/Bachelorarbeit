"""
Executing the programm.
access-token: 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
valid until: 22.02.2022
"""


import readin
import calculator

from matplotlib import pyplot as plt
import numpy as np
import os.path


def main():
    ID = readin.overviewreader(-60, -58, -130, -128)
    print(ID[5800])
    for i in ID:
        """p_prof = readin.datareader_nc("{split}/profiles/D{full}.nc".format(split=i.split("_")[0], full=i), "PRES_ADJUSTED")[0]
        p_prof = -p_prof
        T_prof = readin.datareader_nc("{split}/profiles/D{full}.nc".format(split=i.split("_")[0], full=i), "TEMP_ADJUSTED")[0]
        counter = 0
        for j in range(0, len(T_prof)):
            if type(T_prof[j-counter]) is not float:
                np.delete(T_prof, j-counter)
                np.delete(p_prof, j)
                counter +=1
        grad = calculator.grad(p_prof, T_prof)
        print("grad: ", grad)
        print("p: ", len(p_prof))
        print("T: ", T_prof)""" # Bitte _ADJUSTED nehmen, sobald geklärt wie mit fehlenden Werten umzugehen
        p_prof = readin.datareader_nc("{split}/profiles/D{full}.nc".format(split=i.split("_")[0], full=i), "PRES")[0]
        p_prof = -p_prof
        T_prof = readin.datareader_nc("{split}/profiles/D{full}.nc".format(split=i.split("_")[0], full=i), "TEMP")[0]
        # plot the measuremnts of the profile
        plt.plot(T_prof, p_prof)
        p_prof, T_prof = calculator.linfit(p_prof, T_prof)
        grad = calculator.grad(p_prof, T_prof)
        print("grad: ", grad)
        #print("T: ", T_prof)
        # plot the curve fit
        plt.plot(T_prof, p_prof)
        plt.savefig(os.path.join("plots", "{a}th_test".format(a=i)))
        plt.show()
    """
    f = open("test.txt", "w")
    for j in range(0, len(T_prof)):
        f.write("{b}: {a}\n".format(a=T_prof[j], b=p_prof[j]))"""

if __name__ == "__main__":
    main()
