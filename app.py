from flask import Flask, render_template, request

app = Flask(__name__)

# Length Conversion
def conv_length(value, unit_from, unit_to):
    conversions = {
        # Feet conversions
        ("ft", "yard"): value / 3,
        ("ft", "mile"): value / 5280,
        ("ft", "inch"): value * 12,
        ("ft", "m"): value * 0.3048,
        ("ft", "cm"): value * 30.48,
        ("ft", "mm"): value * 304.8,
        ("ft", "km"): value * 0.0003048,

        # Inches conversions
        ("inch", "ft"): value / 12,
        ("inch", "yard"): value / 36,
        ("inch", "mile"): value / 63360,
        ("inch", "m"): value * 0.0254,
        ("inch", "cm"): value * 2.54,
        ("inch", "mm"): value * 25.4,
        ("inch", "km"): value * 0.0000254,

        # Yards conversions
        ("yard", "mile"): value / 1760,
        ("yard", "ft"): value * 3,
        ("yard", "inch"): value * 36,
        ("yard", "m"): value * 0.9144,
        ("yard", "cm"): value * 91.44,
        ("yard", "mm"): value * 914.4,
        ("yard", "km"): value * 0.0009144,

        # Miles conversions
        ("mile", "yard"): value * 1760,
        ("mile", "ft"): value * 5280,
        ("mile", "inch"): value * 63360,
        ("mile", "m"): value * 1609.34,
        ("mile", "cm"): value * 160934,
        ("mile", "mm"): value * 1.609e+6,
        ("mile", "km"): value * 1.60934,

        # Meters conversions
        ("m", "ft"): value / 0.3048,
        ("m", "inch"): value / 0.0254,
        ("m", "yard"): value / 0.9144,
        ("m", "mile"): value / 1609.34,
        ("m", "cm"): value * 100,
        ("m", "mm"): value * 1000,
        ("m", "km"): value / 1000,

        # Centimeters conversions
        ("cm", "ft"): value / 30.48,
        ("cm", "inch"): value / 2.54,
        ("cm", "yard"): value / 91.44,
        ("cm", "mile"): value / 160934,
        ("cm", "m"): value / 100,
        ("cm", "mm"): value * 10,
        ("cm", "km"): value / 100000,

        # Millimeters conversions
        ("mm", "ft"): value / 304.8,
        ("mm", "inch"): value / 25.4,
        ("mm", "yard"): value / 914.4,
        ("mm", "mile"): value / 1.609e+6,
        ("mm", "m"): value / 1000,
        ("mm", "cm"): value / 10,
        ("mm", "km"): value / 1e+6,

        # Kilometers conversions
        ("km", "ft"): value / 0.0003048,
        ("km", "inch"): value / 0.0000254,
        ("km", "yard"): value / 0.0009144,
        ("km", "mile"): value / 1.60934,
        ("km", "m"): value * 1000,
        ("km", "cm"): value * 100000,
        ("km", "mm"): value * 1e+6,
    }
    return conversions.get((unit_from, unit_to), "Invalid Conversion")

# Weight Conversion
def conv_weight(value, unit_from, unit_to):
    conversions = {
        ("g", "kg"): 0.001,
        ("g", "oz"): 0.0352739,
        ("g", "lb"): 0.00220462,
        ("g", "mg"): 1000,
        ("kg", "g"): 1000,
        ("kg", "oz"): 35.274,
        ("kg", "lb"): 2.20462,
        ("kg", "mg"): 1_000_000,
        ("oz", "g"): 28.3495,
        ("oz", "kg"): 0.0283495,
        ("oz", "lb"): 0.0625,
        ("lb", "g"): 453.592,
        ("lb", "kg"): 0.453592,
        ("lb", "oz"): 16,
        ("mg", "g"): 0.001,
        ("mg", "kg"): 0.000001,
        ("mg", "oz"): 0.0000352739,
        ("mg", "lb"): 0.00000220462,
    }
    conversion_factor = conversions.get((unit_from, unit_to))
    return value * conversion_factor if conversion_factor else "Conversion not supported"

# Temperature Conversion
def conv_temperature(value, unit_from, unit_to):
    conversions = {
        ("c", "f"): (value * 9/5) + 32,
        ("c", "k"): value + 273.15,
        ("f", "c"): (value - 32) * 5/9,
        ("f", "k"): ((value - 32) * 5/9) + 273.15,
        ("k", "c"): value - 273.15,
        ("k", "f"): ((value - 273.15) * 9/5) + 32
    }
    return conversions.get((unit_from, unit_to), "Invalid conversion")

# Routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/convert', methods=['POST'])
def converter():
    value = float(request.form['value'])
    from_unit = request.form['from_unit']
    to_unit = request.form['to_unit'] 
    conversion_type = request.form['conversion_type']

    if conversion_type == 'length':
        result = conv_length(value, from_unit, to_unit)
    elif conversion_type == 'weight':
        result = conv_weight(value, from_unit, to_unit)
    elif conversion_type == 'temperature':
        result = conv_temperature(value, from_unit, to_unit)
    else:
        result = "Invalid conversion type"

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
