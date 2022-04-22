"""
## List of variables

abbreviations:
earnings before interest and taxes (EBIT)
#### Primitive formulas

"""


class CoreFormulas:
    def __init__(self):
        self.description = "This class contains basic formulas needed to calculate other financial ratios."


def working_capital(current_assets, current_liabilities):
    return current_assets - current_liabilities


def ebitda(ebit_value, depreciation, amortization):
    return ebit_value + depreciation + amortization


def assets(liabilities_value, shareholders_equity_value):
    return liabilities_value + shareholders_equity_value


def ebit(revenue, operating_expenses):
    return revenue - operating_expenses


def shareholders_equity(assets_value, liabilities_value):
    return assets_value - liabilities_value


def gross_profit(revenue, cost_of_goods_sold):
    return revenue - cost_of_goods_sold


def growth_rate(final_value, initial_value):
    return (final_value - initial_value) / initial_value


def liabilities(assets_value, shareholders_equity_value):
    return assets_value - shareholders_equity_value


def net_profit(gross_profit_value, operating_expenses, taxes, interest):
    return gross_profit_value - operating_expenses - taxes - interest


def net_assets(total_fixed_assets, total_current_assets, total_current_liabilities, total_long_term_liabilities):
    return (total_fixed_assets + total_current_assets) - (total_current_liabilities + total_long_term_liabilities)


def net_sales(sales_revenue_value, sales_returns, sales_discounts, sales_allowances):
    return sales_revenue_value - (sales_returns + sales_discounts + sales_allowances)


def operating_profit(gross_profit_value, operating_expenses):
    return gross_profit_value - operating_expenses


def operating_income(revenue_value, fixed_or_direct_costs_value, variable_or_indirect_cost_value):
    """
    Operating Income = Gross Profit – Operating Expenses – Depreciation – Amortization
    Operating Income = Total Revenue – Direct Costs – Indirect Cost
    Operating Income = Net Earnings + Interest Expense + Tax
    Returns
    -------

    """
    return revenue_value - fixed_or_direct_costs_value - variable_or_indirect_cost_value


def pre_tax_income(net_sales_value, cost_of_goods_sold_value, operating_expenses_value):
    return net_sales_value - cost_of_goods_sold_value - operating_expenses_value


def sales_revenue(gross_sales, sales_of_returns_and_allowances):
    return gross_sales - sales_of_returns_and_allowances


""" depreciation """


def average_plant_property_and_equipment_age(accumulated_depreciation, depreciation_expense):
    return accumulated_depreciation / depreciation_expense


def average_plant_property_and_equipment_useful_life(ending_balance_of_gross_plant_property_and_equipment,
                                                     depreciation_expense):
    return ending_balance_of_gross_plant_property_and_equipment / depreciation_expense


def book_value(acquisition_cost, depreciation):
    return acquisition_cost - depreciation


def declining_balance(depreciation_rate, book_value_at_beginning_of_year):
    return depreciation_rate * book_value_at_beginning_of_year


def units_of_production(cost_of_asset, residual_value, estimated_total_production, actual_production):
    return ((cost_of_asset - residual_value) / estimated_total_production) * actual_production


def straight_line_method(cost_of_fixed_asset, residual_value, useful_life_of_asset):
    return (cost_of_fixed_asset - residual_value) / useful_life_of_asset


# market
def dividend_cover(earnings_per_share_amount, dividends_per_share_value):
    return earnings_per_share_amount / dividends_per_share_value


def dividends_per_share(dividends_paid, number_of_shares):
    return dividends_paid / number_of_shares


def dividend_yield(annual_dividend_per_share, price_per_share):
    return annual_dividend_per_share / price_per_share


def calc_earnings_per_share(net_earnings, number_of_shares):
    return net_earnings / number_of_shares


"""

### Financial Ratios
- Number of shares outstanding
"""

"""
##### Leverage / solvency ratios
- Asset growth rate 
- asset liability ratio
- Capital Expenditures/total assets 
- Cash coverage ratio 
- Cash debt coverage ratio
- Debt service coverage ratio
- Debt-equity ratio 
- Equity/Fixed assets 
- Financial Leverage formula
- Interest Coverage Formula 
- Long term debt ratio
- Market value equity/total debt 
- Operating cash flow to current liabilities ratio
- Operating cash flow to liabilities ratio
- Operating cash flow to net profit ratio
- Operating cash net flow to sales revenue ratio
- Operating Income to Total assets 
- operating Leverage formula
- Ratio of long-term funds to fixed assets 
- Ratio of long-term liabilities and shareholders' equity 
- Shareholder equity ratio
- Times interest earned 
- Total debt ratio 
- Total debt to total assets
- Working capital to total assets
"""


