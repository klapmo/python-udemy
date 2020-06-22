print("How many kilometers were traveled?")
kms = float(input())
miles = kms/1.60934

cleanmiles = round(miles, 2)
print(f"Ok, you said {cleanmiles} miles")