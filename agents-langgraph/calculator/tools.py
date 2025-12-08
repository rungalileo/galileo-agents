"""Calculator tools."""
import math

ALLOWED_NAMES = {
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "sum": sum,
    "pow": pow,
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "exp": math.exp,
    "pi": math.pi,
    "e": math.e,
}

UNIT_CONVERSIONS = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254,
    "kg": 1000,
    "g": 1,
    "mg": 0.001,
    "lb": 453.592,
    "oz": 28.3495,
}


def calculate(expression: str) -> dict:
    """Evaluate a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}}, ALLOWED_NAMES)
        return {"expression": expression, "result": result, "success": True}
    except Exception as e:
        return {"expression": expression, "error": str(e), "success": False}


def convert_units(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert between units."""
    from_unit, to_unit = from_unit.lower(), to_unit.lower()

    if from_unit in ["c", "f", "k"] or to_unit in ["c", "f", "k"]:
        return _convert_temperature(value, from_unit, to_unit)

    if from_unit not in UNIT_CONVERSIONS or to_unit not in UNIT_CONVERSIONS:
        return {"error": f"Unknown unit: {from_unit} or {to_unit}", "success": False}

    base_value = value * UNIT_CONVERSIONS[from_unit]
    result = base_value / UNIT_CONVERSIONS[to_unit]
    return {
        "original": f"{value} {from_unit}",
        "converted": f"{result:.4f} {to_unit}",
        "value": result,
        "success": True,
    }


def _convert_temperature(value: float, from_unit: str, to_unit: str) -> dict:
    """Convert temperature between C, F, K."""
    if from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15
    else:
        celsius = value

    if to_unit == "f":
        result = celsius * 9 / 5 + 32
    elif to_unit == "k":
        result = celsius + 273.15
    else:
        result = celsius

    return {
        "original": f"{value} {from_unit.upper()}",
        "converted": f"{result:.2f} {to_unit.upper()}",
        "value": result,
        "success": True,
    }