def validation(financial_indicator_name_and_value_mapping):
    assert bool(financial_indicator_name_and_value_mapping), "financial_indicator_name_and_value_mapping is empty"

    validated_financial_indicator_name_and_value_mapping, invalidated_financial_indicator_name_and_value_mapping = dict() , dict()
    for financial_name, financial_value in financial_indicator_name_and_value_mapping.items():
        if not type(financial_value) in (int, float):
            print(f"{financial_value} is not int or float")
            invalidated_financial_indicator_name_and_value_mapping.update({financial_name: financial_value})
        else:
            validated_financial_indicator_name_and_value_mapping.update({financial_name: financial_value})
    return validated_financial_indicator_name_and_value_mapping, invalidated_financial_indicator_name_and_value_mapping


class LeverageSolvencyRatios:
    def __init__(self, **kwargs):
        self.financial_indicator_name_and_value_mapping = kwargs
        self.validation_financial_indicator_name_and_value_mapping = validation(self.financial_indicator_name_and_value_mapping)[0]

    def generate_indicators(self, selection="LeverageSolvencyRatios"):

        if selection.lower() == "assetsIndicators".lower():
            return AssetsIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators()
        if selection.lower() == "CashIndicators".lower():
            return CashIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators()
        if selection.lower() == "DebtIndicators".lower():
            return DebtIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators()
        if selection.lower() == "LeverageSolvencyRatios".lower():
            leverage_solvency_ratios_dict = dict()
            if AssetsIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators():
                leverage_solvency_ratios_dict = {**AssetsIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators()}
            if CashIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators():
                leverage_solvency_ratios_dict = {**CashIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators()}
            if DebtIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators():
                leverage_solvency_ratios_dict = {**DebtIndicators(**self.validation_financial_indicator_name_and_value_mapping).generate_indicators()}
            if leverage_solvency_ratios_dict:
                return leverage_solvency_ratios_dict

        return None


class GrowthIndicators:
    def __init__(self, prefix=""):
        self.prefix = prefix


def asset_growth_rate(final_asset_value, initial_asset_value):
    return growth_rate(final_asset_value, initial_asset_value)


def operating_leverage_formula(percentage_change_in_operating_income, percentage_change_in_revenue):
    return percentage_change_in_operating_income / percentage_change_in_revenue


def degree_of_operating_leverage(contribution_margin_value, operating_margin_value):
    return contribution_margin_value / operating_margin_value


