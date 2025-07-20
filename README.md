# Black-Scholes Option Pricing Calculator

A collection of Black-Scholes option pricing calculators, from a simple command-line version to a more modern GUI application. Built with Python and CustomTkinter.

## Versions

### 1. **GUI Version** (`bs_web.py`)
- Modern desktop application with intuitive GUI
- Built with CustomTkinter for a professional look
- Real-time calculations with instant feedback

### 2. **Command-Line Version** (`BSF.py`)
- The first Black-Scholes calculator I made
- Simple, bare-bones interactive command-line interface
- No external dependencies beyond scipy

## Features

- **Intuitive GUI**: Clean interface with dark theme
- **Real-time Calculations**: Instant option price calculations
- **Support for Both Options**: Calculate prices for both call and put options
- **Error Handling**: Input validation and error messages in both versions


## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/black-scholes-calculator.git
   cd black-scholes-calculator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   **GUI Version:**
   ```bash
   python bs_web.py
   ```

   **Command-Line Version:**
   ```bash
   python BSF.py
   ```

## Usage

### GUI Version (`bs_web.py`)
1. Launch the application
2. Enter the required parameters:
   - **Underlying Price (S)**: Current price of the underlying asset
   - **Strike Price (K)**: Option strike price
   - **Risk-Free Rate (%)**: Annual risk-free interest rate
   - **Volatility (%)**: Annual volatility of the underlying asset
   - **Days to Expiry**: Number of days until option expiration
3. Select the option type (Call or Put)
4. Click "Calculate" to get the option price

### Command-Line Version (`BSF.py`)
1. Run the script
2. Follow the interactive prompts to enter:
   - Underlying security's price
   - Option's strike price
   - Option type (Call or Put)
   - Risk-free rate (as a percentage)
   - Annualized volatility (as a percentage)
   - Days until expiration
3. The calculated option price will be displayed

## Input Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| S (Underlying Price) | Current price of the stock/asset | 100.00 |
| K (Strike Price) | Option strike price | 105.00 |
| r (Risk-Free Rate) | Annual risk-free interest rate (%) | 2.5 |
| V (Volatility) | Annual volatility of the asset (%) | 25.0 |
| t (Days to Expiry) | Days until option expiration | 30 |

## Mathematical Background

The application implements the Black-Scholes option pricing model:

**For Call Options:**
```
C = S * N(d1) - K * e^(-r*t) * N(d2)
```

**For Put Options:**
```
P = K * e^(-r*t) * N(-d2) - S * N(-d1)
```

Where:
- d1 = (ln(S/K) + (r + σ²/2)*t) / (σ*√t)
- d2 = d1 - σ*√t
- N(x) = Cumulative standard normal distribution

## Dependencies

- `customtkinter`: Modern GUI framework
- `scipy`: Scientific computing library (for normal distribution)
- `math`: Python standard library

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- Mathematical implementation based on the Black-Scholes model
- Inspired by the need for a user-friendly option pricing tool

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - email@example.com

Project Link: [https://github.com/yourusername/black-scholes-calculator](https://github.com/yourusername/black-scholes-calculator) 