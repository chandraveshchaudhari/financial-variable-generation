"""
## List of variables
some code is borrowed from https://github.com/srbrettle/Financial-Formulas

#### Primitive formulas

"""


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


def liabilities(assets_value, shareholders_equity_value):
    return assets_value - shareholders_equity_value


def net_profit(gross_profit_value, operating_expenses, taxes, interest):
    return gross_profit_value - operating_expenses - taxes - interest


def operating_profit(gross_profit_value, operating_expenses):
    return gross_profit_value - operating_expenses


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


def units_of_production(
        cost_of_asset,
        residual_value,
        estimated_total_production,
        actual_production):
    return ((cost_of_asset - residual_value) /
            estimated_total_production) * actual_production


def straight_line_method(
        cost_of_fixed_asset,
        residual_value,
        useful_life_of_asset):
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


def dividends_payout_ratio(cash_dividends_paid_on_common_equity, net_income):
    return cash_dividends_paid_on_common_equity / net_income


def plowback_ratio(dividends, earnings):
    return 1 - dividends_payout_ratio(dividends, earnings)


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


def asset_growth_rate(final_asset_value, initial_asset_value):
    return (final_asset_value - initial_asset_value) / initial_asset_value


def asset_liabilities_ratio(assets_value, liabilities_value):
    return assets_value / liabilities_value


def long_term_debt_ratio(long_term_debt, shareholders_equity_value):
    return long_term_debt / (long_term_debt + shareholders_equity_value)


def long_term_debt_equity_ratio(long_term_liabilities, shareholders_equity_value):
    return long_term_liabilities / shareholders_equity_value


def debt_to_total_assets(total_debt, total_assets):
    return total_debt / total_assets


def debt_to_equity(total_debt, total_shareholders_equity):
    return total_debt / total_shareholders_equity


def financial_leverage(average_assets, average_shareholders_equity):
    return average_assets / average_shareholders_equity


def debt_equity_ratio(long_term_debt, shareholders_equity_value):
    return long_term_debt / shareholders_equity_value


def total_debt_ratio():
    return total_liabilities / total_assets


def debt_ratio(total_liabilities, total_assets):
    return total_liabilities / total_assets


def debt_service_coverage_ratio(net_operating_income, total_debt_service):
    return net_operating_income / total_debt_service


def times_interest_earned(ebit_value, interest_payments):
    return ebit_value, interest_payments


def cash_coverage_ratio(ebit_value, depreciation, interest_payments):
    return (ebit_value + depreciation) / interest_payments


def operating_cash_flow_ratio(operating_cash_flow, total_debts):
    return operating_cash_flow / total_debts


def cash_flow_from_operating_activities_to_interest(cash_flow_from_operating_activities, interest, taxes_paid_in_cash,
                                                    interest_expense):
    return (cash_flow_from_operating_activities + interest + taxes_paid_in_cash) / interest_expense


def cash_flow_from_operating_activities_to_debt(cash_flow_from_operating_activities, interest, taxes_paid_in_cash,
                                                average_total_liabilities):
    return (cash_flow_from_operating_activities + interest + taxes_paid_in_cash) / average_total_liabilities


"""
##### Liquidity ratios
- Cash ratio 
- Current ratio 
- NWC to assets 
- Quick ratio
"""
""" liquidity """


def net_working_capital_to_total_assets_ratio(net_working_capital, total_assets):
    return net_working_capital / total_assets


def cash_ratio(cash, marketable_securities, current_liabilities):
    return (cash + marketable_securities) / current_liabilities


def cash_flow_from_operating_activities_ratio(cash_flow_from_operating_activities, average_current_liabilities):
    return cash_flow_from_operating_activities / average_current_liabilities


def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities


def quick_or_acid_test_ratio(cash, marketable_securities, receivables, current_liabilities):
    return (cash + marketable_securities + receivables) / current_liabilities


def interval_measure(cash, marketable_securities, receivables, average_daily_expenditures_from_operation):
    return (cash + marketable_securities + receivables) / average_daily_expenditures_from_operation


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


