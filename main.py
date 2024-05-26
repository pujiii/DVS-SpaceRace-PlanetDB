import random
import sqlite3

# Connect to the database
conn = sqlite3.connect('exoplanets.db')
cursor = conn.cursor()

# Define table schema
table_schema = """
CREATE TABLE IF NOT EXISTS exoplanets (
    name TEXT PRIMARY KEY,
    host_star_name TEXT,
    distance_from_earth REAL,  -- in light years
    discovery_year INTEGER,
    orbital_period REAL,  -- in days
    planet_radius REAL,  -- in earth radii
    mass REAL  -- in earth masses
);
"""

cursor.execute(table_schema)

# Mythology databases
mythology_sources = {
    "greek": ["Gaia", "Zeus", "Poseidon", "Hera", "Ares", "Athena", "Apollo", "Artemis", "Hephaestus", "Aphrodite"],
    "roman": ["Jupiter", "Juno", "Neptune", "Venus", "Mars", "Minerva", "Apollo", "Diana", "Vulcan", "Venus"],
    "egyptian": ["Ra", "Osiris", "Isis", "Seth", "Nephthys", "Geb", "Nut", "Thoth", "Bastet", "Anubis"],
    "norse": ["Odin", "Thor", "Frigg", "Baldr", "Loki", "Freyja", "Heimdall", "Hel", "Bragi", "Tyr"]
}

def generate_exoplanet():
  # Choose a random mythology
  mythology = random.choice(list(mythology_sources.keys()))
  
  # Choose a random name from the chosen mythology
  name = random.choice(mythology_sources[mythology])
  
  # Add a unique number suffix (up to 4 digits)
  number_suffix = str(random.randint(1000, 9999))
  name += number_suffix

  # Generate host star name options
  star_name_options = [
      # Constellation + Bayer designation (e.g., Alpha Centauri B)
      f"{random.choice(constellations)} {chr(random.randint(65, 90))}",
      # Constellation abbreviation + number (e.g., Gliese 581)
      f"{random.choice(constellation_abbreviations)}{random.randint(100, 999)}",
      # Fictional star name with a celestial theme (e.g., Helios, Solaria)
      random.choice(fictional_star_names)
  ]
  host_star_name = random.choice(star_name_options)

  distance = random.uniform(100, 5000)  # distance in light years
  discovery_year = random.randint(2000, 2024)
  orbital_period = random.uniform(1, 100)  # orbital period in days
  planet_radius = random.uniform(0.5, 2.0)  # planet radius in earth radii
  mass = random.uniform(0.1, 10.0)  # mass in earth masses
  return (name, host_star_name, distance, discovery_year, orbital_period, planet_radius, mass)

# Constellation lists (replace with your preferred sources if needed)
constellations = [
    "Andromeda", "Aquarius", "Aries", "Auriga", "Boötes", "Cancer",
    "Canis Major", "Canis Minor", "Capricornus", "Cassiopeia", "Centaurus", "Cepheus"
    # ... and so on for all 88 constellations
]

constellation_abbreviations = [
    "And", "Aqu", "Ari", "Aur", "Boo", "Cnc", "CMa", "CMi", "Cap", "Cas", "Cen", "Cep"
    # ... and so on for all constellation abbreviations
]

# Fictional star names
fictional_star_names = [
    "Helios", "Solaria", "Proxima", "Antares", "Corvus", "Vega", "Arcturus"
]

# Generate and insert 15000 exoplanets (might take some time)
for _ in range(15000):
  while True:
    data = generate_exoplanet()
    try:
        cursor.execute("INSERT INTO exoplanets VALUES (?, ?, ?, ?, ?, ?, ?)", data)
        break
    except:
       continue

rows = cursor.execute("SELECT * FROM exoplanets").fetchall()
print(rows)


# Save changes and close connection
conn.commit()
conn.close()

print("15000 Exoplanet data generated and inserted into exoplanets.db!")
