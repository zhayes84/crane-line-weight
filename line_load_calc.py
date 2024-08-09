# Crane Calculations

# Define crane specifications
main_boom_length: int = 134  # Length of the main boom in feet
jib_length: int = 174  # Length of the jib in feet
tip_height: float = 219.98  # Maximum height of the crane tip in feet
hook_height: float = 60.0  # Height of the hook in feet
line_load_weight: float = 2.1  # Weight of the line in pounds per foot

# Calculate line lengths
boom_jib_line_length: float = (
    main_boom_length + jib_length  # Total length of line along boom and jib
)
extended_line_length: float = (
    tip_height - hook_height  # Length of line extended from tip to hook
)
total_line_length: float = (
    boom_jib_line_length + extended_line_length  # Total length of line used
)

# Calculate total line weight
total_line_weight: float = (
    total_line_length * line_load_weight  # Total weight of the line used
)

# Print results
print(f"\nExtended line length: {extended_line_length:.2f} ft.")
print(f"Total line used: {total_line_length:.2f} ft.")
print(f"Total line weight: {total_line_weight:.2f} lbs\n")
