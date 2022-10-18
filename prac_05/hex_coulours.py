COLOUR_TO_HEX = {"red1": "#ff0000", "blue1": "#0000ff", "yellow1": "#ffff00", "orangered1": "#ff4500",
                 "orange1": "#ffa500", "yelloworange": "#ffae42", "green": "#00a550",
                 "bluegreen": "#0d98ba", "purple": "#a020f0", "greenyellow": "#adff2f"}

print(COLOUR_TO_HEX)

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_HEX:
        print(f"Hex value is {COLOUR_TO_HEX[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
