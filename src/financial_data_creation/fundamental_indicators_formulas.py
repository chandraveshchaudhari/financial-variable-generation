"""
## List of variables

abbreviations:
earnings before interest and taxes (EBIT)
#### Primitive formulas

"""


def working_capital(current_assets_value, current_liabilities_value):
    return current_assets_value - current_liabilities_value


def ebitda(ebit_value, depreciation_value, amortization_value):
    return ebit_value + depreciation_value + amortization_value


def assets(liabilities_value, equity_value):
    return liabilities_value + equity_value


def ebit(revenue_value, operating_expenses_value):
    return revenue_value - operating_expenses_value


def equity(assets_value, liabilities_value):
    return assets_value - liabilities_value


def gross_profit(revenue_value, cost_of_goods_sold_value):
    return revenue_value - cost_of_goods_sold_value


def growth_rate(final_value, initial_value):
    return (final_value - initial_value) / initial_value


def liabilities(assets_value, equity_value):
    return assets_value - equity_value


def net_profit(gross_profit_value, operating_expenses_value, taxes_value, interest_value):
    return gross_profit_value - operating_expenses_value - taxes_value - interest_value


def net_assets(fixed_assets_value, current_assets_value, current_liabilities_value, long_term_liabilities_value):
    return (fixed_assets_value + current_assets_value) - (current_liabilities_value + long_term_liabilities_value)


def net_sales(sales_revenue_value, sales_returns_value, sales_discounts_value, sales_allowances_value):
    return sales_revenue_value - (sales_returns_value + sales_discounts_value + sales_allowances_value)


def operating_profit(gross_profit_value, operating_expenses_value):
    return gross_profit_value - operating_expenses_value


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


def sales_revenue(gross_sales_value, sales_of_returns_and_allowances_value):
    return gross_sales_value - sales_of_returns_and_allowances_value


""" depreciation """


def average_plant_property_and_equipment_age(accumulated_depreciation_value, depreciation_expense_value):
    return accumulated_depreciation_value / depreciation_expense_value


def average_plant_property_and_equipment_useful_life(ending_balance_of_gross_plant_property_and_equipment_value,
                                                     depreciation_expense_value):
    return ending_balance_of_gross_plant_property_and_equipment_value / depreciation_expense_value


def book_value_of_plant_property_and_equipment(acquisition_cost_value, depreciation_value):
    return acquisition_cost_value - depreciation_value


def declining_balance(depreciation_rate_value, book_value_at_beginning_of_year_value):
    return depreciation_rate_value * book_value_at_beginning_of_year_value


def units_of_production(cost_of_assets_value, residual_value, estimated_production_value, actual_production_value):
    return ((cost_of_assets_value - residual_value) / estimated_production_value) * actual_production_value


def straight_line_method(cost_of_fixed_assets_value, residual_value, useful_life_of_assets_value):
    return (cost_of_fixed_assets_value - residual_value) / useful_life_of_assets_value


# market
def dividend_cover(earnings_per_share_amount_value, dividends_per_share_value):
    return earnings_per_share_amount_value / dividends_per_share_value


def dividends_per_share(dividends_paid_value, number_of_shares_value):
    return dividends_paid_value / number_of_shares_value


def dividend_yield(annual_dividend_per_share_value, price_per_share_value):
    return annual_dividend_per_share_value / price_per_share_value


def calc_earnings_per_share(net_earnings_value, number_of_shares_value):
    return net_earnings_value / number_of_shares_value


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


def assets_growth_rate(final_assets_value, initial_assets_value):
    return growth_rate(final_assets_value, initial_assets_value)


def assets_liabilities_ratio(assets_value, liabilities_value):
    return assets_value / liabilities_value


def capital_expenditures_to_assets(capital_expenditures_value, assets_value):
    return capital_expenditures_value / assets_value


def cash_flow_from_operating_activities_to_interest(cash_flow_from_operating_activities_value, interest_value, taxes_paid_in_cash_value,
                                                    interest_expense_value):
    return (cash_flow_from_operating_activities_value + interest_value + taxes_paid_in_cash_value) / interest_expense_value


def cash_flow_from_operating_activities_to_debt(cash_flow_from_operating_activities_value, interest_value, taxes_paid_in_cash_value,
                                                average_liabilities_value):
    return (cash_flow_from_operating_activities_value + interest_value + taxes_paid_in_cash_value) / average_liabilities_value


