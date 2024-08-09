# Crane Calculations

This Python script performs advanced calculations related to crane operations, including line lengths and weights, while considering the angle between the main boom and jib.

## Description

The script calculates various measurements for a crane setup, including:

-   Actual jib length (considering the angle)
-   Extended line length
-   Total line used (including a factor for the pulley system)
-   Total line weight

These calculations are based on predefined crane specifications and use trigonometry to account for the angle between the main boom and jib.

## Usage

To use this script:

1. Ensure you have Python installed on your system.
2. Save the script as `crane_calculations.py`.
3. Run the script using the command: `python crane_calculations.py`

## Specifications

The script uses the following crane specifications:

-   Main boom length: 134 feet
-   Jib length: 174 feet
-   Tip height: 219.98 feet
-   Hook height: 60.0 feet
-   Line load weight: 2.1 pounds per foot
-   Jib angle: 15 degrees (angle between main boom and jib)
-   Pulley factor: 1.1 (10% extra line for pulley system)

## Calculations

The script performs the following calculations:

1. Convert jib angle to radians
2. Calculate actual jib length considering the angle: `jib_length * cos(jib_angle)`
3. Calculate boom and jib line length: `main_boom_length + actual_jib_length`
4. Calculate extended line length: `tip_height - hook_height`
5. Calculate total line length: `(boom_jib_line_length + extended_line_length) * pulley_factor`
6. Calculate total line weight: `total_line_length * line_load_weight`

## Output

The script will print the following information:

-   Main boom length (in feet)
-   Jib length (in feet)
-   Jib angle (in degrees)
-   Actual jib length considering angle (in feet)
-   Extended line length (in feet)
-   Total line used including pulley factor (in feet)
-   Total line weight (in pounds)

## Customization

To modify the crane specifications, update the values at the beginning of the script:

```python
main_boom_length: float = 134.0
jib_length: float = 174.0
tip_height: float = 219.98
hook_height: float = 60.0
line_load_weight: float = 2.1
jib_angle: float = 15.0
pulley_factor: float = 1.1
```

## Notes

-   The `jib_angle` is the angle between the main boom and the jib. Adjust this value based on the crane's configuration.
-   The `pulley_factor` is an estimate of the extra line needed for the pulley system. Adjust this value based on the specific pulley configuration of your crane.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue.
