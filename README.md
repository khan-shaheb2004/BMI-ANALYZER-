# BMI Calculator

A professional Python-based Body Mass Index (BMI) calculator that processes multiple individuals, categorizes results according to WHO standards, and generates comprehensive reports.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [BMI Categories](#bmi-categories)
- [Code Structure](#code-structure)
- [Examples](#examples)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

This BMI Calculator is a robust command-line tool designed to:
- Calculate BMI for multiple individuals
- Accept height in feet/inches (imperial) and weight in kilograms (metric)
- Automatically convert measurements to meters
- Categorize results based on WHO standards
- Generate detailed statistical reports

## ✨ Features

- **Multi-person Processing**: Analyze multiple individuals in a single session
- **Automatic Unit Conversion**: Converts feet/inches to meters internally
- **WHO Standard Categories**: Underweight, Normal weight, Overweight, Obese
- **Comprehensive Reporting**: 
  - Individual BMI values
  - Average BMI calculation
  - Category distribution with percentages
  - Professional formatted output
- **Input Validation**: Handles invalid inputs gracefully
- **Error Recovery**: Skips invalid entries and continues processing
- **Session Management**: Option to analyze multiple groups
- **Type Hints**: Full typing support for better code clarity

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only standard library)

### Setup

1. **Clone the repository** (or save the script):
```bash
git clone https://github.com/rari-alam-khan/bmi-analyzer.git
cd bmi-analyzer