def cash_coverage_ratio(ebit_value, depreciation_value, interest_payments_value):
    return (ebit_value + depreciation_value) / interest_payments_value


def cash_debt_coverage_ratio(operating_cash_flow_value, liabilities_value):
    return operating_cash_flow_value / liabilities_value


def debt_to_equity(debt_value, equity_value):
    return debt_value / equity_value


def long_term_debt_to_equity_ratio(long_term_debt_value, equity_value):
    return long_term_debt_value / equity_value


def debt_service_coverage_ratio(net_operating_income_value, debt_service_value):
    return net_operating_income_value / debt_service_value


def equity_to_fixed_assets(equity_value, fixed_assets_value):
    return equity_value / fixed_assets_value


def financial_leverage(average_assets_value, average_equity_value):
    return average_assets_value / average_equity_value


def interest_coverage_formula_or_times_interest_earned(ebit_value, interest_expense_value):
    return ebit_value / interest_expense_value


def long_term_debt_ratio(long_term_debt_value, assets_value):
    return long_term_debt_value / assets_value


def operating_cash_flow_ratio(operating_cash_flow_value, current_liabilities_value):
    return operating_cash_flow_value / current_liabilities_value


def operating_cash_flow_to_liabilities_ratio(operating_cash_flow_value, liabilities_value):
    return operating_cash_flow_value / liabilities_value


def operating_cash_flow_to_net_profit_ratio(operating_cash_flow_value, net_profit_value):
    return operating_cash_flow_value / net_profit_value


def operating_cash_net_flow_to_sales_revenue_ratio(operating_cash_net_flow_value, sales_revenue_value):
    return operating_cash_net_flow_value / sales_revenue_value


def operating_income_to_assets(operating_income_value, assets_value):
    return operating_income_value / assets_value


def operating_leverage_formula(percentage_change_in_operating_income_value, percentage_change_in_revenue_value):
    return percentage_change_in_operating_income_value / percentage_change_in_revenue_value


def degree_of_operating_leverage(contribution_margin_value, operating_margin_value):
    return contribution_margin_value / operating_margin_value


def long_term_funds_to_fixed_assets(long_term_funds_value, fixed_assets_value):
    return long_term_funds_value / fixed_assets_value


def long_term_liabilities_to_equity(long_term_liabilities_value, equity_value):
    return long_term_liabilities_value / equity_value


def equity_ratio(equity_value, assets_value):
    return equity_value / assets_value


def debt_ratio(liabilities_value, assets_value):
    return liabilities_value / assets_value


def debt_to_assets(debt_value, assets_value):
    return debt_value / assets_value


def working_capital_to_assets(working_capital_value, assets_value):
    return working_capital_value / assets_value


"""
##### Liquidity ratios
- Cash ratio 
- Current ratio 
- NWC to assets 
- Quick ratio
"""
""" liquidity """


def cash_ratio(cash_value, marketable_securities_value, current_liabilities_value):
    return (cash_value + marketable_securities_value) / current_liabilities_value


def cash_flow_from_operating_activities_ratio(cash_flow_from_operating_activities_value, average_current_liabilities_value):
    return cash_flow_from_operating_activities_value / average_current_liabilities_value


def current_ratio(current_assets_value, current_liabilities_value):
    return current_assets_value / current_liabilities_value


def interval_measure(cash_value, marketable_securities_value, receivables_value, average_daily_expenditures_from_operation_value):
    return (cash_value + marketable_securities_value + receivables_value) / average_daily_expenditures_from_operation_value


def net_working_capital_to_assets_ratio(net_working_capital_value, assets_value):
    return net_working_capital_value / assets_value


def quick_or_acid_test_ratio(cash_value, marketable_securities_value, receivables_value, current_liabilities_value):
    return (cash_value + marketable_securities_value + receivables_value) / current_liabilities_value


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


def accounts_receivable_days_or_collection_period(accounts_receivable_value, revenue_value, number_of_days_in_year=365):
    return (accounts_receivable_value / revenue_value) * number_of_days_in_year


def accounts_receivable_turnover(net_credit_sales_value, average_accounts_receivable_value):
    return net_credit_sales_value / average_accounts_receivable_value


