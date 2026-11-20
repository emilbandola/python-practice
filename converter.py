print("=== PHP to JPY Currency Converter ===")

pesos = float(input("Enter amount in Philippine Pesos (PHP): "))
exchange_rate = 2.65
yen = pesos * exchange_rate

print(f"{pesos} PHP is equal to {yen:.2f} Japanese Yen (JPY).")