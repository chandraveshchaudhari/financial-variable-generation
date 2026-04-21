import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from financial_data_creation import DataCreation
from financial_data_creation.data_generation import validate_input_data


class DataCreationTests(unittest.TestCase):
    def test_generate_derives_chained_metrics(self):
        input_data = {
            "current_assets_value": 120.0,
            "current_liabilities_value": 100.0,
            "liabilities_value": 300.0,
            "equity_value": 200.0,
            "revenue_value": 500.0,
            "operating_expenses_value": 350.0,
        }

        generated = DataCreation(input_data).generate()

        self.assertEqual(generated["working_capital_value"], 20.0)
        self.assertEqual(generated["assets_value"], 500.0)
        self.assertEqual(generated["ebit_value"], 150.0)
        self.assertAlmostEqual(generated["current_ratio_value"], 1.2)
        self.assertAlmostEqual(generated["financial_leverage_value"], 2.5)

    def test_zero_result_is_preserved(self):
        input_data = {
            "revenue_value": 100.0,
            "cost_of_goods_sold_value": 100.0,
        }

        generated = DataCreation(input_data).generate()

        self.assertIn("gross_profit_value", generated)
        self.assertEqual(generated["gross_profit_value"], 0.0)

    def test_invalid_non_numeric_values_are_filtered(self):
        validated, invalidated = validate_input_data(
            {
                "revenue_value": 100.0,
                "notes": "not numeric",
                "is_estimated": True,
            }
        )

        self.assertEqual(validated, {"revenue_value": 100.0})
        self.assertEqual(
            invalidated,
            {
                "notes": "not numeric",
                "is_estimated": True,
            },
        )

    def test_unsupported_type_raises_value_error(self):
        with self.assertRaises(ValueError):
            DataCreation({}, type_of_data="technical_data").generate()


if __name__ == "__main__":
    unittest.main()
