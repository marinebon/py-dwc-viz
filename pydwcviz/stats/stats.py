"""
stats: visualize distribution of records and environmental parameters
"""
import pandas as pd
from ..utils import get, obis_base_url
import matplotlib.pyplot as plt
import plotly.express as px

def get_records(
    scientificname = None,
    taxonid=None,
    areaid=None,
    datasetid=None,
    nodeid=None,
    startdate=None,
    enddate=None,
    startdepth=None,
    enddepth=None,
    geometry=None,
    redlist=None,
    hab=None,
    wrims=None,
    dropped=None,
    absence=None,
    flags=None,
    exclude=None,
    **kwargs,
    ):
    """

    Get basic statistics for occurrence records.

    :param scientificname: [string] Scientific name. Leave empty to include all taxa.
    :param taxonid: [string] Taxon AphiaID.
    :param areaid: [string] Area ID.
    :param datasetid: [string] Dataset UUID.
    :param nodeid: [string] Node UUID.
    :param startdate: [string] Start date formatted as YYYY-MM-DD.
    :param enddate: [string] End date formatted as YYYY-MM-DD.
    :param startdepth: [integer] Start depth, in meters.
    :param enddepth: [integer] End depth, in meters.
    :param geometry: [string] Geometry, formatted as WKT or GeoHash.
    :param redlist: [boolean] Red List species only, true/false.
    :param hab: [boolean] HAB species only, true/false.
    :param wrims: [boolean] WRiMS species only, true/false.
    :param dropped: [string] Include dropped records (include) or get dropped records exclusively (true).
    :param absence: [string] Include absence records (include) or get absence records exclusively (true).
    :param flags: [string] Comma separated list of quality flags which need to be set.
    :param exclude: [string] Comma separated list of quality flags to be excluded.

    ::Usage

    """
    args = {
        "scientificname":	scientificname,
        "taxonid":	taxonid,
        "areaid":	areaid,
        "datasetid":	datasetid,
        "nodeid":	nodeid,
        "startdate":	startdate,
        "enddate":	enddate,
        "startdepth":	startdepth,
        "enddepth":	enddepth,
        "geometry":	geometry,
        "redlist":	redlist,
        "hab":	hab,
        "wrims":	wrims,
        "dropped":	dropped,
        "absence":	absence,
        "flags":	flags,
        "exclude":	exclude,
    }
    out = get(f'{obis_base_url}/statistics',args, **kwargs)
    return out

def get_years(
    scientificname = None,
    taxonid=None,
    areaid=None,
    datasetid=None,
    nodeid=None,
    startdate=None,
    enddate=None,
    startdepth=None,
    enddepth=None,
    geometry=None,
    redlist=None,
    hab=None,
    wrims=None,
    dropped=None,
    absence=None,
    flags=None,
    exclude=None,
    **kwargs,
    ):
    """
    Get number of presence records per year.

    :param scientificname: [string] Scientific name. Leave empty to include all taxa.
    :param taxonid: [string] Taxon AphiaID.
    :param areaid: [string] Area ID.
    :param datasetid: [string] Dataset UUID.
    :param nodeid: [string] Node UUID.
    :param startdate: [string] Start date formatted as YYYY-MM-DD.
    :param enddate: [string] End date formatted as YYYY-MM-DD.
    :param startdepth: [integer] Start depth, in meters.
    :param enddepth: [integer] End depth, in meters.
    :param geometry: [string] Geometry, formatted as WKT or GeoHash.
    :param redlist: [boolean] Red List species only, true/false.
    :param hab: [boolean] HAB species only, true/false.
    :param wrims: [boolean] WRiMS species only, true/false.
    :param dropped: [string] Include dropped records (include) or get dropped records exclusively (true).
    :param absence: [string] Include absence records (include) or get absence records exclusively (true).
    :param flags: [string] Comma separated list of quality flags which need to be set.
    :param exclude: [string] Comma separated list of quality flags to be excluded.

    ::Usage

    """
    args = {
        "scientificname":	scientificname,
        "taxonid":	taxonid,
        "areaid":	areaid,
        "datasetid":	datasetid,
        "nodeid":	nodeid,
        "startdate":	startdate,
        "enddate":	enddate,
        "startdepth":	startdepth,
        "enddepth":	enddepth,
        "geometry":	geometry,
        "redlist":	redlist,
        "hab":	hab,
        "wrims":	wrims,
        "dropped":	dropped,
        "absence":	absence,
        "flags":	flags,
        "exclude":	exclude,
    }
    out = get(f'{obis_base_url}/statistics/years',args, **kwargs)
    return out

