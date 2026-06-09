from polytope.api import Client

client = Client(
    address="polytope.lumi.apps.dte.destination-earth.eu",
)

request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "model": "ifs-fesom",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "type": "fc",
    "param": "167",
    "levtype": "sfc",
    "date": "20100102",
    "time": "0000"
}

# Download to a files in current directory
files = client.retrieve("destination-earth", request, "download_polytope_test.grib")

