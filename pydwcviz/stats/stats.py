import pandas as pd
from ..utils import get, obis_base_url

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
