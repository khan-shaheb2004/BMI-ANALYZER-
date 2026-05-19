"""
BMI Calculator - A professional tool to calculate and categorize BMI for multiple individuals.
"""

from typing import List, Tuple, Dict
from dataclasses import dataclass
from enum import Enum


class BMICategory(Enum):
    """BMI categories based on WHO standards."""
    UNDERWEIGHT = "Underweight"
    NORMAL = "Normal weight"
    OVERWEIGHT = "Overweight"
    OBESE = "Obese"


@dataclass
class BMIConstants:
    """Constants for BMI calculations."""
    UNDERWEIGHT_THRESHOLD: float = 18.5
    NORMAL_THRESHOLD: float = 24.9
    OVERWEIGHT_THRESHOLD: float = 29.9
    FEET_TO_METERS: float = 0.3048
    INCHES_TO_METERS: float = 0.0254


class BMIAnalyzer:
    """BMI calculation and analysis tool."""

    def __init__(self):
        self.constants = BMIConstants()
        self.bmi_records: List[float] = []
        self.category_counts: Dict[BMICategory, int] = {category: 0 for category in BMICategory}

    @staticmethod
    def calculate_bmi(weight_kg: float, height_m: float) -> float:
        """
        Calculate BMI using the standard formula.

        Args:
            weight_kg: Weight in kilograms
            height_m: Height in meters

        Returns:
            Calculated BMI value
        """
        if height_m <= 0:
            raise ValueError("Height must be greater than zero")
        if weight_kg <= 0:
            raise ValueError("Weight must be greater than zero")
        return weight_kg / (height_m ** 2)

    @staticmethod
    def convert_height_to_meters(feet: float, inches: float) -> float:
        """
        Convert height from feet and inches to meters.

        Args:
            feet: Height in feet
            inches: Height in inches

        Returns:
            Height in meters
        """
        if feet < 0 or inches < 0:
            raise ValueError("Height measurements cannot be negative")
        return (feet * BMIConstants.FEET_TO_METERS) + (inches * BMIConstants.INCHES_TO_METERS)

    def get_bmi_category(self, bmi: float) -> BMICategory:
        """
        Determine BMI category based on standard thresholds.

        Args:
            bmi: Calculated BMI value

        Returns:
            BMICategory enum value
        """
        if bmi < self.constants.UNDERWEIGHT_THRESHOLD:
            return BMICategory.UNDERWEIGHT
        elif bmi < self.constants.NORMAL_THRESHOLD:
            return BMICategory.NORMAL
        elif bmi < self.constants.OVERWEIGHT_THRESHOLD:
            return BMICategory.OVERWEIGHT
        else:
            return BMICategory.OBESE

    def add_person(self, weight_kg: float, feet: float, inches: float) -> Tuple[float, BMICategory]:
        """
        Process a person's measurements and calculate BMI.

        Args:
            weight_kg: Weight in kilograms
            feet: Height in feet
            inches: Height in inches

        Returns:
            Tuple of (BMI value, BMI Category)
        """
        height_m = self.convert_height_to_meters(feet, inches)
        bmi = self.calculate_bmi(weight_kg, height_m)
        category = self.get_bmi_category(bmi)

        self.bmi_records.append(bmi)
        self.category_counts[category] += 1

        return bmi, category

    def get_average_bmi(self) -> float:
        """Calculate average BMI of all recorded individuals."""
        if not self.bmi_records:
            return 0.0
        return sum(self.bmi_records) / len(self.bmi_records)

    def generate_report(self) -> str:
        """
        Generate a formatted report of all BMI calculations.

        Returns:
            Formatted report string
        """
        if not self.bmi_records:
            return "No data available. Please add records first."

        report_lines = [
            "=" * 50,
            "BMI ANALYSIS REPORT",
            "=" * 50,
            f"Total Individuals Analyzed: {len(self.bmi_records)}",
            f"Average BMI: {self.get_average_bmi():.2f}",
            "-" * 50,
            "CATEGORY DISTRIBUTION:",
        ]

        for category, count in self.category_counts.items():
            percentage = (count / len(self.bmi_records)) * 100
            report_lines.append(f"  {category.value:<15}: {count:>3} ({percentage:>5.1f}%)")

        report_lines.extend([
            "-" * 50,
            "INDIVIDUAL BMI VALUES:",
            f"  {', '.join(f'{bmi:.2f}' for bmi in self.bmi_records)}",
            "=" * 50
        ])

        return "\n".join(report_lines)

    def reset(self):
        """Reset all recorded data."""
        self.bmi_records.clear()
        self.category_counts = {category: 0 for category in BMICategory}


def safe_float_input(prompt: str, min_value: float = 0) -> float:
    """
    Safely get float input from user with validation.

    Args:
        prompt: Input prompt message
        min_value: Minimum allowed value (inclusive)

    Returns:
        Validated float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value < min_value:
                print(f"Value must be at least {min_value}. Please try again.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    """Main program execution."""
    print("\n" + "=" * 50)
    print("PROFESSIONAL BMI CALCULATOR")
    print("=" * 50)

    # Get number of people with validation
    while True:
        try:
            n = int(input("\nHow many people to analyze? "))
            if n <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    analyzer = BMIAnalyzer()

    # Process each person
    for i in range(n):
        print(f"\n--- Person {i + 1} of {n} ---")

        weight = safe_float_input("Weight (kg): ", min_value=0.1)
        feet = safe_float_input("Height (feet): ", min_value=0)
        inches = safe_float_input("Height (inches): ", min_value=0)

        try:
            bmi, category = analyzer.add_person(weight, feet, inches)
            print(f"✓ BMI: {bmi:.2f}")
            print(f"✓ Category: {category.value}")
        except ValueError as e:
            print(f"✗ Error: {e}")
            print("Skipping this entry...")
            continue

    # Generate and display final report
    print("\n" + analyzer.generate_report())

    # Offer reset option
    if input("\nWould you like to analyze another group? (y/n): ").lower().startswith('y'):
        analyzer.reset()
        main()
    else:
        print("\nThank you for using BMI Calculator!")


if __name__ == "__main__":
    main()