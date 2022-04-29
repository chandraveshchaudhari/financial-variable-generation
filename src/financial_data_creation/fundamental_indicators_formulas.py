"""
## List of variables

abbreviations:
earnings before interest and taxes (EBIT)
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


def asset_growth_rate(final_asset_value, initial_asset_value):
    return growth_rate(final_asset_value, initial_asset_value)


def asset_liabilities_ratio(assets_value, liabilities_value):
    return assets_value / liabilities_value


def capital_expenditures_to_total_assets(capital_expenditures, total_assets):
    return capital_expenditures / total_assets


def cash_flow_from_operating_activities_to_interest(cash_flow_from_operating_activities, interest, taxes_paid_in_cash,
                                                    interest_expense):
    return (cash_flow_from_operating_activities + interest + taxes_paid_in_cash) / interest_expense


def cash_flow_from_operating_activities_to_debt(cash_flow_from_operating_activities, interest, taxes_paid_in_cash,
                                                average_total_liabilities):
    return (cash_flow_from_operating_activities + interest + taxes_paid_in_cash) / average_total_liabilities


def cash_coverage_ratio(ebit_value, depreciation, interest_payments):
    return (ebit_value + depreciation) / interest_payments


def cash_debt_coverage_ratio(operating_cash_flow, total_liabilities):
    return operating_cash_flow / total_liabilities


def debt_to_total_assets(total_debt, total_assets):
    return total_debt / total_assets


def debt_to_equity(total_debt, total_shareholders_equity):
    return total_debt / total_shareholders_equity


def debt_equity_ratio(long_term_debt, shareholders_equity_value):
    return long_term_debt / shareholders_equity_value


def debt_ratio(total_liabilities, total_assets):
    return total_liabilities / total_assets


def debt_service_coverage_ratio(net_operating_income, total_debt_service):
    return net_operating_income / total_debt_service


def equity_to_fixed_assets(equity_value, fixed_assets_value):
    return equity_value / fixed_assets_value


def financial_leverage(average_assets, average_shareholders_equity):
    return average_assets / average_shareholders_equity


def interest_coverage_formula_or_times_interest_earned(ebit_value, interest_expense_value):
    return ebit_value / interest_expense_value


def long_term_debt_ratio(long_term_debt, shareholders_equity_value):
    return long_term_debt / (long_term_debt + shareholders_equity_value)


def long_term_debt_equity_ratio(long_term_liabilities, shareholders_equity_value):
    return long_term_liabilities / shareholders_equity_value


def operating_cash_flow_ratio(operating_cash_flow, current_liabilities):
    return operating_cash_flow / current_liabilities


def operating_cash_flow_to_liabilities_ratio(operating_cash_flow, liabilities):
    return operating_cash_flow / liabilities


def operating_cash_flow_to_net_profit_ratio(operating_cash_flow, net_profit_value):
    return operating_cash_flow / net_profit_value


def operating_cash_net_flow_to_sales_revenue_ratio(operating_cash_net_flow, sales_revenue_value):
    return operating_cash_net_flow / sales_revenue_value


def operating_income_to_total_assets(operating_income, total_assets):
    return operating_income / total_assets


def operating_leverage_formula(percentage_change_in_operating_income, percentage_change_in_revenue):
    return percentage_change_in_operating_income / percentage_change_in_revenue


def degree_of_operating_leverage(contribution_margin_value, operating_margin_value):
    return contribution_margin_value / operating_margin_value


def long_term_funds_to_fixed_assets(long_term_funds_value, fixed_assets_value):
    return long_term_funds_value / fixed_assets_value


def long_term_liabilities_to_shareholders_equity(long_term_liabilities, shareholders_equity_value):
    return long_term_liabilities / shareholders_equity_value


def shareholders_equity_ratio(shareholders_equity_value, total_assets_value):
    return shareholders_equity_value / total_assets_value


def total_debt_ratio(total_liabilities, total_assets_value):
    return total_liabilities / total_assets_value


def total_debt_to_total_assets(total_debt_value, total_assets_value):
    return total_debt_value / total_assets_value


def working_capital_to_total_assets(working_capital_value, total_assets_value):
    return working_capital_value / total_assets_value


"""
##### Liquidity ratios
- Cash ratio 
- Current ratio 
- NWC to assets 
- Quick ratio
"""
""" liquidity """


def cash_ratio(cash, marketable_securities, current_liabilities):
    return (cash + marketable_securities) / current_liabilities


def cash_flow_from_operating_activities_ratio(cash_flow_from_operating_activities, average_current_liabilities):
    return cash_flow_from_operating_activities / average_current_liabilities


def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities


def interval_measure(cash, marketable_securities, receivables, average_daily_expenditures_from_operation):
    return (cash + marketable_securities + receivables) / average_daily_expenditures_from_operation


def net_working_capital_to_total_assets_ratio(net_working_capital, total_assets):
    return net_working_capital / total_assets


def quick_or_acid_test_ratio(cash, marketable_securities, receivables, current_liabilities):
    return (cash + marketable_securities + receivables) / current_liabilities


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


def payables_conversion_period(accounts_payable, purchases_value, number_of_days_in_year=365):
    return (accounts_payable / purchases_value) * number_of_days_in_year


def purchases(cost_of_goods_sold, change_in_inventory):
    return cost_of_goods_sold + change_in_inventory


def payables_days(purchase_amount, average_accounts_payable, number_of_days_in_year=365):
    return number_of_days_in_year / payables_turnover(purchase_amount, average_accounts_payable)


def payables_turnover(purchase_amount, average_accounts_payable):
    return purchase_amount / average_accounts_payable


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