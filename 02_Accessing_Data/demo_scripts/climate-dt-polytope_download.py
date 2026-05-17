from polytope.api import Client

client = Client(
    address="polytope.lumi.apps.dte.destination-earth.eu",
)


## Build the request: LINK(s) to where to find the parameters 

request = {
    "activity": "baseline",
    "class": "d1",
    "dataset": "climate-dt",
    "date": "20100102",
    "experiment": "hist",
    "expver": "0001",
    "generation": "2",
    "levtype": "sfc",
    "model": "ifs-fesom",
    "param": "167",
    "realization": "1",
    "resolution": "high",
    "stream": "clte",
    "time": "0000",
    "type": "fc",
}

# Download to a files in current directory
files = client.retrieve("destination-earth", request, f"download_polytope_test.grib")

## Alternative to just get in memory?
