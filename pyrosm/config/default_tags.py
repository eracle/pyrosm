# ===============================
# OSM TAGS
# ===============================
# These configurations are used to specify which OSM tags are kept
# by default as columns in DataFrame. Follows more or less the
# OSM documentation and the tags mentioned on the Wiki:
# https://wiki.openstreetmap.org/wiki/Map_Features

# If a tag is NOT mentioned in these lists (below),
# such tag will be kept in a JSON that is stored in a "tag" column.
# The purpose of specifying default tag structure is to speed up the parsing, and
# reduce the complexity in the resulting DataFrame as OSM data can contain numerous
# attributes that are not most relevant for basic user (e.g. "customized" tags).

# ========================
# BASIC INFO TAGS
# ========================
# A list of tags that are relevant for most OSM keys
basic_info_tags = ["addr:city",
                   "addr:country",
                   "addr:full",
                   "addr:housenumber",
                   "addr:housename",
                   "addr:postcode",
                   "addr:place",
                   "addr:street",
                   "email",
                   "name",
                   "opening_hours",
                   "operator",
                   "phone",
                   "ref",
                   "url",
                   "website",
                   "yes",
                   ]

# ========================
# HIGHWAY TAGS
# ========================

# Default tags to keep as columns with highways
# Mostly based on: https://wiki.openstreetmap.org/wiki/Key:highway
highway_columns = ["access",
                   "area",
                   "bicycle",
                   "bicycle_road",
                   "bridge",
                   "busway",
                   "cycleway",
                   "est_width",
                   "foot",
                   "footway",
                   "highway",
                   "int_ref",
                   "junction",
                   "lanes",
                   "lit",
                   "maxspeed",
                   "motorcar",
                   "motorroad",
                   "motor_vehicle",
                   "name",
                   "oneway",
                   "overtaking",
                   "path",
                   "passing_places",
                   "psv",
                   "ref",
                   "service",
                   "segregated",
                   "sidewalk",
                   "smoothness",
                   "surface",
                   "tracktype",
                   "tunnel",
                   "turn",
                   "width",
                   "winter_road",

                   # Other highway tags which are not kept by default
                   # (more tags slows down the parsing)
                   # =====================================

                   # "abutters",
                   # "driving_side",
                   # "embedded_rails",
                   # "ford",
                   # "ice_road",
                   # "incline",
                   # "mtb:scale",
                   # "mtb:scale:uphill",
                   # "mtb:scale:imba",
                   # "mtb:description",
                   # "parking:condition",
                   # "parking:lane",
                   # "sac_scale",
                   # "tactile_paving",
                   # "traffic_calming",
                   # "trail_visibility",

                   ]

# ========================
# BUILDING TAGS
# ========================
# See:
# https://wiki.openstreetmap.org/wiki/Key:building
# https://wiki.openstreetmap.org/wiki/Key:addr

# Default tags to keep as columns with buildings

building_columns = basic_info_tags + \
                   ["building",
                    "amenity",
                    "building:flats",
                    "building:levels",
                    "building:material",
                    "building:max_level",
                    "building:min_level",
                    "building:fireproof",
                    "building:use",
                    "craft",
                    "height",
                    "internet_access",
                    "landuse",
                    "levels",
                    "office",
                    "operator",
                    "shop",
                    "source",
                    "start_date",
                    "wikipedia",

                    # Other tags that are not kept by default
                    # "addr:conscriptionnumber",
                    # "addr:district",
                    # "addr:province",
                    # "soft_storey",
                    # "takeaway",
                    # "addr:state",
                    # "mml:class"
                    ]

# ========================
# AMENITY TAGS
# ========================
# See:
# https://wiki.openstreetmap.org/wiki/Key:amenity