def get_env(
    scientificname = None,
    taxonid=None,
    areaid=None,
    datasetid=None,
    nodeid=None,
    startdate=None,
    enddate=None,
    startdepth=None,
    enddepth=None,
    geometry=None,
    redlist=None,
    hab=None,
    wrims=None,
    dropped=None,
    absence=None,
    flags=None,
    exclude=None,
    **kwargs,
    ):
    """
    Get number of records per SST, SSS or depth bin.

    :param scientificname: [string] Scientific name. Leave empty to include all taxa.
    :param taxonid: [string] Taxon AphiaID.
    :param areaid: [string] Area ID.
    :param datasetid: [string] Dataset UUID.
    :param nodeid: [string] Node UUID.
    :param startdate: [string] Start date formatted as YYYY-MM-DD.
    :param enddate: [string] End date formatted as YYYY-MM-DD.
    :param startdepth: [integer] Start depth, in meters.
    :param enddepth: [integer] End depth, in meters.
    :param geometry: [string] Geometry, formatted as WKT or GeoHash.
    :param redlist: [boolean] Red List species only, true/false.
    :param hab: [boolean] HAB species only, true/false.
    :param wrims: [boolean] WRiMS species only, true/false.
    :param dropped: [string] Include dropped records (include) or get dropped records exclusively (true).
    :param absence: [string] Include absence records (include) or get absence records exclusively (true).
    :param flags: [string] Comma separated list of quality flags which need to be set.
    :param exclude: [string] Comma separated list of quality flags to be excluded.

    ::Usage

    """
    args = {
        "scientificname":	scientificname,
        "taxonid":	taxonid,
        "areaid":	areaid,
        "datasetid":	datasetid,
        "nodeid":	nodeid,
        "startdate":	startdate,
        "enddate":	enddate,
        "startdepth":	startdepth,
        "enddepth":	enddepth,
        "geometry":	geometry,
        "redlist":	redlist,
        "hab":	hab,
        "wrims":	wrims,
        "dropped":	dropped,
        "absence":	absence,
        "flags":	flags,
        "exclude":	exclude,
    }
    out = get(f'{obis_base_url}/statistics/env',args, **kwargs)
    return out

def get_qc(
    scientificname = None,
    taxonid=None,
    areaid=None,
    datasetid=None,
    nodeid=None,
    startdate=None,
    enddate=None,
    startdepth=None,
    enddepth=None,
    geometry=None,
    redlist=None,
    hab=None,
    wrims=None,
    dropped=None,
    absence=None,
    flags=None,
    exclude=None,
    **kwargs,
    ):
    """
    Get a QC summary, including missing or invalid values, number of records on land, 
    number of non marine records and number of records without Aphia ID.
    
    :param scientificname: [string] Scientific name. Leave empty to include all taxa.
    :param taxonid: [string] Taxon AphiaID.
    :param areaid: [string] Area ID.
    :param datasetid: [string] Dataset UUID.
    :param nodeid: [string] Node UUID.
    :param startdate: [string] Start date formatted as YYYY-MM-DD.
    :param enddate: [string] End date formatted as YYYY-MM-DD.
    :param startdepth: [integer] Start depth, in meters.
    :param enddepth: [integer] End depth, in meters.
    :param geometry: [string] Geometry, formatted as WKT or GeoHash.
    :param redlist: [boolean] Red List species only, true/false.
    :param hab: [boolean] HAB species only, true/false.
    :param wrims: [boolean] WRiMS species only, true/false.
    :param dropped: [string] Include dropped records (include) or get dropped records exclusively (true).
    :param absence: [string] Include absence records (include) or get absence records exclusively (true).
    :param flags: [string] Comma separated list of quality flags which need to be set.
    :param exclude: [string] Comma separated list of quality flags to be excluded.

    ::Usage

    """
    args = {
        "scientificname":	scientificname,
        "taxonid":	taxonid,
        "areaid":	areaid,
        "datasetid":	datasetid,
        "nodeid":	nodeid,
        "startdate":	startdate,
        "enddate":	enddate,
        "startdepth":	startdepth,
        "enddepth":	enddepth,
        "geometry":	geometry,
        "redlist":	redlist,
        "hab":	hab,
        "wrims":	wrims,
        "dropped":	dropped,
        "absence":	absence,
        "flags":	flags,
        "exclude":	exclude,
    }
    out = get(f'{obis_base_url}/statistics/qc',args, **kwargs)
    return out
    