class AssetsIndicators:
    parameters = {"asset_liabilities_ratio_name": "asset liabilities ratio",
                  "capital_expenditures_to_total_assets_name": "capital expenditures to total assets",
                  "equity_to_fixed_assets_name": "equity to fixed assets",
                  "financial_leverage_name": "financial leverage",
                  "shareholders_equity_ratio_name": "shareholders equity ratio",
                  "debt_ratio_name": "debt ratio",
                  "debt_to_assets_name": "debt to assets",
                  "working_capital_to_assets_name": "working capital to assets",
                  "long_term_funds_to_fixed_assets_name": "long term funds to fixed assets"}
    info = f"""The following variables are needed to create Asset related indicators: \n{parameters}"""

    def __init__(self, assets_value=None, fixed_assets_value=None, average_assets=None, shareholders_equity_value=None,
                 average_shareholders_equity=None, debt_value=None, liabilities_value=None, capital_expenditures=None,
                 working_capital_value=None, long_term_funds_value=None, **kwargs):

        self.assets_value = assets_value
        self.fixed_assets_value = fixed_assets_value
        self.average_assets = average_assets
        self.shareholders_equity_value = shareholders_equity_value
        self.average_shareholders_equity = average_shareholders_equity
        self.debt_value = debt_value
        self.liabilities_value = liabilities_value
        self.capital_expenditures = capital_expenditures
        self.working_capital_value = working_capital_value
        self.long_term_funds_value = long_term_funds_value

    def generate_indicators(self):

        generated_assets_indicators = dict()
        if self.asset_liabilities_ratio():
            generated_assets_indicators[self.parameters["asset_liabilities_ratio_name"]] = self.asset_liabilities_ratio()

        if self.capital_expenditures_to_total_assets():
            generated_assets_indicators[self.parameters["capital_expenditures_to_total_assets_name"]] = self.capital_expenditures_to_total_assets()

        if self.equity_to_fixed_assets():
            generated_assets_indicators[self.parameters["equity_to_fixed_assets_name"]] = self.equity_to_fixed_assets()

        if self.financial_leverage():
            generated_assets_indicators[self.parameters["financial_leverage_name"]] = self.financial_leverage()

        if self.shareholders_equity_ratio():
            generated_assets_indicators[self.parameters["shareholders_equity_ratio_name"]] = self.shareholders_equity_ratio()

        if self.debt_ratio():
            generated_assets_indicators[self.parameters["debt_ratio_name"]] = self.debt_ratio()

        if self.debt_to_assets():
            generated_assets_indicators[self.parameters["debt_to_assets_name"]] = self.debt_to_assets()

        if self.working_capital_to_assets():
            generated_assets_indicators[self.parameters["working_capital_to_assets_name"]] = self.working_capital_to_assets()

        if self.long_term_funds_to_fixed_assets():
            generated_assets_indicators[self.parameters["long_term_funds_to_fixed_assets_name"]] = self.long_term_funds_to_fixed_assets()

        return generated_assets_indicators

    def asset_liabilities_ratio(self):
        if self.assets_value and self.liabilities_value:
            assert self.liabilities_value != 0
            return self.assets_value / self.liabilities_value
        return None

    def capital_expenditures_to_total_assets(self):
        if self.capital_expenditures and self.assets_value:
            assert self.assets_value != 0
            return self.capital_expenditures / self.assets_value
        return None

    def equity_to_fixed_assets(self):
        if self.shareholders_equity_value and self.fixed_assets_value:
            assert self.fixed_assets_value != 0
            return self.shareholders_equity_value / self.fixed_assets_value
        return None

    def financial_leverage(self):
        if self.average_assets and self.average_shareholders_equity:
            assert self.average_shareholders_equity != 0
            return self.average_assets / self.average_shareholders_equity
        return None

    def shareholders_equity_ratio(self):
        if self.shareholders_equity_value and self.assets_value:
            assert self.assets_value != 0
            return self.shareholders_equity_value / self.assets_value
        return None

    def debt_ratio(self):
        if self.liabilities_value and self.assets_value:
            assert self.assets_value != 0
            return self.liabilities_value / self.assets_value
        return None

    def debt_to_assets(self):
        if self.debt_value and self.assets_value:
            assert self.assets_value != 0
            return self.debt_value / self.assets_value
        return None

    def working_capital_to_assets(self):
        if self.working_capital_value and self.assets_value:
            assert self.assets_value != 0
            return self.working_capital_value / self.assets_value
        return None

    def long_term_funds_to_fixed_assets(self):
        if self.long_term_funds_value and self.fixed_assets_value:
            assert self.fixed_assets_value != 0
            return self.long_term_funds_value / self.fixed_assets_value
        return None


