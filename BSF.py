import math
from scipy.stats import norm

def inputs():
    while True:
        S = input("Enter the underlying security's price: ").strip()
        try:
            float(S)
            break
        except ValueError:
            print("Enter an appropriate value.\n")

    while True:
        K = input("Enter the option's strike price: ").strip()
        try:
            float(K)
            break
        except ValueError:
            print("Enter an appropriate value.\n")

    CorP = input("Enter whether the option is a Call or Put: ").strip().lower()
    while not CorP or CorP[0] not in ('p', 'c'):
        CorP = input("Enter whether the option is a Call or Put: ").strip().lower()
    CorP = CorP[0]

    while True:
        r = input("Enter the risk-free-rate as a percent: ").strip()
        try:
            float(r)
            break
        except ValueError:
            print("Enter an appropriate value.\n")

    while True:
        V = input("Enter the annualized (trading-day year) volatility as a percent: ").strip()
        try:
            float(V)
            break
        except ValueError:
            print("Enter an appropriate value.\n")

    while True:
        t = input("Enter the number of days until the option's expiration: ").strip()
        try:
            float(t)
            break
        except ValueError:
            print("Enter an appropriate value.\n")

    t = float(t) / 365
    r = float(r) / 100
    V = float(V) / 100
    V = V * math.sqrt(252/365)
    return round(float(S), 2), int(K), round(float(r), 4), round(float(V), 4), t, CorP

def calculation(S, K, r, V, t, CorP):
    d1 = (math.log(S/K) + (r + (0.5 * V**2)) * t) / (V * math.sqrt(t))

    d2 = d1 - (V * math.sqrt(t))

    if CorP[0] == 'c':
        price = S * norm.cdf(d1) - K * math.exp(-r * t) * norm.cdf(d2)
    else:
        price = K * math.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price

def main():
    print("Black-Scholes Option Pricing Calculator\n")

    S, K, r, V, t, CorP = inputs()
    price = calculation(S, K, r, V, t, CorP)

    if CorP == 'c':
        print("\nThe Black-Scholes price of the given call option is:", round(price, 2))
    else:
        print("\nThe Black-Scholes price of the given put option is:", round(price, 2))

    print("\nGoodbye")

if __name__ == "__main__":
    main()