def average_receivables_collection_days(net_sales_value, average_net_trade_receivables_value, number_of_days_in_year=365):
    return number_of_days_in_year / receivable_turnover(net_sales_value, average_net_trade_receivables_value)


def average_days_payables_outstanding(payables_turnover_amount_value, number_of_days_in_year=365):
    return number_of_days_in_year / payables_turnover_amount_value


def assets_turnover_ratio(net_sales_value, average_assets_value):
    """.. math:: \int_0^a x\, dx=\frac{1}{2}a^2

    """
    return net_sales_value / average_assets_value


def cash_conversion_cycle(inventory_conversion_period_value, receivables_conversion_period_value,
                          payables_conversion_period_value):
    return (inventory_conversion_period_value
            + receivables_conversion_period_value - payables_conversion_period_value)


def current_assets_turnover_ratio(net_sales_value, average_current_assets_value):
    """.. math:: \int_0^a x\, dx=\frac{1}{2}a^2

    Parameters
    ----------
    average_current_assets_value
    net_sales_value

    Returns
    -------

    """
    return net_sales_value / average_current_assets_value


def days_sales_outstanding(average_accounts_receivable_value, revenue_value, number_of_days_in_year=365):
    return number_of_days_in_year * (average_accounts_receivable_value / revenue_value)


def days_sales_in_inventories(average_inventory_value, cost_of_goods_sold_value, number_of_days_in_year=365):
    return number_of_days_in_year * (average_inventory_value / cost_of_goods_sold_value)


def efficiency_ratio(non_interest_expense_value, revenue_value):
    return non_interest_expense_value / revenue_value


def equity_turnover_ratio(net_sale_value, average_equity_value):
    return net_sale_value / average_equity_value


def fixed_assets_turnover(net_sales_value, average_net_fixed_assets_value):
    return net_sales_value / average_net_fixed_assets_value


def inventory_conversion_period(inventory_turnover_ratio_value, number_of_days_in_year=365):
    return number_of_days_in_year / inventory_turnover_ratio_value


def inventory_conversion_ratio(sales_value, cost_of_goods_sold_value):
    return (sales_value * 0.5) / cost_of_goods_sold_value


def inventory_days(inventory_turnover_value, number_of_days_in_year=365):
    return number_of_days_in_year / inventory_turnover_value


def inventory_to_assets(inventory_value, assets_value):
    return inventory_value / assets_value


def inventory_turnover(cost_of_goods_sold_value, average_inventory_value):
    return cost_of_goods_sold_value / average_inventory_value


def net_assets_growth_rate(final_net_assets_value, initial_net_assets_value):
    return growth_rate(final_net_assets_value, initial_net_assets_value)


def payables_conversion_period(accounts_payable_value, purchases_value, number_of_days_in_year=365):
    return (accounts_payable_value / purchases_value) * number_of_days_in_year


def purchases(cost_of_goods_sold_value, change_in_inventory_value):
    return cost_of_goods_sold_value + change_in_inventory_value


def payables_days(purchase_amount_value, average_accounts_payable_value, number_of_days_in_year=365):
    return number_of_days_in_year / payables_turnover(purchase_amount_value, average_accounts_payable_value)


def payables_turnover(purchase_amount_value, average_accounts_payable_value):
    return purchase_amount_value / average_accounts_payable_value


def receivables_conversion_period(receivables_value, net_sales_value, number_of_days_in_year=365):
    return (receivables_value / net_sales_value) * number_of_days_in_year


def receivable_turnover(net_sales_value, average_net_trade_receivables_value):
    return net_sales_value / average_net_trade_receivables_value


def receivables_turnover_ratio(net_credit_sales_value, average_net_receivables_value):
    return net_credit_sales_value / average_net_receivables_value


def sales_to_fixed_assets(net_sales_value, fixed_assets_value, depreciation_value=0):
    return net_sales_value / (fixed_assets_value - depreciation_value)


def sales_to_cash(net_sales_value, cash_value):
    return net_sales_value / cash_value


def sales_to_inventory(net_sales_value, inventory_value):
    return net_sales_value / inventory_value


def working_capital_turnover(net_sales_value, average_working_capital_value):
    return net_sales_value / average_working_capital_value


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


def contribution_margin(revenue_value, variable_costs_value):
    return (revenue_value - variable_costs_value) / revenue_value


def dividends_payout_ratio(cash_dividends_paid_on_common_equity_value, net_income_value):
    return cash_dividends_paid_on_common_equity_value / net_income_value