# Default tags to keep as columns with amenities
amenity_columns = basic_info_tags + \
                  ["amenity",
                   "arts_centre",
                   "atm",
                   "bank",
                   "bicycle_parking",
                   "bicycle_rental",
                   "bicycle_repair_station",
                   "bar",
                   "bbq",
                   "biergarten",
                   "brothel",
                   "building",
                   "building:levels",
                   "bureau_de_change",
                   "bus_station",
                   "bus_stop",
                   "cafe",
                   "car_rental",
                   "car_repair",
                   "car_sharing",
                   "car_wash",
                   "casino",
                   "charging_station",
                   "childcare",
                   "cinema",
                   "clinic",
                   "college",
                   "dentist",
                   "doctors",
                   "driving_school",
                   "drinking_water",
                   "fast_food",
                   "ferry_terminal",
                   "fire_station",
                   "food_court",
                   "fountain",
                   "fuel",
                   "gambling",
                   "hospital",
                   "ice_cream",
                   "internet_access",
                   "kindergarten",
                   "landuse",
                   "language_school",
                   "library",
                   "music_school",
                   "nightclub",
                   "nursing_home",
                   "office",
                   "operator",
                   "parking",
                   "pharmasy",
                   "planetarium",
                   "police",
                   "post_office",
                   "pub",
                   "public_bath",
                   "rescue_station",
                   "restaurant",
                   "retirement_home",
                   "school",
                   "social_centre",
                   "social_facility",
                   "source",
                   "spa",
                   "start_date",
                   "stripclub",
                   "taxi",
                   "theatre",
                   "university",
                   "wikipedia",

                   # Other tags
                   # ----------
                   # "baby_hatch",
                   # "levels",
                   # "ev_charging",
                   # "motorcycle_parking",
                   # "parking_entrance",
                   # "parking_space",
                   # "dive_centre",
                   # "dojo",
                   ]

# ========================
# SHOP TAGS
# ========================
# See:
# https://wiki.openstreetmap.org/wiki/Key:shop

# Default tags to keep as columns with amenities
shop_columns = basic_info_tags + \
               ["agrarian",
                "alcohol",
                "anime",
                "antiques",
                "appliance",
                "art",
                "atv",
                "baby_goods",
                "bag",
                "bakery",
                "bathroom_furnishing",
                "bed",
                "beverages",
                "bicycle",
                "boat",
                "bookmaker",
                "books",
                "boutique",
                "brewing_supplies",
                "butcher",
                "camera",
                "candles",
                "cannabis",
                "car",
                "car_parts",
                "car_repair",
                "caravan",
                "carpet",
                "charity",
                "cheese",
                "chemist",
                "chocolate",
                "clothes",
                "coffee",
                "collector",
                "computer",
                "confectionery",
                "convenience",
                "copyshop",
                "cosmetics",
                "craft",
                "curtain",
                "dairy",
                "deli",
                "department_store",
                "doityourself",
                "doors",
                "drugstore",
                "dry_cleaning",
                "e-cigarette",
                "electrical",
                "electronics",
                "energy",
                "erotic",
                "fabric",
                "farm",
                "fashion",
                "fireplace",
                "fishing",
                "flooring",
                "florist",
                "frame",
                "free_flying",
                "frozen_food",
                "fuel",
                "funeral_directors",
                "furniture",
                "games",
                "garden_centre",
                "garden_furniture",
                "gas",
                "general",
                "gift",
                "glaziery",
                "golf",
                "greengrocer",
                "hairdresser",
                "hairdresser_supply",
                "hardware",
                "health_food",
                "hearing_aids",
                "herbalist",
                "hifi",
                "houseware",
                "hunting",
                "ice_cream",
                "interior_decoration",
                "jetski",
                "jewelry",
                "kiosk",
                "kitchen",
                "lamps",
                "laundry",
                "leather",
                "lighting",
                "locksmith",
                "lottery",
                "mall",
                "massage",
                "medical_supply",
                "military_surplus",
                "mobile_phone",
                "model",
                "money_lender",
                "motorcycle",
                "music",
                "musical_instrument",
                "name",
                "newsagent",
                "nutrition_supplements",
                "optician",
                "organic",
                "outdoor",
                "outpost",
                "paint",
                "party",
                "pasta",
                "pastry",
                "pawnbroker",
                "perfumery",
                "pest_control",
                "pet",
                "pet_grooming",
                "phone",
                "photo",
                "pyrotechnics",
                "radiotechnics",
                "religion",
                "robot",
                "scuba_diving",
                "seafood",
                "second_hand",
                "security",
                "sewing",
                "shoes",
                "shop",
                "ski",
                "snowmobile",
                "spices",
                "sports",
                "stationery",
                "storage_rental",
                "supermarket",
                "swimming_pool",
                "tailor",
                "tattoo",
                "tea",
                "ticket",
                "tiles",
                "tobacco",
                "toys",
                "trade",
                "trailer",
                "travel_agency",
                "trophy",
                "tyres",
                "user defined",
                "vacant",
                "vacuum_cleaner",
                "variety_store",
                "video",
                "video_games",
                "watches",
                "water",
                "weapons",
                "wholesale",
                "window_blind",
                "windows",
                "wine",
                "wool",
                ]

