# Crane Calculations
import math

# Define crane specifications
main_boom_length: int = 134  # Length of the main boom in feet
jib_length: int = 174  # Length of the jib in feet
tip_height: float = 219.98  # Maximum height of the crane tip in feet
hook_height: float = 60.0  # Height of the hook in feet
line_load_weight: float = 2.1  # Weight of the line in pounds per foot
jib_angle: float = 15.0  # Angle between main boom and jib in degrees

# Convert jib angle to radians
jib_angle_rad: float = math.radians(jib_angle)

# Calculate actual jib length considering the angle
actual_jib_length: float = jib_length * math.cos(jib_angle_rad)

# Calculate line lengths
boom_jib_line_length: float = main_boom_length + actual_jib_length
extended_line_length: float = tip_height - hook_height

# Add extra length for pulley system (this is an estimate, adjust as needed)
pulley_factor: float = 1.1  # 10% extra for pulley system
total_line_length: float = (boom_jib_line_length + extended_line_length) * pulley_factor

# Calculate total line weight
total_line_weight: float = total_line_length * line_load_weight

# Print results
print(f"\nMain boom length: {main_boom_length:.2f} ft")
print(f"Jib length: {jib_length:.2f} ft")
print(f"Jib angle: {jib_angle:.2f} degrees")
print(f"Actual jib length (considering angle): {actual_jib_length:.2f} ft")
print(f"Extended line length: {extended_line_length:.2f} ft")
print(f"Total line used (including pulley factor): {total_line_length:.2f} ft")
print(f"Total line weight: {total_line_weight:.2f} lbs\n")
