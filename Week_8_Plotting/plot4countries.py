# countries.py

import numpy as np
import matplotlib.pyplot as plot

possibleCountries = ["Ireland", "England", "South Korea", "Netherlands", "Australia"]
countries = np.random.choice(
    possibleCountries,
    p = [0.1, 0.3, 0.2, 0.12, 0.28],
    size = (100)
)

unique, counts = np.unique(countries, return_counts = True)

plot.bar(unique, counts)
plot.show()