class CashIndicators:
    parameters = {"cash_flow_from_operating_activities_to_interest_name": "cash flow from operating activities to interest",
                  "cash_flow_from_operating_activities_to_debt_name": "cash flow from operating activities to debt",
                  "cash_coverage_ratio_name": "cash coverage ratio",
                  "interest_coverage_formula_or_times_interest_earned_name": "interest coverage formula or times interest earned",
                  "cash_debt_coverage_ratio_name": "cash debt coverage ratio",
                  "operating_cash_flow_ratio_name": "operating cash flow ratio",
                  "operating_cash_flow_to_liabilities_ratio_name": "operating cash flow to liabilities ratio",
                  "operating_cash_flow_to_net_profit_ratio_name": "operating cash flow to net profit ratio",
                  "operating_cash_net_flow_to_sales_revenue_ratio_name": "operating cash net flow to sales revenue ratio",
                  "operating_income_to_total_assets_name":"operating income to total assets"}
    info = f"""The following variables are needed to create cash related indicators: \n{parameters}"""

    def __init__(self, cash_flow_from_operating_activities=None, interest=None, interest_expense_value=None,
                 liabilities_value=None, taxes_paid_in_cash=None, average_total_liabilities=None, ebit_value=None,
                 depreciation=None, current_liabilities=None, net_profit_value=None, operating_cash_net_flow=None,
                 sales_revenue_value=None, assets_value=None, operating_income_value=None, **kwargs):
        self.interest_expense_value = interest_expense_value
        self.cash_flow_from_operating_activities = cash_flow_from_operating_activities
        self.interest = interest
        self.liabilities_value = liabilities_value
        self.taxes_paid_in_cash = taxes_paid_in_cash
        self.average_total_liabilities = average_total_liabilities
        self.ebit_value = ebit_value
        self.depreciation = depreciation
        self.current_liabilities = current_liabilities
        self.net_profit_value = net_profit_value
        self.operating_cash_net_flow = operating_cash_net_flow
        self.sales_revenue_value = sales_revenue_value
        self.assets_value = assets_value
        self.operating_income_value = operating_income_value

    def generate_indicators(self):
        generated_cash_indicators = dict()
        if self.cash_flow_from_operating_activities_to_interest():
            generated_cash_indicators[self.parameters["cash_flow_from_operating_activities_to_interest_name"]] = self.cash_flow_from_operating_activities_to_interest()

        if self.cash_flow_from_operating_activities_to_debt():
            generated_cash_indicators[self.parameters["cash_flow_from_operating_activities_to_debt_name"]] = self.cash_flow_from_operating_activities_to_debt()

        if self.cash_coverage_ratio():
            generated_cash_indicators[self.parameters["cash_coverage_ratio_name"]] = self.cash_coverage_ratio()

        if self.interest_coverage_formula_or_times_interest_earned():
            generated_cash_indicators[self.parameters["interest_coverage_formula_or_times_interest_earned_name"]] = self.interest_coverage_formula_or_times_interest_earned()

        if self.cash_debt_coverage_ratio():
            generated_cash_indicators[self.parameters["cash_debt_coverage_ratio_name"]] = self.cash_debt_coverage_ratio()

        if self.operating_cash_flow_ratio():
            generated_cash_indicators[self.parameters["operating_cash_flow_ratio_name"]] = self.operating_cash_flow_ratio()

        if self.operating_cash_flow_to_liabilities_ratio():
            generated_cash_indicators[self.parameters["operating_cash_flow_to_liabilities_ratio_name"]] = self.operating_cash_flow_to_liabilities_ratio()

        if self.operating_cash_flow_to_net_profit_ratio():
            generated_cash_indicators[self.parameters["operating_cash_flow_to_net_profit_ratio_name"]] = self.operating_cash_flow_to_net_profit_ratio()

        if self.operating_cash_net_flow_to_sales_revenue_ratio():
            generated_cash_indicators[self.parameters["operating_cash_net_flow_to_sales_revenue_ratio_name"]] = self.operating_cash_net_flow_to_sales_revenue_ratio()

        if self.operating_income_to_total_assets():
            generated_cash_indicators[self.parameters["operating_income_to_total_assets_name"]] = self.operating_income_to_total_assets()

        return generated_cash_indicators

    def cash_flow_from_operating_activities_to_interest(self):
        if self.cash_flow_from_operating_activities and self.interest and self.taxes_paid_in_cash and self.interest_expense_value:
            assert self.interest_expense_value != 0
            return (self.cash_flow_from_operating_activities + self.interest + self.taxes_paid_in_cash) / self.interest_expense_value
        return None

    def cash_flow_from_operating_activities_to_debt(self):
        if self.cash_flow_from_operating_activities and self.interest and self.taxes_paid_in_cash and self.average_total_liabilities:
            assert self.average_total_liabilities != 0
            return (self.cash_flow_from_operating_activities + self.interest + self.taxes_paid_in_cash) / self.average_total_liabilities
        return None

    def cash_coverage_ratio(self):
        if self.ebit_value and self.depreciation and self.interest_expense_value:
            assert self.interest_expense_value != 0
            return (self.ebit_value + self.depreciation) / self.interest_expense_value
        return None

    def interest_coverage_formula_or_times_interest_earned(self):
        if self.ebit_value and self.interest_expense_value:
            assert self.interest_expense_value != 0
            return self.ebit_value / self.interest_expense_value
        return None

    def cash_debt_coverage_ratio(self):
        if self.cash_flow_from_operating_activities and self.liabilities_value:
            assert self.liabilities_value != 0
            return self.cash_flow_from_operating_activities / self.liabilities_value
        return None

    def operating_cash_flow_ratio(self):
        if self.cash_flow_from_operating_activities and self.current_liabilities:
            assert self.current_liabilities != 0
            return self.cash_flow_from_operating_activities / self.current_liabilities
        return None

    def operating_cash_flow_to_liabilities_ratio(self):
        if self.cash_flow_from_operating_activities and self.liabilities_value:
            assert self.liabilities_value != 0
            return self.cash_flow_from_operating_activities / self.liabilities_value
        return None

    def operating_cash_flow_to_net_profit_ratio(self):
        if self.cash_flow_from_operating_activities and self.net_profit_value:
            assert self.net_profit_value != 0
            return self.cash_flow_from_operating_activities / self.net_profit_value
        return None

    def operating_cash_net_flow_to_sales_revenue_ratio(self):
        if self.operating_cash_net_flow and self.sales_revenue_value:
            assert  self.sales_revenue_value != 0
            return self.operating_cash_net_flow / self.sales_revenue_value
        return None

    def operating_income_to_total_assets(self):
        if self.operating_income_value and self.assets_value:
            assert self.assets_value != 0
            return self.operating_income_value / self.assets_value
        return None