# ========================
# CRAFT TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Acraft
craft_columns = basic_info_tags + \
                ["agricultural_engines",
                 "atelier",
                 "bakery",
                 "basket_maker",
                 "beekeeper",
                 "blacksmith",
                 "boatbuilder",
                 "bookbinder",
                 "brewery",
                 "builder",
                 "cabinet_maker",
                 "carpenter",
                 "carpet_layer",
                 "caterer",
                 "chimney_sweeper",
                 "clockmaker",
                 "confectionery",
                 "cooper",
                 "craft",
                 "dental_technician",
                 "distillery",
                 "door_construction",
                 "dressmaker",
                 "electronics_repair",
                 "embroiderer",
                 "electrician",
                 "engraver",
                 "floorer",
                 "gardener",
                 "glaziery",
                 "grinding_mill",
                 "handicraft",
                 "hvac",
                 "insulation",
                 "jeweller",
                 "joiner",
                 "key_cutter",
                 "locksmith",
                 "metal_construction",
                 "mint",
                 "musical_instrument",
                 "oil_mill",
                 "optician",
                 "organ_builder",
                 "painter",
                 "parquet_layer",
                 "photographer",
                 "photographic_laboratory",
                 "piano_tuner",
                 "plasterer",
                 "plumber",
                 "pottery",
                 "printer",
                 "printmaker",
                 "rigger",
                 "roofer",
                 "saddler",
                 "sailmaker",
                 "sawmill",
                 "scaffolder",
                 "sculptor",
                 "shoemaker",
                 "signmaker",
                 "stand_builder",
                 "stonemason",
                 "sun_protection",
                 "tailor",
                 "tiler",
                 "tinsmith",
                 "toolmaker",
                 "turner",
                 "upholsterer",
                 "watchmaker",
                 "water_well_drilling",
                 "window_construction",
                 "winery",
                 ]

# ========================
# LEISURE TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Acraft
leisure_columns = basic_info_tags + \
                  ["adult_gaming_centre",
                   "amusement_arcade",
                   "bandstand",
                   "beach_resort",
                   "bird_hide",
                   "bowling_alley",
                   "common",
                   "dance",
                   "disc_golf_course",
                   "dog_park",
                   "escape_game",
                   "firepit",
                   "fishing",
                   "fitness_centre",
                   "fitness_station",
                   "garden",
                   "golf_course",
                   "hackerspace",
                   "horse_riding",
                   "ice_rink",
                   "leisure",
                   "marina",
                   "miniature_golf",
                   "nature_reserve",
                   "outdoor_seating",
                   "park",
                   "picnic_table",
                   "pitch",
                   "playground",
                   "sauna",
                   "slipway",
                   "sports_centre",
                   "stadium",
                   "summer_camp",
                   "swimming_area",
                   "swimming_pool",
                   "track",
                   "trampoline_park",
                   "water_park",
                   "wildlife_hide",
                   ]

# ========================
# TOURISM TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Atourism
tourism_columns = basic_info_tags + \
                  ["alpine_hut",
                   "apartment",
                   "aquarium",
                   "artwork",
                   "attraction",
                   "camp_pitch",
                   "camp_site",
                   "caravan_site",
                   "chalet",
                   "gallery",
                   "guest_house",
                   "hostel",
                   "hotel",
                   "information",
                   "motel",
                   "museum",
                   "picnic_site",
                   "theme_park",
                   "tourism",
                   "viewpoint",
                   "wilderness_hut",
                   "zoo",
                   ]