def get_composition(
    scientificname = None,
    taxonid=None,
    areaid=None,
    datasetid=None,
    nodeid=None,
    startdate=None,
    enddate=None,
    startdepth=None,
    enddepth=None,
    geometry=None,
    redlist=None,
    hab=None,
    wrims=None,
    dropped=None,
    absence=None,
    flags=None,
    exclude=None,
    **kwargs,
    ):
    """
    Get an overview of taxonomic composition.
    
    :param scientificname: [string] Scientific name. Leave empty to include all taxa.
    :param taxonid: [string] Taxon AphiaID.
    :param areaid: [string] Area ID.
    :param datasetid: [string] Dataset UUID.
    :param nodeid: [string] Node UUID.
    :param startdate: [string] Start date formatted as YYYY-MM-DD.
    :param enddate: [string] End date formatted as YYYY-MM-DD.
    :param startdepth: [integer] Start depth, in meters.
    :param enddepth: [integer] End depth, in meters.
    :param geometry: [string] Geometry, formatted as WKT or GeoHash.
    :param redlist: [boolean] Red List species only, true/false.
    :param hab: [boolean] HAB species only, true/false.
    :param wrims: [boolean] WRiMS species only, true/false.
    :param dropped: [string] Include dropped records (include) or get dropped records exclusively (true).
    :param absence: [string] Include absence records (include) or get absence records exclusively (true).
    :param flags: [string] Comma separated list of quality flags which need to be set.
    :param exclude: [string] Comma separated list of quality flags to be excluded.

    ::Usage

    """
    args = {
        "scientificname":	scientificname,
        "taxonid":	taxonid,
        "areaid":	areaid,
        "datasetid":	datasetid,
        "nodeid":	nodeid,
        "startdate":	startdate,
        "enddate":	enddate,
        "startdepth":	startdepth,
        "enddepth":	enddepth,
        "geometry":	geometry,
        "redlist":	redlist,
        "hab":	hab,
        "wrims":	wrims,
        "dropped":	dropped,
        "absence":	absence,
        "flags":	flags,
        "exclude":	exclude,
    }
    out = get(f'{obis_base_url}/statistics/composition',args, **kwargs)
    return out

def dist_years(data, interactive=False, **kwargs):
    """
    Get a bar graph of distribution of number of records per year

    :param data: [Dict] Ingest data grabbed from get_years() function.

    :return: a matplotlib Axes object or plotly Figure object

    ::Usage

        from pydwcviz import stats
        # return a matplotlib.pyplot plot when interactive=False
        stats.dist_years(stats.get_years(taxonid = 1071), interactive=False)
        
        # return a plotly object when interactive=True
        stats.dist_years(stats.get_years(taxonid = 1071), interactive=True)
    """
    df = pd.DataFrame(data)
    if not interactive:
        ax = plt.bar(x = df['year'], height = df['records'])
        plt.xlabel("year")
        plt.ylabel("records")
        return ax
    
    fig = px.bar(data, x = "year", y = "records")
    return fig

def dist_env(data, parameter, interactive=False, **kwargs):
    """
    Get a distribution of environmental parameters: SST, SSS and depth
    
    :param data: [Dict] Ingest data grabbed from get_env() function.
    :param parameter: [String] One of "sst", "sss", or "depth" to visualize its distribution

    :return: a matplotlib Axes object or plotly Figure object

    ::Usage

        from pydwcviz import stats
        # return a matplotlib.pyplot Axes object when interactive=False
        stats.dist_env(stats.get_env(taxonid = 1071), parameter="sst", interactive=False)
        
        # return a plotly object when interactive=True
        stats.dist_env(stats.get_years(taxonid = 1071), parameter="sss", interactive=True)
    """
    valid = ["sst", "sss", "depth"]
    if parameter not in valid:
        raise ValueError(f"Argument 'parameter' must be one of {valid}.")

    df = pd.DataFrame(data[parameter])
    angle = 0

    if parameter == "depth":
        df[df.columns[0]] = df[df.columns[0]].astype(str)
        angle = 90
    if not interactive:        
        ax = plt.bar(x = df[df.columns[0]], height = df[df.columns[1]])
        plt.xlabel(parameter)
        plt.ylabel(df.columns[1])
        plt.xticks(rotation = angle)
        return ax
    
    fig = px.bar(df, x = df.columns[0], y = df.columns[1], labels={df.columns[0]:parameter})
    return fig