class DebtIndicators:
    parameters = {
        "debt_to_equity_name": "debt to equity",
        "debt_equity_ratio_name": "debt equity ratio",
        "debt_ratio_name": "debt ratio",
        "debt_service_coverage_ratio_name": "debt service coverage ratio",
        "long_term_debt_ratio_name": "long term debt ratio",
        "long_term_debt_equity_ratio_name": "long term debt equity ratio",
        "long_term_liabilities_to_shareholders_equity_name": "long term liabilities to shareholders equity"}
    info = f"""The following variables are needed to create debt related indicators: \n{parameters}"""

    def __init__(self, debt_value=None, long_term_debt=None, total_debt_service=None, shareholders_equity_value=None,
                 liabilities_value=None, assets_value=None, net_operating_income=None, long_term_liabilities=None, **kwargs):
        self.long_term_liabilities = long_term_liabilities
        self.net_operating_income = net_operating_income
        self.liabilities_value = liabilities_value
        self.shareholders_equity_value = shareholders_equity_value
        self.debt_value = debt_value
        self.long_term_debt = long_term_debt
        self.total_debt_service = total_debt_service
        self.assets_value = assets_value

    def generate_indicators(self):
        generated_cash_indicators = dict()

        if self.debt_to_equity():
            generated_cash_indicators[self.parameters["debt_to_equity_name"]] = self.debt_to_equity()

        if self.debt_equity_ratio():
            generated_cash_indicators[self.parameters["debt_equity_ratio_name"]] = self.debt_equity_ratio()

        if self.debt_ratio():
            generated_cash_indicators[self.parameters["debt_ratio_name"]] = self.debt_ratio()

        if self.debt_service_coverage_ratio():
            generated_cash_indicators[self.parameters["debt_service_coverage_ratio_name"]] = self.debt_service_coverage_ratio()

        if self.long_term_debt_ratio():
            generated_cash_indicators[self.parameters["long_term_debt_ratio_name"]] = self.long_term_debt_ratio()

        if self.long_term_debt_equity_ratio():
            generated_cash_indicators[self.parameters["long_term_debt_equity_ratio_name"]] = self.long_term_debt_equity_ratio()

        if self.long_term_liabilities_to_shareholders_equity():
            generated_cash_indicators[self.parameters["long_term_liabilities_to_shareholders_equity_name"]] = self.long_term_liabilities_to_shareholders_equity()

        return generated_cash_indicators

    def debt_to_equity(self):
        if self.debt_value and self.shareholders_equity_value:
            assert self.shareholders_equity_value != 0
            return self.debt_value / self.shareholders_equity_value
        return None

    def debt_equity_ratio(self):
        if self.long_term_debt and self.shareholders_equity_value:
            assert self.shareholders_equity_value != 0
            return self.long_term_debt / self.shareholders_equity_value
        return None

    def debt_ratio(self):
        if self.liabilities_value and self.assets_value:
            assert self.assets_value != 0
            return self.liabilities_value / self.assets_value
        return None

    def debt_service_coverage_ratio(self):
        if self.net_operating_income and self.total_debt_service:
            assert self.total_debt_service != 0
            return self.net_operating_income / self.total_debt_service
        return None

    def long_term_debt_ratio(self):
        if self.long_term_debt and self.long_term_debt and self.shareholders_equity_value:
            assert (self.long_term_debt + self.shareholders_equity_value) != 0
            return self.long_term_debt / (self.long_term_debt + self.shareholders_equity_value)
        return None

    def long_term_debt_equity_ratio(self):
        if self.long_term_liabilities and self.shareholders_equity_value:
            assert self.shareholders_equity_value != 0
            return self.long_term_liabilities / self.shareholders_equity_value
        return None

    def long_term_liabilities_to_shareholders_equity(self):
        if self.long_term_liabilities and self.shareholders_equity_value:
            assert self.shareholders_equity_value != 0
            return self.long_term_liabilities / self.shareholders_equity_value
        return None


"""
##### Liquidity ratios
- Cash ratio 
- Current ratio 
- NWC to assets 
- Quick ratio
"""
""" liquidity """


