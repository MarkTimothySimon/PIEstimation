# Monte Carlo Pi Estimation

This Streamlit application demonstrates the Monte Carlo method for estimating the value of π (pi). The app provides an interactive visualization of how the estimation becomes more accurate as the number of random points increases.

## How it Works

The Monte Carlo method for estimating π works by:
1. Creating a square with side length 1 and an inscribed quarter circle with radius 1
2. Randomly generating points within the square
3. Calculating the ratio of points that fall inside the quarter circle to the total number of points
4. Multiplying this ratio by 4 to get an estimation of π

## Features

- Interactive slider to adjust the number of random points (100-10,000)
- Real-time visualization of point distribution
- Live convergence plot showing how the estimation approaches π
- Detailed statistics including absolute error from true π value

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/monte-carlo-pi.git
cd monte-carlo-pi
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

Run the Streamlit app:
```bash
streamlit run monte_carlo_pi.py
```

The app will open in your default web browser. Use the slider to adjust the number of points and observe how the estimation of π changes.

## Files in this Repository

- `monte_carlo_pi.py`: Main application file containing the Streamlit app code
- `requirements.txt`: List of Python dependencies
- `README.md`: This documentation file

## Requirements

- Python 3.7+
- See requirements.txt for Python package dependencies

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.
