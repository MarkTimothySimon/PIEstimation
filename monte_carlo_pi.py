import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.title("Monte Carlo Pi Estimation")
st.write("""
This app demonstrates how to estimate π using the Monte Carlo method.
The method works by randomly throwing darts at a square with an inscribed quarter circle.
The ratio of darts landing inside the quarter circle to total darts thrown approaches π/4.
""")

# Slider for number of points
n_points = st.slider("Number of points", min_value=100, max_value=100000, value=1000, step=100)

# Generate random points
np.random.seed(42)  # For reproducibility
x = np.random.uniform(0, 1, n_points)
y = np.random.uniform(0, 1, n_points)

# Check which points are inside the quarter circle
distances = np.sqrt(x**2 + y**2)
inside = distances <= 1

# Calculate pi estimation
pi_estimation = 4 * np.sum(inside) / n_points

# Create running estimation
running_inside = np.cumsum(inside)
running_total = np.arange(1, n_points + 1)
running_pi = 4 * running_inside / running_total

# Create subplots
fig = make_subplots(rows=1, cols=2, 
                    subplot_titles=("Dart Throws", "Pi Estimation Convergence"),
                    specs=[[{"type": "scatter"}, {"type": "scatter"}]])

# Scatter plot of points
fig.add_trace(
    go.Scatter(
        x=x[~inside], y=y[~inside],
        mode='markers',
        name='Outside',
        marker=dict(color='red', size=5, opacity=0.6)
    ),
    row=1, col=1
)

fig.add_trace(
    go.Scatter(
        x=x[inside], y=y[inside],
        mode='markers',
        name='Inside',
        marker=dict(color='blue', size=5, opacity=0.6)
    ),
    row=1, col=1
)

# Add quarter circle
theta = np.linspace(0, np.pi/2, 100)
fig.add_trace(
    go.Scatter(
        x=np.cos(theta),
        y=np.sin(theta),
        mode='lines',
        name='Quarter Circle',
        line=dict(color='black', width=2)
    ),
    row=1, col=1
)

# Convergence plot
fig.add_trace(
    go.Scatter(
        x=running_total,
        y=running_pi,
        mode='lines',
        name='Pi Estimation',
        line=dict(color='green', width=2)
    ),
    row=1, col=2
)

fig.add_trace(
    go.Scatter(
        x=[0, n_points],
        y=[np.pi, np.pi],
        mode='lines',
        name='Actual Pi',
        line=dict(color='white', dash='dash', width=2)
    ),
    row=1, col=2
)

# Update layout
fig.update_layout(
    height=500,
    width=1000,
    showlegend=True,
    title_text=f"Current π estimation: {pi_estimation:.6f}"
)

fig.update_xaxes(title_text="X", row=1, col=1)
fig.update_yaxes(title_text="Y", row=1, col=1)
fig.update_xaxes(title_text="Number of Points", row=1, col=2)
fig.update_yaxes(title_text="Pi Estimation", row=1, col=2)

# Display the plot
st.plotly_chart(fig, use_container_width=True)

# Additional information
st.write(f"""
### Results:
- Number of points: {n_points}
- Points inside quarter circle: {np.sum(inside)}
- Final π estimation: {pi_estimation:.6f}
- Actual π: {np.pi:.6f}
- Absolute error: {abs(pi_estimation - np.pi):.6f}
""")
