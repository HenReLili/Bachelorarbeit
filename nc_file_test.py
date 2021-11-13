"""
Shows what happens in fft_basics_for_henri.py
https://askubuntu.com/questions/1081288/18-04-apt-get-install-python3-netcdf4
"""


import readin
import plot

from matplotlib import pyplot as plt


def main():
    lon, names = readin.datareader_nc("R5906590_001.nc", "LONGITUDE")
    print(names)
    print("longitude: ", lon)
    lat, names = readin.datareader_nc("R5906590_001.nc", "LATITUDE")
    print("latitude: ", lat)

    pres_ad, names = readin.datareader_nc("R5906590_001.nc", "PRES_ADJUSTED")

    psal_ad, names = readin.datareader_nc("R5906590_001.nc", "PSAL_ADJUSTED")
    plot.plot_profile(psal_ad[0], - pres_ad[0], "psal_ad_nc")

    temp_ad, names = readin.datareader_nc("R5906590_001.nc", "TEMP_ADJUSTED")
    plot.plot_profile(temp_ad[0], - pres_ad[0], "temp_ad_nc")

    pres, names = readin.datareader_nc("R5906590_001.nc", "PRES")
    psal, names = readin.datareader_nc("R5906590_001.nc", "PSAL")
    temp, names = readin.datareader_nc("R5906590_001.nc", "TEMP")
    print("pres: ", pres[0])
    print("pres_ad: ", pres_ad[0])
    print("temp: ", temp[0])
    print("temp_ad: ", temp_ad[0])
    print("psal: ", psal[0])
    print("psal_ad: ", psal_ad[0])

    #nn = np.linspace(1, len(pres_ad[0]), num=len(pres_ad[0]))
    plt.plot(pres_ad[0], pres[0])


if __name__ == "__main__":
    main()
