
import earthkit.data
import concurrent.futures as cf

address="polytope.lumi.apps.dte.destination-earth.eu"


def makerequest(date):

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
        "date": f"{date}",
        "time": "0000"
    }
    return request


def getstuff(date):

    request = makerequest(date)

    ## Gets data to memory
    data = earthkit.data.from_source(
        "polytope",
        "destination-earth",
        request,
        stream=False,    
        address = address
    )

    ## save to file
    data.to_target("file",f"earthkit_test_download_parallel_{date}.grib")

    # return handle
    return data

dates_list = [
    "20100301",
    "20100302",
    "20100303",
    "20100304"
]


with cf.ThreadPoolExecutor(max_workers=4) as exe:
    futures = [exe.submit(getstuff, dt) for dt in dates_list]


handles = [ff.result() for ff in futures]