class LiquidityRatios:
    parameters = {
        "cash_ratio_name": "cash ratio",
        "cash_flow_from_operating_activities_ratio_name": "cash flow from operating activities ratio",
        "current_ratio_name": "current ratio name",
        "interval_measure_name": "interval measure name",
        "net_working_capital_to_total_assets_ratio_name": "net working capital to total assets ratio",
        "quick_or_acid_test_ratio_name": "quick or acid test ratio"}
    info = f"""The following variables are needed to create liquidity related indicators: \n{parameters}"""

    def __init__(self, cash, marketable_securities, current_liabilities, cash_flow_from_operating_activities, 
                 average_current_liabilities, current_assets, receivables, average_daily_expenditures_from_operation,
                 net_working_capital, assets_value):
        self.assets_value = assets_value
        self.net_working_capital = net_working_capital
        self.average_daily_expenditures_from_operation = average_daily_expenditures_from_operation
        self.receivables = receivables
        self.current_assets = current_assets
        self.average_current_liabilities = average_current_liabilities
        self.cash_flow_from_operating_activities = cash_flow_from_operating_activities
        self.current_liabilities = current_liabilities
        self.marketable_securities = marketable_securities
        self.cash = cash

    def generate_indicators(self):
        generated_cash_indicators = dict()

        if self.cash_ratio():
            generated_cash_indicators[self.parameters["cash_ratio_name"]] = self.cash_ratio()

        if self.cash_flow_from_operating_activities_ratio():
            generated_cash_indicators[self.parameters["cash_flow_from_operating_activities_ratio_name"]] = self.cash_flow_from_operating_activities_ratio()

        if self.current_ratio():
            generated_cash_indicators[self.parameters["current_ratio_name"]] = self.current_ratio()

        if self.interval_measure():
            generated_cash_indicators[self.parameters["interval_measure_name"]] = self.interval_measure()

        if self.net_working_capital_to_total_assets_ratio():
            generated_cash_indicators[self.parameters["net_working_capital_to_total_assets_ratio_name"]] = self.net_working_capital_to_total_assets_ratio()

        if self.quick_or_acid_test_ratio():
            generated_cash_indicators[self.parameters["quick_or_acid_test_ratio_name"]] = self.quick_or_acid_test_ratio()

    def cash_ratio(self):
        if self.cash and self.marketable_securities and self.current_liabilities:
            assert self.current_liabilities != 0
            return (self.cash + self.marketable_securities) / self.current_liabilities
        return None

    def cash_flow_from_operating_activities_ratio(self):
        if self.cash_flow_from_operating_activities and self.average_current_liabilities:
            assert self.average_current_liabilities != 0
            return self.cash_flow_from_operating_activities / self.average_current_liabilities
        return None

    def current_ratio(self):
        if self.current_assets and self.current_liabilities:
            assert self.current_liabilities != 0
            return self.current_assets / self.current_liabilities
        return None

    def interval_measure(self):
        if self.cash and self.marketable_securities and self.receivables and self.average_daily_expenditures_from_operation:
            assert self.average_daily_expenditures_from_operation != 0
            return (self.cash + self.marketable_securities + self.receivables) / self.average_daily_expenditures_from_operation
        return None

    def net_working_capital_to_total_assets_ratio(self):
        if self.net_working_capital and self.assets_value:
            assert self.assets_value != 0
            return self.net_working_capital / self.assets_value
        return None

    def quick_or_acid_test_ratio(self):
        if self.cash and self.marketable_securities and self.receivables and self.current_liabilities:
            assert self.current_liabilities != 0
            return (self.cash + self.marketable_securities + self.receivables) / self.current_liabilities
        return None


"""
##### Efficiency ratios
- Accounts Receivables Days Formula 
- Accounts Receivables Turnover 
- Asset Turnover ratio Formula 
- Average collection period 
- Cash conversion cycle
- Current asset turnover ratio 
- Days sales outstanding
- Days' sales in inventories 
- Equity Turnover Ratio Formula 
- Fixed asset turnover
- Growth rate of total assets
- inventory conversion period
- inventory conversion ratio
- Inventory Days Formula 
- Inventory to total assets 
- Inventory turnover 
- Net asset growth rate
- payables conversion period
- payables Days 
- payables Turnover 
- receivables conversion period
- Sales to Fixed assets 
- Sales to total cash 
- Sales to total Inventory 
- Sales to total working capital or Working capital turnover 
- Total asset turnover 
"""

class EfficiencyRatios:
    pass

def accounts_receivable_days_or_collection_period(accounts_receivable_value, revenue, number_of_days_in_year=365):
    return (accounts_receivable_value / revenue) * number_of_days_in_year


