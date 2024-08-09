# Crane Calculations

This Python script performs calculations related to crane operations, including line lengths and weights.

## Description

The script calculates various measurements for a crane setup, including:

-   Extended line length
-   Total line used
-   Total line weight

These calculations are based on predefined crane specifications such as main boom length, jib length, tip height, and hook height.

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

## Calculations

The script performs the following calculations:

1. Boom and jib line length: `main_boom_length + jib_length`
2. Extended line length: `tip_height - hook_height`
3. Total line length: `boom_jib_line_length + extended_line_length`
4. Total line weight: `total_line_length * line_load_weight`

## Output

The script will print the following information:

-   Extended line length (in feet)
-   Total line used (in feet)
-   Total line weight (in pounds)

## Customization

To modify the crane specifications, simply update the values at the beginning of the script:

```python
main_boom_length: int = 134
jib_length: int = 174
tip_height: float = 219.98
hook_height: float = 60.0
line_load_weight: float = 2.1
```

## License

This project is open source and available under the [MIT License](LICENSE).

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue.
