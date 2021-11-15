"""
Executing the programm.
access-token: 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
"""


import readin
import calculator

from matplotlib import pyplot as plt
import numpy as np


def main():
    ID = readin.overviewreader(-60, -58, -130, -128)
    print(ID[5800])
    for i in ID:
        p_prof = readin.datareader_nc("{split}/profiles/D{full}.nc".format(split=i.split("_")[0], full=i), "PRES_ADJUSTED")[0]
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
        print("T: ", T_prof)
    

if __name__ == "__main__":
    main()