def accounts_receivable_turnover(net_credit_sales_value, average_accounts_receivable_value):
    return net_credit_sales_value / average_accounts_receivable_value


def average_receivables_collection_days(net_sales_value, average_net_trade_receivables, number_of_days_in_year=365):
    return number_of_days_in_year / receivable_turnover(net_sales_value, average_net_trade_receivables)


def average_days_payables_outstanding(payables_turnover_amount, number_of_days_in_year=365):
    return number_of_days_in_year / payables_turnover_amount


def asset_turnover_ratio(net_sales_value, average_total_assets):
    """.. math:: \int_0^a x\, dx=\frac{1}{2}a^2

    """
    return net_sales_value / average_total_assets


def cash_conversion_cycle(inventory_conversion_period_value, receivables_conversion_period_value,
                          payables_conversion_period_value):
    return (inventory_conversion_period_value
            + receivables_conversion_period_value - payables_conversion_period_value)


def current_asset_turnover_ratio(net_sales_value, average_current_assets):
    """.. math:: \int_0^a x\, dx=\frac{1}{2}a^2

    Parameters
    ----------
    average_current_assets
    net_sales_value

    Returns
    -------

    """
    return net_sales_value / average_current_assets


def days_sales_outstanding(average_accounts_receivable_value, revenue, number_of_days_in_year=365):
    return number_of_days_in_year * (average_accounts_receivable_value / revenue)


def days_sales_in_inventories(average_inventory_value, cost_of_goods_sold_value, number_of_days_in_year=365):
    return number_of_days_in_year * (average_inventory_value / cost_of_goods_sold_value)


def efficiency_ratio(non_interest_expense, revenue):
    return non_interest_expense / revenue


def equity_turnover_ratio(net_sale_value, average_shareholders_equity):
    return net_sale_value / average_shareholders_equity


def fixed_asset_turnover(net_sales_value, average_net_fixed_assets):
    return net_sales_value / average_net_fixed_assets


class InventoryRatios:
    pass


def inventory_conversion_period(inventory_turnover_ratio, number_of_days_in_year=365):
    return number_of_days_in_year / inventory_turnover_ratio


def inventory_conversion_ratio(sales, cost_of_goods_sold):
    return (sales * 0.5) / cost_of_goods_sold


def inventory_days(inventory_turnover_value, number_of_days_in_year=365):
    return number_of_days_in_year / inventory_turnover_value


def inventory_to_total_assets(inventory_value, total_assets):
    return inventory_value / total_assets


def inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory


def net_asset_growth_rate(final_net_asset_value, initial_net_asset_value):
    return growth_rate(final_net_asset_value, initial_net_asset_value)


class PurchasesRatios:
    pass


def payables_conversion_period(accounts_payable, purchases_value, number_of_days_in_year=365):
    return (accounts_payable / purchases_value) * number_of_days_in_year


def purchases(cost_of_goods_sold, change_in_inventory):
    return cost_of_goods_sold + change_in_inventory


def payables_days(purchase_amount, average_accounts_payable, number_of_days_in_year=365):
    return number_of_days_in_year / payables_turnover(purchase_amount, average_accounts_payable)


def payables_turnover(purchase_amount, average_accounts_payable):
    return purchase_amount / average_accounts_payable


class SalesRatios:
    pass


def receivables_conversion_period(receivables, net_sales_value, number_of_days_in_year=365):
    return (receivables / net_sales_value) * number_of_days_in_year


def receivable_turnover(net_sales_value, average_net_trade_receivables):
    return net_sales_value / average_net_trade_receivables


def receivables_turnover_ratio(net_credit_sales, average_net_receivables):
    return net_credit_sales / average_net_receivables


def sales_to_fixed_assets(net_sales_value, fixed_assets_value, depreciation=0):
    return net_sales_value / (fixed_assets_value - depreciation)


def sales_to_total_cash(net_sales_value, cash_value):
    return net_sales_value / cash_value


def sales_to_total_inventory(net_sales_value, inventory_value):
    return net_sales_value / inventory_value


def working_capital_turnover(net_sales_value, average_working_capital):
    return net_sales_value / average_working_capital


"""
##### Profitability ratios
- Dividends payout ratio 
- Earnings per share (EPS)
- EBITDA Margin Ratio
- Gross profit margin 
- Growth in equity from plowback 
- Main business income growth
- Net cash flow of investing activities per share 
- Net profit margin
- Operating Profit Margin 
- Plowback ratio 
- Pre taxes income/Sales 
- price to book ratio (P/B)
- price to sales ratio (P/S)
- Price- Earnings ratio 
- Research & Development Expense to Sales 
- Return on assets (ROA)
- Return on Capital Employed (ROCE) 
- Return on Investment (ROI)
- Return on net assets
- Return on sales
- ROE or Return on Equity Formula 
- Sales revenue growth rate 
- Sales/Total Assest
- Shareholder equity growth rate
"""

