from abc import ABC, abstractmethod


class Converter(ABC):

    @abstractmethod
    def convert(self, value, from_unit, to_unit):
        pass
    
class UnitConverter(Converter):
    UNIT = {}
    def convert(self, value, from_unit, to_unit):
        if from_unit not in self.UNIT or to_unit not in self.UNIT:
            raise ValueError("Unsupported unit")
        
        if from_unit == to_unit:
            return value
        
        base_unit = value * self.UNIT[from_unit]
        return base_unit / self.UNIT[to_unit]
    
class LengthConverter(UnitConverter):
    UNIT = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "in": 0.0254,
        "ft": 0.3048,
        "yd": 0.9144,
        "mi": 1609.34
    }
    
class WeightConverter(UnitConverter):
    UNIT = {
        "mg": 0.000001,
        "g": 0.001,
        "kg": 1,
        "oz": 0.0283495,
        "lb": 0.453592
    }

class TemperatureConverter(Converter):
    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        
        conversion = {
            ("C", "F"): lambda x: (x * 9/5) + 32,
            ("F", "C"): lambda x: (x - 32) * 5/9,
            ("F", "K"): lambda x: (x - 32) * 5/9 + 273.15,
            ("K", "F"): lambda x: (x - 273.15) * 9/5 + 32,
            ("K", "C"): lambda x: (x - 273.15),
            ("C", "K"): lambda x: (x + 273.15),
        }
        
        try:
            return conversion[(from_unit, to_unit)](value)
        except KeyError:
            raise ValueError(f"Unsupported temperature conversion: {from_unit} to {to_unit}")
    
    