# ========================
# HISTORIC TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Ahistoric
historic_columns = basic_info_tags + \
                   ["aircraft",
                    "aqueduct",
                    "archaeological_site",
                    "battlefield",
                    "boundary_stone",
                    "building",
                    "cannon",
                    "castle",
                    "castle_wall",
                    "church",
                    "city_gate",
                    "citywalls",
                    "farm",
                    "fort",
                    "gallows",
                    "highwater_mark",
                    "historic",
                    "locomotive",
                    "manor",
                    "memorial",
                    "milestone",
                    "monastery",
                    "monument",
                    "optical_telegraph",
                    "pillory",
                    "railway_car",
                    "ruins",
                    "rune_stone",
                    "ship",
                    "tank",
                    "tomb",
                    "tower",
                    "wayside_cross",
                    "wayside_shrine",
                    "wreck",
                    ]

# ========================
# EMERGENCY TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Aemergency
emergency_columns = basic_info_tags + \
                    ["access_point",
                     "ambulance_station",
                     "assembly_point",
                     "defibrillator",
                     "drinking_water",
                     "dry_riser_inlet",
                     "emergency",
                     "emergency_ward_entrance",
                     "fire_alarm_box",
                     "fire_extinguisher",
                     "fire_flapper",
                     "fire_hose",
                     "fire_hydrant",
                     "fire_water_pond",
                     "first_aid_kit",
                     "landing_site",
                     "life_ring",
                     "lifeguard",
                     "lifeguard_base",
                     "lifeguard_platform",
                     "lifeguard_tower",
                     "mountain_rescue",
                     "phone",
                     "rescue_box",
                     "siren",
                     "suction_point",
                     "water_tank",
                     ]

# ========================
# OFFICE TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Aoffice

office_columns = basic_info_tags + \
                 ["accountant",
                  "adoption_agency",
                  "advertising_agency",
                  "architect",
                  "association",
                  "bail_bond_agent",
                  "charity",
                  "company",
                  "consulting",
                  "coworking",
                  "diplomatic",
                  "educational_institution",
                  "employment_agency",
                  "energy_supplier",
                  "engineer",
                  "estate_agent",
                  "financial",
                  "forestry",
                  "foundation",
                  "geodesist",
                  "government",
                  "graphic_design",
                  "guide",
                  "harbour_master",
                  "insurance",
                  "it",
                  "lawyer",
                  "logistics",
                  "moving_company",
                  "newspaper",
                  "ngo",
                  "notary",
                  "office",
                  "political_party",
                  "private_investigator",
                  "property_management",
                  "quango",
                  "religion",
                  "research",
                  "security",
                  "surveyor",
                  "tax",
                  "tax_advisor",
                  "telecommunication",
                  "union",
                  "visa",
                  "water_utility",
                  ]

# ========================
# LANDUSE TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key:landuse
landuse_columns = ["allotments",
                   "basin",
                   "brownfield",
                   "cemetery",
                   "commercial",
                   "conservation",
                   "construction",
                   "depot",
                   "farmland",
                   "farmyard",
                   "forest",
                   "garages",
                   "grass",
                   "greenfield",
                   "greenhouse_horticulture",
                   "industrial",
                   "landfill",
                   "landuse",
                   "meadow",
                   "military",
                   "orchard",
                   "peat_cutting",
                   "plant_nursery",
                   "port",
                   "quarry",
                   "railway",
                   "recreation_ground",
                   "religious",
                   "reservoir",
                   "residential",
                   "retail",
                   "salt_pond",
                   "village_green",
                   "vineyard",
                   "yes"]

# ========================
# NATURAL TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Anatural
natural_columns = ["arete",
                   "bare_rock",
                   "bay",
                   "beach",
                   "cape",
                   "cave_entrance",
                   "cliff",
                   "coastline",
                   "dune",
                   "fell",
                   "geyser",
                   "glacier",
                   "grassland",
                   "heath",
                   "hill",
                   "hot_spring",
                   "isthmus",
                   "moor",
                   "mud",
                   "natural",
                   "peak",
                   "peninsula",
                   "reef",
                   "ridge",
                   "rock",
                   "saddle",
                   "sand",
                   "scree",
                   "scrub",
                   "shingle",
                   "sinkhole",
                   "spring",
                   "stone",
                   "strait",
                   "tree",
                   "tree_row",
                   "valley",
                   "volcano",
                   "water",
                   "wetland",
                   "wood"
                   ]

