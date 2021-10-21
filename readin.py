"""
reads data
"""

import os.path
import netcdf4 as nc4


def datareader_nc(filename):

    nc = nc4.Dataset(os.path.join("measurements", filename), "r")

    # print variable names (see Argo manual for reference of your variables)
    print(nc.variables.keys())

    # load a variable
    #variable1 = nc.variables["variable_name"][:]

    #   close file again
    nc.close()


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
