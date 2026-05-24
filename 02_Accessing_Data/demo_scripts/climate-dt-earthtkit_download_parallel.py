
import earthkit.data
import concurrent.futures as cf

address="polytope.lumi.apps.dte.destination-earth.eu"


def makerequest(date):

    request = {
        "activity": "baseline",
        "class": "d1",
        "dataset": "climate-dt",
        "date": f"{date}",
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
    return request


def getstuff(date):

    request = makerequest(date)

    ## Gets data to memory
    data = earthkit.data.from_source(
        "polytope",
        "destination-earth",
        request,
        stream=False,    ## stream == true would return an iterator-like object
        address = address
    )

    ## save to file
    data.to_target("file",f"earthkit_test_download_parallel_{date}.grib")



dates_list = [
    "20100301",
    "20100302",
    "20100303",
    "20100304"
]

with cf.ThreadPoolExecutor(max_workers=4) as exe:
    future = [exe.submit(getstuff, dt) for dt in dates_list]

