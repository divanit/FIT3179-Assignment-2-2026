import pandas as dict_pandas  # or import pandas

# 1. Load your raw CSV
df = dict_pandas.read_csv("data/varietal_concentration_index_by_region.csv")

# 2. Define latitude and longitude mapping for Australian wine regions
# (Example coordinates for key regions - complete or adjust as needed)
coordinates = {
    "Adelaide Hills": (-34.915, 138.805),
    "Adelaide Plains": (-34.750, 138.600),
    "Alpine Valleys": (-36.650, 146.850),
    "Barossa Valley": (-34.538, 138.948),
    "Beechworth": (-36.358, 146.688),
    "Bendigo": (-36.757, 144.279),
    "Big Rivers - other": (-34.500, 144.000),
    "Blackwood Valley": (-33.850, 116.150),
    "Canberra District": (-35.280, 149.130),
    "Central Ranges - other": (-32.600, 149.000),
    "Central Victoria - other": (-36.800, 144.500),
    "Clare Valley": (-33.833, 138.617),
    "Coonawarra": (-37.283, 140.833),
    "Cowra": (-33.839, 148.680),
    "Eden Valley": (-34.550, 139.083),
    "Fleurieu - other": (-35.550, 138.650),
    "Geelong": (-38.149, 144.361),
    "Geographe": (-33.370, 115.640),
    "Gippsland": (-38.100, 147.100),
    "Glenrowan": (-36.467, 146.367),
    "Goulburn Valley": (-36.380, 145.400),
    "Grampians": (-37.250, 142.500),
    "Granite Belt": (-28.650, 151.950),
    "Great Southern": (-34.950, 117.600),
    "Greater Perth - other": (-31.950, 115.850),
    "Gundagai": (-35.060, 148.110),
    "Hastings River": (-31.430, 152.900),
    "Heathcote": (-36.908, 144.708),
    "Henty": (-37.700, 141.500),
    "Hilltops": (-34.550, 148.400),
    "Hunter Valley": (-32.770, 151.350),
    "Langhorne Creek": (-35.283, 139.033),
    "Limestone Coast - other": (-37.000, 140.500),
    "Macedon Ranges": (-37.350, 144.550),
    "Manjimup": (-34.244, 116.145),
    "Margaret River": (-33.955, 115.075),
    "McLaren Vale": (-35.222, 138.542),
    "Mornington Peninsula": (-38.350, 145.033),
    "Mudgee": (-32.598, 149.588),
    "Murray Darling - Swan Hill (NSW)": (-35.000, 143.500),
    "Murray Darling - Swan Hill (Vic)": (-35.330, 143.550),
    "North East Victoria - other": (-36.400, 146.500),
    "Northern Rivers - other": (-28.800, 153.000),
    "Northern Slopes": (-31.000, 150.000),
    "Orange": (-33.283, 149.100),
    "Padthaway": (-36.567, 140.600),
    "Peel": (-32.533, 115.900),
    "Pemberton": (-34.444, 116.033),
    "Perricoota": (-36.117, 144.750),
    "Perth Hills": (-31.950, 116.100),
    "Port Phillip - other": (-37.800, 145.000),
    "Pyrenees": (-37.250, 143.367),
    "Qld - other": (-25.000, 151.500),
    "Riverina": (-34.283, 146.050),
    "Riverland": (-34.250, 140.583),
    "Rutherglen": (-36.050, 146.467),
    "SA - other": (-32.000, 135.000),
    "South Burnett": (-26.540, 151.850),
    "South Coast - other": (-35.000, 117.500),
    "Southern Highlands": (-34.483, 150.417),
    "Southern New South Wales - other": (-35.000, 147.000),
    "Strathbogie Ranges": (-36.850, 145.500),
    "Sunbury": (-37.583, 144.733),
    "Swan District": (-31.833, 116.000),
    "Tas": (-42.000, 147.000),
    "Tumbarumba": (-35.767, 148.017),
    "Upper Goulburn": (-37.200, 145.800),
    "WA - other": (-30.000, 121.000),
    "Western Plains": (-32.000, 147.000),
    "Western Victoria - other": (-37.500, 143.000),
    "Wrattonbully": (-37.150, 140.883),
    "Yarra Valley": (-37.650, 145.417)
}

# 3. Map latitude and longitude into the DataFrame
df["latitude"] = df["region"].map(lambda r: coordinates.get(r, (None, None))[0])
df["longitude"] = df["region"].map(lambda r: coordinates.get(r, (None, None))[1])

# 4. Handle missing values (fill NaN with 0 or drop if needed for specific years)
df.fillna(0, inplace=True)

# 5. Save the processed dataset
df.to_csv("data/varietal_concentration_processed.csv", index=False)
print("Dataset successfully processed and saved!")