# ========================
# WATERWAY TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Awaterway
waterway_columns = ["boatyard",
                    "canal",
                    "dam",
                    "ditch",
                    "dock",
                    "drain",
                    "drystream",
                    "fairway",
                    "fuel",
                    "lock_gate",
                    "pressurised",
                    "river",
                    "riverbank",
                    "stream",
                    "tidal_channel",
                    "turning_point",
                    "wadi",
                    "water_point",
                    "waterfall",
                    "weir",
                    ]

# ========================
# GEOLOGICAL TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Ageological
geological_columns = ["moraine",
                      "outcrop",
                      "palaeontological_site",
                      ]

# ========================
# POWER TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Apower
power_columns = ["cable",
                 "catenary_mast",
                 "compensator",
                 "converter",
                 "generator",
                 "heliostat",
                 "insulator",
                 "line",
                 "busbar",
                 "bay",
                 "minor_line",
                 "plant",
                 "pole",
                 "portal",
                 "substation",
                 "switch",
                 "switchgear",
                 "terminal",
                 "tower",
                 "transformer",
                 ]

# ========================
# PUBLIC_TRANSPORT TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Apublic_transport
public_transport_columns = ["stop_position",
                            "platform",
                            "station",
                            "stop_area",
                            ]

# ========================
# RAILWAY TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key:railway
railway_columns = ["abandoned",
                   "buffer_stop",
                   "construction",
                   "crossing",
                   "derail",
                   "disused",
                   "funicular",
                   "halt",
                   "level_crossing",
                   "light_rail",
                   "miniature",
                   "monorail",
                   "narrow_gauge",
                   "platform",
                   "preserved",
                   "rail",
                   "railway",
                   "railway_crossing",
                   "roundhouse",
                   "signal",
                   "station",
                   "subway",
                   "subway_entrance",
                   "switch",
                   "tram",
                   "tram_stop",
                   "traverser",
                   "turntable",
                   "wash",
                   ]

# ========================
# ROUTE TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key:route
route_columns = ["bicycle",
                 "bus",
                 "canoe",
                 "detour",
                 "duration",
                 "evacuation",
                 "ferry",
                 "foot",
                 "from",
                 "hiking",
                 "horse",
                 "inline_skates",
                 "light_rail",
                 "mtb",
                 "network",
                 "piste",
                 "railway",
                 "road",
                 "running",
                 "ski",
                 "subway",
                 "to",
                 "train",
                 "tracks",
                 "tram",
                 "trolleybus",
                 "type",
                 ]

# ========================
# PLACE TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Aplace
place_columns = ["allotments",
                 "archipelago",
                 "borough",
                 "city",
                 "city_block",
                 "continent",
                 "country",
                 "county",
                 "district",
                 "farm",
                 "hamlet",
                 "island",
                 "islet",
                 "isolated_dwelling",
                 "locality",
                 "municipality",
                 "neighbourhood",
                 "ocean",
                 "plot",
                 "province",
                 "quarter",
                 "region",
                 "sea",
                 "square",
                 "state",
                 "suburb",
                 "town",
                 "village"]

# ========================
# AERIALWAY TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Aaerialway
aerialway_columns = ["cable_car",
                     "gondola",
                     "mixed_lift",
                     "chair_lift",
                     "drag_lift",
                     "t-bar",
                     "j-bar",
                     "platter",
                     "rope_tow",
                     "magic_carpet",
                     "zip_line",
                     "goods",
                     "pylon",
                     "station", ]

# ========================
# AEROWAY TAGS
# ========================
# See: https://wiki.openstreetmap.org/wiki/Key%3Aaeroway
aeroway_columns = ["aerodrome",
                   "apron",
                   "control_tower",
                   "control_center",
                   "gate",
                   "hangar",
                   "helipad",
                   "heliport",
                   "navigationaid",
                   "beacon",
                   "runway",
                   "taxilane",
                   "taxiway",
                   "terminal",
                   "windsock",
                   "highway_strip",
                   ]
