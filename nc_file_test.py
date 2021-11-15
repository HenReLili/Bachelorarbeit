"""
Shows what happens in fft_basics_for_henri.py
https://askubuntu.com/questions/1081288/18-04-apt-get-install-python3-netcdf4
"""


import readin
import plot

from matplotlib import pyplot as plt


def main():
    lon, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "LONGITUDE")
    print(names)
    print("longitude: ", lon)
    lat, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "LATITUDE")
    print("latitude: ", lat)

    pres_ad, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "PRES_ADJUSTED")

    psal_ad, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "PSAL_ADJUSTED")
    plot.plot_profile(psal_ad, - pres_ad, "psal_ad_nc")

    temp_ad, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "TEMP_ADJUSTED")
    plot.plot_profile(temp_ad, - pres_ad, "temp_ad_nc")

"""    pres, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "PRES")
    psal, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "PSAL")
    temp, names = readin.datareader_nc("6901658/profiles/D6901658_001.nc", "TEMP")
    print("pres: ", pres)
    print("pres_ad: ", pres_ad)
    print("temp: ", temp)
    print("temp_ad: ", temp_ad)
    print("psal: ", psal)
    print("psal_ad: ", psal_ad)

    #nn = np.linspace(1, len(pres_ad), num=len(pres_ad))
    plt.plot(pres_ad[0], pres)"""


if __name__ == "__main__":
    main()
