
### control_torals_taz_simple.csv
- TAZ: TAZ ID
- POPBASE: number of person in the area
- HHBASE: numnber of Household in the area 
- HHSIZE*: household size category
- HHAGE*: household average age category
- HHINC*: household income category

### geo_cross_walk_simple.csv
- BLKGRP: Block group
- STATEFP: State FIPS Code
- COUNTYFP: County FIPS Code code
- TRACTCE: Census Tract Code
- GEOID: Concatenations of state FIPS and PUMA codes
- NAME: Name code of the geography
- NAMELSAD: Name of the geography
- PUMA: PUMA code
- REGION: Region ID

## seed_household.csv
- RT: Data type
- SERIALNO: Data serial number
- DIVISION: Devision ID
- PUMA: PUMA ID, e.g., 600
- REGION: Region ID
- WGTP: Housing Weight 
- NP: Number of person records following this housing record
- TAXP: Annual value of property taxes paid
- FWATP: Water (yearly cost) allocation

## seed_persons.csv
- RT: Data type
- SERIALNO: Data serial number
- SPORDER: Person serial number
- PUMA: PUMA ID, e.g., 600
- MAR: Marital status
- NWAB: Temporary absence from work
