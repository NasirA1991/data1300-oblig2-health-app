import math

class Health:
    def __init__(self, name: str, weight_kg: float, height_m: float):
        name = name.strip()
        if name == "":
            raise ValueError("Please input a name (required).")
        self.name = name

        if weight_kg <= 0:
            raise ValueError("Weight cannot be zero or less than zero.")
        self.weight_kg = weight_kg

        if height_m <= 0:
            raise ValueError("Height cannot be zero or less than zero.")
        self.height_m = height_m


    def calculate_bmi(self) -> float:
        bmi = self.weight_kg / math.pow(self.height_m, 2)
        return round(bmi, 2)

    def category_bmi(self) -> str:
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi <= 24.9:
            return "Normal"
        elif bmi <= 29.9:
            return "Overweight"
        else:
            return "Obese"

    def get_health_advice(self) -> str:
        category = self.category_bmi()
        advice = ""

        if category == "Underweight":
            advice = "You are underweight. Consider increasing calorie intake with nutrient-dense foods. Strength training may help build muscle mass."
        elif category == "Normal":
            advice = "Your BMI is in the healthy range. Maintain a balanced diet and regular physical activity. Continue your current habits."
        elif category == "Overweight":
            advice = "You are in the overweight range. Consider increasing physical activity. Small dietary improvements can help improve results."
        elif category == "Obese":
            advice = "Your BMI is in the obese range. Consider improving diet and increasing physical activity. Small consistent changes can improve health over time."

        return advice

    def get_ideal_weight(self) -> float:
        return round((22 * math.pow(self.height_m, 2)), 1)