"""
reads data
"""

import os.path
import netCDF4 as nc4
import pandas as pd


def overviewreader(latmin=-71, latmax=11, lonmin=176, lonmax=-116):
    """
    latmin: unten; lonmin: links
    """
    file = pd.read_csv("measurements/data/overview.csv")
    if lonmin < 0 or lonmax > 0:
        queried = file.query('{a} < LON0 < {b} and {c} < LAT0 < {d}'.format(a=lonmin, b=lonmax, c=latmin, d=latmax))
    else:
        queried = file.query('{a} < LON0 or {b} > LON0'.format(a=lonmin, b=lonmax))
        queried = queried.query('{c} < LAT0 < {d}'.format(c=latmin, d=latmax))
    return queried["ID"]


def datareader_nc(filename, varname):
    nc = nc4.Dataset(os.path.join("measurements/data/floats", filename), "r")

    # print variable names (see Argo manual for reference of your variables)
    # print(nc.variables.keys())

    # load a variable
    variable = nc.variables[varname][:]

    #   close file again
    nc.close()
    return variable[0], nc.variables.keys()


def datareader_profile(datanumber):
    dataname = "test_profile_{number}".format(number=datanumber)
    fp = open(os.path.join("measurements", dataname + ".dat"))
    readdata = fp.readlines()
    fp.close

    data = readdata[1:]
    pressure = []
    temperature = []

    for i in range(0, len(data)):
        data[i] = data[i].split()
        for j in range(0, 2):
            data[i][j] = float(data[i][j].strip(";"))
            continue
        pressure.append(-data[i][0])
        temperature.append(data[i][1])

    return pressure, temperature, dataname


def datareader_timeseries():
    dataname = "test_timeseries"
    fp = open(os.path.join("measurements", dataname + ".dat"))
    readdata = fp.readlines()
    fp.close

    data = readdata[1:]
    time = []
    pressure = []
    temperature = []

    for i in range(0, len(data)):
        data[i] = data[i].split()
        for j in range(0, 3):
            data[i][j] = float(data[i][j].strip(";"))
            continue
        time.append(data[i][0])
        pressure.append(data[i][1])
        temperature.append(data[i][2])

    return time, pressure, temperature, dataname
