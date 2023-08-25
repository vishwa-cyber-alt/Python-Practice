class Airplane:
    name=""
    weight=0
    fare=0
    country=""
    source="delhi"
    destination="pune"
ap=Airplane()
ap.name="vistara"
ap.weight="4004"
ap.fare="6789"
ap.country="india"
print(ap.name,ap.weight,ap.country,ap.fare,ap.source,ap.destination)
print("thanks your flight name is ",ap.name,"from ",ap.source,"to ",ap.destination)
