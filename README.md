<div align="left">
  <table>
    <tr>
      <td width="150" valign="middle">
        <img
          src="https://raw.githubusercontent.com/chandraveshchaudhari/chandraveshchaudhari/b4b4c8ff7b7b9747e3c8a67a2ab561e4aae7d7df/data/logo.png"
          alt="Financial Variable Generation logo"
          width="120"
        />
      </td>
      <td valign="middle">
        <h1>Financial Variable Generation</h1>
        <p>Generate financial ratios and derived fundamental-analysis variables from extracted financial statement data.</p>
      </td>
    </tr>
  </table>
</div>

Financial Variable Generation is a lightweight Python package for taking raw values from balance sheets, income statements, and related datasets, then automatically deriving the financial ratios and intermediate metrics that can be computed from them.

Instead of manually wiring each dependency yourself, the package inspects the available formula inputs, computes what it can, adds the newly derived values back into the working dataset, and keeps going until no more indicators can be generated.

## Features

- Generates derived fundamental indicators from partial input dictionaries.
- Supports ratio families such as leverage, liquidity, efficiency, profitability, and market-related metrics.
- Uses iterative dependency resolution so newly created values can unlock additional formulas.
- Skips invalid divisions safely instead of crashing the full generation flow.
- Keeps the API simple: pass a dictionary in, get an enriched dictionary back.

## Installation

```bash
python3 -m pip install .
```

For editable local development:

```bash
python3 -m pip install -e .
```

## Quick Start

```python
from financial_data_creation import DataCreation

input_data = {
    "current_assets_value": 120.0,
    "current_liabilities_value": 100.0,
    "liabilities_value": 300.0,
    "equity_value": 200.0,
    "revenue_value": 500.0,
    "operating_expenses_value": 350.0,
}

generated = DataCreation(input_data).generate()

print(generated["working_capital_value"])
print(generated["current_ratio_value"])
print(generated["ebit_value"])
print(generated["financial_leverage_value"])
```

Example output:

```python
{
    "current_assets_value": 120.0,
    "current_liabilities_value": 100.0,
    "liabilities_value": 300.0,
    "equity_value": 200.0,
    "revenue_value": 500.0,
    "operating_expenses_value": 350.0,
    "assets_value": 500.0,
    "current_ratio_value": 1.2,
    "ebit_value": 150.0,
    "financial_leverage_value": 2.5,
    "working_capital_value": 20.0,
}
```

## How It Works

1. You provide a dictionary of raw financial statement values.
2. The library validates numeric inputs and ignores invalid non-numeric values.
3. It inspects available formulas and checks whether the required parameters exist.
4. Any computable result is appended back into the dataset with a `_value` suffix.
5. The generator repeats this process until no additional formulas can be resolved.

## Project Structure

- `src/financial_data_creation/fundamental_indicators_formulas.py`: financial formulas and ratio definitions.
- `src/financial_data_creation/data_generation.py`: dependency matching, validation, and indicator generation engine.
- `src/financial_data_creation/__init__.py`: public package exports.

## Current Scope

The package currently focuses on formula-based generation from already extracted financial data. It does not yet include:

- Financial statement parsing from PDFs or filings.
- Automatic market data downloads.
- Full documentation site generation.
- Sector-specific ratio templates or schema validation presets.

## Development

Run the test suite:

```bash
python3 -m unittest discover -s tests
```

Run a quick compile check:

```bash
python3 -m compileall src
```

## Roadmap

- Add grouped APIs for ratio families such as liquidity, leverage, and profitability.
- Add richer schema validation and clearer reporting for skipped inputs.
- Publish package documentation with usage examples for common statement formats.
- Expand tests around chained derivations and edge-case inputs.

## Important Links

- [Source Repository](https://github.com/chandraveshchaudhari/financial-variable-generation)
- [Issue Tracker](https://github.com/chandraveshchaudhari/financial-variable-generation/issues)
- [License](LICENSE.txt)
- [Project Maintainer](mailto:chandraveshchaudhari@gmail.com?subject=[GitHub]%20financial-variable-generation)

## License

This project is released under the MIT License. See [LICENSE.txt](LICENSE.txt) for details.
