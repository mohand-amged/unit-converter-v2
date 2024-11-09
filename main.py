
def length_conv(): 
    msg = int(input("Enter the length to convert: "))
    msg_from = input("unit to convert from: ")
    msg_to = input("unit to convert to: ")

    conversions = {
    # Feet conversions
    ("ft", "yard"): (msg / 3),
    ("ft", "mile"): (msg / 5280),
    ("ft", "inch"): (msg * 12),
    ("ft", "m"): (msg * 0.3048),
    ("ft", "cm"): (msg * 30.48),
    ("ft", "mm"): (msg * 304.8),
    ("ft", "km"): (msg * 0.0003048),

    # Inches conversions
    ("inch", "ft"): (msg / 12),
    ("inch", "yard"): (msg / 36),
    ("inch", "mile"): (msg / 63360),
    ("inch", "m"): (msg * 0.0254),
    ("inch", "cm"): (msg * 2.54),
    ("inch", "mm"): (msg * 25.4),
    ("inch", "km"): (msg * 0.0000254),

    # Yards conversions
    ("yard", "mile"): (msg / 1760),
    ("yard", "ft"): (msg * 3),
    ("yard", "inch"): (msg * 36),
    ("yard", "m"): (msg * 0.9144),
    ("yard", "cm"): (msg * 91.44),
    ("yard", "mm"): (msg * 914.4),
    ("yard", "km"): (msg * 0.0009144),

    # Miles conversions
    ("mile", "yard"): (msg * 1760),
    ("mile", "ft"): (msg * 5280),
    ("mile", "inch"): (msg * 63360),
    ("mile", "m"): (msg * 1609.34),
    ("mile", "cm"): (msg * 160934),
    ("mile", "mm"): (msg * 1.609e+6),
    ("mile", "km"): (msg * 1.60934),

    # Meters conversions
    ("m", "ft"): (msg / 0.3048),
    ("m", "inch"): (msg / 0.0254),
    ("m", "yard"): (msg / 0.9144),
    ("m", "mile"): (msg / 1609.34),
    ("m", "cm"): (msg * 100),
    ("m", "mm"): (msg * 1000),
    ("m", "km"): (msg / 1000),

    # Centimeters conversions
    ("cm", "ft"): (msg / 30.48),
    ("cm", "inch"): (msg / 2.54),
    ("cm", "yard"): (msg / 91.44),
    ("cm", "mile"): (msg / 160934),
    ("cm", "m"): (msg / 100),
    ("cm", "mm"): (msg * 10),
    ("cm", "km"): (msg / 100000),

    # Millimeters conversions
    ("mm", "ft"): (msg / 304.8),
    ("mm", "inch"): (msg / 25.4),
    ("mm", "yard"): (msg / 914.4),
    ("mm", "mile"): (msg / 1.609e+6),
    ("mm", "m"): (msg / 1000),
    ("mm", "cm"): (msg / 10),
    ("mm", "km"): (msg / 1e+6),

    # Kilometers conversions
    ("km", "ft"): (msg / 0.0003048),
    ("km", "inch"): (msg / 0.0000254),
    ("km", "yard"): (msg / 0.0009144),
    ("km", "mile"): (msg / 1.60934),
    ("km", "m"): (msg * 1000),
    ("km", "cm"): (msg * 100000),
    ("km", "mm"): (msg * 1e+6),
}

    if (msg_from, msg_to) in conversions:
        print(conversions[(msg_from, msg_to)])
    else:
        print("Conversion not supported")
    
def weight_conv():
    msg = int(input("Enter the weight to convert: "))
    msg_from = input("unit to convert from: ")
    msg_to = input("unit to convert to: ")

    conversions = {
        ("g", "kg"): 0.001,
        ("g", "oz"): 0.0352739,
        ("g", "lb"): 0.00220462,
        ("g", "mg"): 1000,  # 1 gram = 1000 milligrams
        ("kg", "g"): 1000,
        ("kg", "oz"): 35.274,
        ("kg", "lb"): 2.20462,
        ("kg", "mg"): 1_000_000,  # 1 kilogram = 1,000,000 milligrams
        ("oz", "g"): 28.3495,
        ("oz", "kg"): 0.0283495,
        ("oz", "lb"): 0.0625,
        ("lb", "g"): 453.592,
        ("lb", "kg"): 0.453592,
        ("lb", "oz"): 16,
        ("mg", "g"): 0.001,  # 1 milligram = 0.001 grams
        ("mg", "kg"): 0.000001,  # 1 milligram = 0.000001 kilograms
        ("mg", "oz"): 0.0000352739,  # 1 milligram = 0.0000352739 ounces
        ("mg", "lb"): 0.00000220462,  # 1 milligram = 0.00000220462 pounds
    }

    
    if (msg_from, msg_to) in conversions:
        conversion_factor = conversions[(msg_from, msg_to)]
        converted_value = msg * conversion_factor
        print(f"{msg} {msg_from} = {converted_value} {msg_to}")
    else:
        print("Conversion not supported")
    
def temp_conv():
    msg = int(input("Enter the temperature to convert: "))
    msg_from = input("unit to convert from: ")
    msg_to = input("unit to convert to: ")

    conversions = {
        ("c", "f"): (msg * 9/5) + 32,
        ("c", "k"): msg + 273.15,
        ("f", "c"): (msg - 32) * 5/9,
        ("f", "k"): ((msg - 32) * 5/9) + 273.15,
        ("k", "c"): msg - 273.15,
        ("k", "f"): ((msg - 273.15) * 9/5) + 32
    }

    if (msg_from, msg_to) in conversions:
        print(conversions[(msg_from, msg_to)])
    else:
        print("Conversion not supported")
    
codition = True

while codition:
    print_msg = print("""
    1) Length
    2) Weight 
    3) Temperature
    4) Exit
    """)
    choose_cat = int(input("Enter number of what you want: "))

    if choose_cat == 1:
        length_conv()
    elif choose_cat == 2:
        weight_conv()
    elif choose_cat == 3 :
        temp_conv()
    else :
        codition = False
        break
        
