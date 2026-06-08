import earthkit

address="polytope.lumi.apps.dte.destination-earth.eu"


def get_data(req):
    ## Gets data to memory
    d = earthkit.data.from_source(
        "polytope",
        "destination-earth",
        req,
        stream=False,
        address = address
    )
    return d

request1 = {
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

request2 = {
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
    "param": "168",
    "levtype": "sfc",
    "date": "20100102",
    "time": "0000"    
}


# Get the data
data = get_data(request1)
data2 = get_data(request2)


clen=40

print("-"*clen)
print(f"Inspect contents: data.ls()\n{'-'*clen}")
print(data.ls())

print(f"\n{'-'*clen}")
print(f"See request indices: data.indices()\n{'-'*clen}")
print(data.indices())

print(f"\n{'-'*clen}")
print(f"Convert to xarray: data.to_xarray()\n{'-'*clen}")
print(data.to_xarray())

print(f"\n{'-'*clen}")
print(f"Conver to numpy arrays: data.to_numpy\n{'-'*clen}")
print(data.to_numpy())

print(f"\n{'-'*clen}")
print(f"Also by using 'data.values'\n{'-'*clen}")
print(data.values)

print(f"\n{'-'*clen}")
print(f"Conversion to Pandas available by 'to_pandas()', but not always useful \n{'-'*clen}")

print(f"\n{'-'*clen}")
print(f"Concanate two data handles \n{'-'*clen}")

combined = data + data2
print(combined.ls())