def earnings_per_share(net_income_value, preferred_dividends_value, weighted_common_shares_outstanding_value):
    return (net_income_value - preferred_dividends_value) / weighted_common_shares_outstanding_value


def ebitda_margin_ratio(ebitda_value, revenue_value):
    return ebitda_value / revenue_value


def gross_profit_margin(gross_profit_value, revenue_value):
    return gross_profit_value / revenue_value


def gross_margin(net_sales_value, cost_of_goods_sold_value):
    return net_sales_value - cost_of_goods_sold_value


def gross_profit_margin_on_sales(gross_margin_amount_value, net_sales_value):
    return gross_margin_amount_value, net_sales_value


def growth_in_equity_from_plowback(return_on_equity_value, plowback_ratio_value):
    return return_on_equity_value * plowback_ratio_value


def market_to_book_ratio(market_value_of_equity_value, book_value_of_equity_value):
    return market_value_of_equity_value / book_value_of_equity_value


def main_business_income_growth(previous_main_business_income_value, final_main_business_income_value):
    return (
                       final_main_business_income_value - previous_main_business_income_value) / previous_main_business_income_value


def net_profit_margin(net_income_value, sales_value):
    return net_income_value / sales_value


def net_cash_flow_of_investing_activities_per_share(net_cash_flow_of_investing_activities_value, number_of_shares_value):
    return net_cash_flow_of_investing_activities_value / number_of_shares_value


def operating_profit_margin(operating_income_value, revenue_value):
    return operating_income_value / revenue_value


def profit_margin(net_profit_value, revenue_value):
    return net_profit_value / revenue_value


def pre_tax_income_to_sales(pre_tax_income_value, sales_value):
    return pre_tax_income_value / sales_value


def market_price_to_book_price_ratio(market_price_value, book_price_value):
    return market_price_value / book_price_value


def plowback_ratio(dividends_value, earnings_value):
    return 1 - dividends_payout_ratio(dividends_value, earnings_value)


""" market """


def peg_ratio(price_per_earnings_value, annual_eps_growth_value):
    return price_per_earnings_value / annual_eps_growth_value


def price_sales_ratio(price_per_share_value, revenue_per_share_value):
    return price_per_share_value / revenue_per_share_value


def price_earnings_ratio(market_price_of_stock_value, earnings_per_share_value):
    return market_price_of_stock_value / earnings_per_share_value


def research_and_development_expense_to_sales(research_and_development_expense_value, sales_value):
    return research_and_development_expense_value / sales_value


def return_on_assets(net_income_value, interest_value, interest_tax_shields_value, average_assets_value):
    return (net_income_value + interest_value - interest_tax_shields_value) / average_assets_value


def return_on_capital_employed(ebit_value, tax_rate_value, invested_capital_value):
    return ebit_value * (1 - tax_rate_value) / invested_capital_value


def risk_adjusted_return_on_capital(expected_return_value, economic_capital_value):
    return expected_return_value / economic_capital_value


def return_on_investment(gain_value, cost_value):
    return (gain_value - cost_value) / cost_value


def return_on_net_assets(net_income_value, fixed_assets_value, working_capital_value):
    return net_income_value / (fixed_assets_value + working_capital_value)


def return_on_sales(operating_profit_value, net_sales_value):
    return operating_profit_value / net_sales_value


def return_on_equity(net_income_value, average_equity_value):
    return net_income_value / average_equity_value


def sales_revenue_growth_rate(final_sales_revenue_value, initial_sales_revenue_value):
    return growth_rate(final_sales_revenue_value, initial_sales_revenue_value)


def sales_to_assets(sales_value, assets_value):
    return sales_value / assets_value


def equity_growth_rate(net_income_value, common_stock_dividends_value, preferred_stock_dividend_value,
                       initial_equity_value):
    return (net_income_value - common_stock_dividends_value - preferred_stock_dividend_value) / initial_equity_value


"""
References

https://faculty.fuqua.duke.edu/~qc2/accountg441/files/Note%20on%20Financial%20Ratio%20Formula.pdf

Richard, A. B., Stewart, C. M., & Alan, J. M. (2001). Fundamentals of corporate finance. McGraw-Hill.

some code is borrowed from https://github.com/srbrettle/Financial-Formulas
"""
