import pandas as pd
import numpy as np
import plotly.express as px

# Generate synthetic inspection dataset
np.random.seed(42)

n = 500

data = pd.DataFrame({
    "latitude": np.random.uniform(-23.7, -23.4, n),
    "longitude": np.random.uniform(-46.8, -46.3, n),
    "inspection_count": np.random.randint(1, 10, n),
    "fraud_risk": np.random.rand(n)
})

# Create geospatial visualization
fig = px.scatter_mapbox(
    data,
    lat="latitude",
    lon="longitude",
    color="fraud_risk",
    size="inspection_count",
    mapbox_style="carto-positron",
    zoom=10,
    title="Geospatial Fraud Risk Visualization"
)

fig.show()