""" profitability """


class ProfitabilityRatios:
    pass


def contribution_margin(revenue, variable_costs):
    return (revenue - variable_costs) / revenue


def dividends_payout_ratio(cash_dividends_paid_on_common_equity, net_income):
    return cash_dividends_paid_on_common_equity / net_income


def earnings_per_share(net_income, preferred_dividends, weighted_common_shares_outstanding):
    return (net_income - preferred_dividends) / weighted_common_shares_outstanding


def ebitda_margin_ratio(ebitda_value, revenue_value):
    return ebitda_value / revenue_value


def gross_profit_margin(gross_profit_value, revenue):
    return gross_profit_value / revenue


def gross_margin(net_sales_value, cost_of_goods_sold):
    return net_sales_value - cost_of_goods_sold


def gross_profit_margin_on_sales(gross_margin_amount, net_sales_value):
    return gross_margin_amount, net_sales_value


def growth_in_equity_from_plowback(roe_value, plowback_ratio_value):
    return roe_value * plowback_ratio_value


def market_to_book_ratio(market_value_of_equity, book_value_of_equity):
    return market_value_of_equity / book_value_of_equity


def main_business_income_growth(previous_main_business_income_value, final_main_business_income_value):
    return (
                       final_main_business_income_value - previous_main_business_income_value) / previous_main_business_income_value


def net_profit_margin(net_income, sales):
    return net_income / sales


def net_cash_flow_of_investing_activities_per_share(net_cash_flow_of_investing_activities, number_of_shares):
    return net_cash_flow_of_investing_activities / number_of_shares


def operating_profit_margin(operating_income_value, revenue_value):
    return operating_income_value / revenue_value


def profit_margin(net_profit_value, revenue):
    return net_profit_value / revenue


def pre_tax_income_to_sales(pre_tax_income_value, sales_value):
    return pre_tax_income_value / sales_value


def market_price_to_book_price_ratio(market_price_value, book_price_value):
    return market_price_value / book_price_value


def plowback_ratio(dividends, earnings):
    return 1 - dividends_payout_ratio(dividends, earnings)


""" market """


def peg_ratio(price_per_earnings, annual_eps_growth):
    return price_per_earnings / annual_eps_growth


def price_sales_ratio(price_per_share, revenue_per_share):
    return price_per_share / revenue_per_share


def price_earnings_ratio(market_price_of_stock, earnings_per_share_value):
    return market_price_of_stock / earnings_per_share_value


def research_and_development_expense_to_sales(research_and_development_expense_value, sales_value):
    return research_and_development_expense_value / sales_value


def return_on_assets(net_income, interest, interest_tax_shields, average_total_assets):
    return (net_income + interest - interest_tax_shields) / average_total_assets


def return_on_capital_employed(ebit, tax_rate, invested_capital):
    return ebit * (1 - tax_rate) / invested_capital


def risk_adjusted_return_on_capital(expected_return, economic_capital):
    return expected_return / economic_capital


def return_on_investment(gain, cost):
    return (gain - cost) / cost


def return_on_net_assets(net_income, fixed_assets, working_capital_value):
    return net_income / (fixed_assets + working_capital_value)


def return_on_sales(operating_profit_value, net_sales_value):
    return operating_profit_value / net_sales_value


def return_on_equity(net_income, average_shareholders_equity):
    return net_income / average_shareholders_equity


def sales_revenue_growth_rate(final_sales_revenue_value, initial_sales_revenue_value):
    return growth_rate(final_sales_revenue_value, initial_sales_revenue_value)


def sales_to_total_asset(sales_value, total_asset_value):
    return sales_value / total_asset_value


def shareholders_equity_growth_rate(net_income_value, common_stock_dividends, preferred_stock_dividend,
                                    initial_shareholders_equity_value):
    return (net_income_value - common_stock_dividends - preferred_stock_dividend) / initial_shareholders_equity_value


"""
References

https://faculty.fuqua.duke.edu/~qc2/accountg441/files/Note%20on%20Financial%20Ratio%20Formula.pdf

Richard, A. B., Stewart, C. M., & Alan, J. M. (2001). Fundamentals of corporate finance. McGraw-Hill.

some code is borrowed from https://github.com/srbrettle/Financial-Formulas
"""
