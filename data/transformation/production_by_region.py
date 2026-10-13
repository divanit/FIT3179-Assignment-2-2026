import pandas as pd

# 1. Load your raw CSV
df = pd.read_csv("data/production_by_region(tonnes).csv")

# 2. Complete dictionary mapping each region to (latitude, longitude, state)
region_metadata = {
    "Adelaide Hills": (-34.915, 138.805, "South Australia"),
    "Adelaide Plains": (-34.750, 138.600, "South Australia"),
    "Alpine Valleys": (-36.650, 146.850, "Victoria"),
    "Barossa Valley": (-34.538, 138.948, "South Australia"),
    "Beechworth": (-36.358, 146.688, "Victoria"),
    "Bendigo": (-36.757, 144.279, "Victoria"),
    "Big Rivers - other": (-34.500, 144.000, "New South Wales"),
    "Blackwood Valley": (-33.850, 116.150, "Western Australia"),
    "Canberra District": (-35.280, 149.130, "Australian Capital Territory"),
    "Central Ranges - other": (-32.600, 149.000, "New South Wales"),
    "Central Victoria - other": (-36.800, 144.500, "Victoria"),
    "Clare Valley": (-33.833, 138.617, "South Australia"),
    "Coonawarra": (-37.283, 140.833, "South Australia"),
    "Cowra": (-33.839, 148.680, "New South Wales"),
    "Eden Valley": (-34.550, 139.083, "South Australia"),
    "Fleurieu - other": (-35.550, 138.650, "South Australia"),
    "Geelong": (-38.149, 144.361, "Victoria"),
    "Geographe": (-33.370, 115.640, "Western Australia"),
    "Gippsland": (-38.100, 147.100, "Victoria"),
    "Glenrowan": (-36.467, 146.367, "Victoria"),
    "Goulburn Valley": (-36.380, 145.400, "Victoria"),
    "Grampians": (-37.250, 142.500, "Victoria"),
    "Granite Belt": (-28.650, 151.950, "Queensland"),
    "Great Southern": (-34.950, 117.600, "Western Australia"),
    "Greater Perth - other": (-31.950, 115.850, "Western Australia"),
    "Gundagai": (-35.060, 148.110, "New South Wales"),
    "Hastings River": (-31.430, 152.900, "New South Wales"),
    "Heathcote": (-36.908, 144.708, "Victoria"),
    "Henty": (-37.700, 141.500, "Victoria"),
    "Hilltops": (-34.550, 148.400, "New South Wales"),
    "Hunter Valley": (-32.770, 151.350, "New South Wales"),
    "Langhorne Creek": (-35.283, 139.033, "South Australia"),
    "Limestone Coast - other": (-37.000, 140.500, "South Australia"),
    "Macedon Ranges": (-37.350, 144.550, "Victoria"),
    "Manjimup": (-34.244, 116.145, "Western Australia"),
    "Margaret River": (-33.955, 115.075, "Western Australia"),
    "McLaren Vale": (-35.222, 138.542, "South Australia"),
    "Mornington Peninsula": (-38.350, 145.033, "Victoria"),
    "Mudgee": (-32.598, 149.588, "New South Wales"),
    "Murray Darling - Swan Hill (NSW)": (-35.000, 143.500, "New South Wales"),
    "Murray Darling - Swan Hill (Vic)": (-35.330, 143.550, "Victoria"),
    "North East Victoria - other": (-36.400, 146.500, "Victoria"),
    "Northern Rivers - other": (-28.800, 153.000, "New South Wales"),
    "Northern Slopes": (-31.000, 150.000, "New South Wales"),
    "Orange": (-33.283, 149.100, "New South Wales"),
    "Padthaway": (-36.567, 140.600, "South Australia"),
    "Peel": (-32.533, 115.900, "Western Australia"),
    "Pemberton": (-34.444, 116.033, "Western Australia"),
    "Perricoota": (-36.117, 144.750, "New South Wales"),
    "Perth Hills": (-31.950, 116.100, "Western Australia"),
    "Port Phillip - other": (-37.800, 145.000, "Victoria"),
    "Pyrenees": (-37.250, 143.367, "Victoria"),
    "Qld - other": (-25.000, 151.500, "Queensland"),
    "Riverina": (-34.283, 146.050, "New South Wales"),
    "Riverland": (-34.250, 140.583, "South Australia"),
    "Rutherglen": (-36.050, 146.467, "Victoria"),
    "SA - other": (-32.000, 135.000, "South Australia"),
    "South Burnett": (-26.540, 151.850, "Queensland"),
    "South Coast - other": (-35.000, 117.500, "Western Australia"),
    "Southern Highlands": (-34.483, 150.417, "New South Wales"),
    "Southern New South Wales - other": (-35.000, 147.000, "New South Wales"),
    "Strathbogie Ranges": (-36.850, 145.500, "Victoria"),
    "Sunbury": (-37.583, 144.733, "Victoria"),
    "Swan District": (-31.833, 116.000, "Western Australia"),
    "Tas": (-42.000, 147.000, "Tasmania"),
    "Tumbarumba": (-35.767, 148.017, "New South Wales"),
    "Upper Goulburn": (-37.200, 145.800, "Victoria"),
    "WA - other": (-30.000, 121.000, "Western Australia"),
    "Western Plains": (-32.000, 147.000, "New South Wales"),
    "Western Victoria - other": (-37.500, 143.000, "Victoria"),
    "Wrattonbully": (-37.150, 140.883, "South Australia"),
    "Yarra Valley": (-37.650, 145.417, "Victoria")
}

# 3. Map metadata columns into dataframe
df["latitude"] = df["region"].map(lambda r: region_metadata.get(r, (None, None, None))[0])
df["longitude"] = df["region"].map(lambda r: region_metadata.get(r, (None, None, None))[1])
df["state"] = df["region"].map(lambda r: region_metadata.get(r, (None, None, None))[2])

# 4. Fill missing production values with 0
df.fillna(0, inplace=True)

# 5. Save processed CSV
df.to_csv("data/production_by_region_processed.csv", index=False)
print("Production dataset successfully processed with coordinates and states!")