def fixed_asset_turnover(net_sales, average_net_fixed_assets):
    return net_sales / average_net_fixed_assets


def working_capital_turnover(net_sales, average_working_capital):
    return net_sales / average_working_capital


def efficiency_ratio(non_interest_expense, revenue):
    return non_interest_expense / revenue


def asset_turnover_ratio(net_sales, average_total_assets):
    """.. math:: \int_0^a x\, dx=\frac{1}{2}a^2

    Parameters
    ----------
    average_total_assets
    net_sales
    total_assets

    Returns
    -------

    """
    return net_sales / average_total_assets


def receivable_turnover(net_sales, average_net_trade_receivables):
    return net_sales / average_net_trade_receivables


def average_receivables_collection_days(net_sales, average_net_trade_receivables):
    return 365 / receivable_turnover(net_sales, average_net_trade_receivables)


def cash_conversion_cycle(inventory_conversion_period, receivables_conversion_period, payables_conversion_period):
    return (inventory_conversion_period
            + receivables_conversion_period - payables_conversion_period)


def inventory_conversion_period(inventory_turnover_ratio):
    return 365 / inventory_turnover_ratio


def inventory_conversion_ratio(sales, cost_of_goods_sold):
    return (sales * 0.5) / cost_of_goods_sold


def inventory_turnover(cost_of_goods_sold, average_inventory):
    return cost_of_goods_sold / average_inventory


def payables_conversion_period(accounts_payable, purchases):
    return (accounts_payable / purchases) * 365


def purchases(cost_of_goods_sold, change_in_inventory):
    return cost_of_goods_sold + change_in_inventory


def payables_turnover(purchase_amount, average_accounts_payable):
    return purchase_amount / average_accounts_payable


def average_days_payables_outstanding(payables_turnover_amount):
    return 365 / payables_turnover_amount


def receivables_conversion_period(receivables, net_sales):
    return (receivables / net_sales) * 365


def receivables_turnover_ratio(net_credit_sales, average_net_receivables):
    return net_credit_sales / average_net_receivables


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


def earnings_per_share(net_income, preferred_dividends, ):
    return (net_income - preferred_dividends) / weighted_common_shares_outstanding


def market_to_book_ratio(market_value_of_equity, book_value_of_equity):
    return market_value_of_equity / book_value_of_equity


def price_earnings_ratio(market_price_of_stock, earnings_per_share):
    return market_price_of_stock / earnings_per_share


def net_profit_margin(net_income, sales):
    return net_income / sales


def gross_profit_margin(gross_profit, revenue):
    return gross_profit / revenue


def gross_margin(net_sales, cost_of_goods_sold):
    return net_sales - cost_of_goods_sold


def gross_profit_margin_on_sales(gross_margin_amount, net_sales):
    return gross_margin_amount, net_sales


def operating_margin(operating_income_amount, revenue):
    return operating_income_amount / revenue


def profit_margin(net_profit, revenue):
    return net_profit / revenue


def return_on_assets(net_income, interest, interest_tax_shields, average_total_assets):
    return (net_income + interest - interest_tax_shields) / average_total_assets


def return_on_capital(ebit, tax_rate, invested_capital):
    return ebit * (1 - tax_rate) / invested_capital


def return_on_equity(net_income, average_shareholders_equity):
    return net_income / average_shareholders_equity


def return_on_net_assets(net_income, fixed_assets, working_capital):
    return net_income / (fixed_assets + working_capital)


def risk_adjusted_return_on_capital(expected_return, economic_capital):
    return expected_return / economic_capital


def return_on_investment(gain, cost):
    return (gain - cost) / cost


""" market """


def peg_ratio(price_per_earnings, annual_eps_growth):
    return price_per_earnings / annual_eps_growth


def price_sales_ratio(price_per_share, revenue_per_share):
    return price_per_share / revenue_per_share


"""
References

https://faculty.fuqua.duke.edu/~qc2/accountg441/files/Note%20on%20Financial%20Ratio%20Formula.pdf

Richard, A. B., Stewart, C. M., & Alan, J. M. (2001). Fundamentals of corporate finance. McGraw-Hill.

"""
