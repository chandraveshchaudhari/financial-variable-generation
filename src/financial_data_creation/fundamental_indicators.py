"""
## List of variables
some code is borrowed from https://github.com/srbrettle/Financial-Formulas

#### Primitive formulas

"""


def calc_ebitda(ebit, depreciation, amortization):
    return ebit + depreciation + amortization


def calc_assets(liabilities, shareholders_equity):
    return liabilities + shareholders_equity


def calc_ebit(revenue, operating_expenses):
    return revenue - operating_expenses


def calc_shareholders_equity(assets, liabilities):
    return assets - liabilities


def calc_gross_profit(revenue, cost_of_goods_sold):
    return revenue - cost_of_goods_sold


def calc_liabilities(assets, shareholders_equity):
    return assets - shareholders_equity


def calc_net_profit(gross_profit, operating_expenses, taxes, interest):
    return gross_profit - operating_expenses - taxes - interest


def calc_operating_profit(gross_profit, operating_expenses):
    return gross_profit - operating_expenses


def calc_sales_revenue(gross_sales, sales_of_returns_and_allowances):
    return gross_sales - sales_of_returns_and_allowances


""" depreciation """


def calc_book_value(acquisition_cost, depreciation):
    return acquisition_cost - depreciation


def calc_declining_balance(depreciation_rate, book_value_at_beginning_of_year):
    return depreciation_rate * book_value_at_beginning_of_year


def calc_units_of_production(
        cost_of_asset,
        residual_value,
        estimated_total_production,
        actual_production):
    return ((cost_of_asset - residual_value) /
            estimated_total_production) * actual_production


def calc_straight_line_method(
        cost_of_fixed_asset,
        residual_value,
        useful_life_of_asset):
    return (cost_of_fixed_asset - residual_value) / useful_life_of_asset


# market


def calc_dividend_cover(earnings_per_share, dividends_per_share):
    return earnings_per_share / dividends_per_share


def calc_dividends_per_share(dividends_paid, number_of_shares):
    return dividends_paid / number_of_shares


def calc_dividend_yield(annual_dividend_per_share, price_per_share):
    return annual_dividend_per_share / price_per_share


def calc_earnings_per_share(net_earnings, number_of_shares):
    return net_earnings / number_of_shares



def dividends_payout_ratio(dividends, earnings):
    return dividends / earnings


def plowback_ratio(dividends, earnings):
    return 1 - dividends_payout_ratio(dividends, earnings)


"""

### Financial Ratios
- Number of shares outstanding
"""
"""
##### Leverage ratios
- Long term debt ratio ++++
- Debt-equity ratio ++++
- Total debt ratio ++++
- Times interest earned +++++
- Cash coverage ratio +++++
- Interest Coverage Formula 
- asset liability ratio
- Total debt to total assets
- Financial Leverage formula
- operating Leverage formula
- Cash debt coverage ratio
- Operating cash flow to liabilities ratio ++++
- Operating cash flow to net profit ratio
- Operating cash net flow to sales revenue ratio
- Operating cash flow to current liabilities ratio
- Equity/Fixed assets 
- Ratio of long-term funds to fixed assets 
- Working capital to total assets
- Capital Expenditures/total assets 
- Operating Income to Total assets 
- Asset growth rate 
- Ratio of long-term liabilities and shareholders' equity 
- Market value equity/total debt 
- Shareholder equity ratio
"""


""" debt """


def long_term_debt_ratio(long_term_debt, shareholders_equity):
    return long_term_debt / (long_term_debt + shareholders_equity)


def long_term_debt_equity_ratio(long_term_liabilities, shareholders_equity):
    return long_term_liabilities / shareholders_equity


def debt_equity_ratio(long_term_debt, shareholders_equity):
    return long_term_debt / shareholders_equity

def total_debt_ratio():
    return total_liabilities / total_assets


def debt_ratio(total_liabilities, total_assets):
    return total_liabilities / total_assets


def debt_service_coverage_ratio(net_operating_income, total_debt_service):
    return net_operating_income / total_debt_service

def times_interest_earned(EBIT, interest_payments):
    return EBIT, interest_payments

def cash_coverage_ratio(EBIT, depriciation, interest_payments):
    return (EBIT + depriciation)/ interest_payments




def operating_cash_flow_ratio(operating_cash_flow, total_debts):
    return operating_cash_flow / total_debts
"""
##### Liquidity ratios
- NWC to assets 
- Current ratio ++++
- Quick ratio ++++
- Cash ratio ++++
"""
""" liquidity """


def net_working_capital_to_total_assets_ratio(net_working_capital, total_assets):
    return net_working_capital/ total_assets


def cash_ratio(cash, marketable_securities, current_liabilities):
    return (cash + marketable_securities) / current_liabilities


def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities


def quick_or_acid_test_ratio(cash, marketable_securities, receivables, current_liabilities):
    return (cash + marketable_securities + receivables) / current_liabilities


def interval_measure(cash, marketable_securities, receivables, average_daily_expenditures_from_operation):
    return (cash + marketable_securities + receivables) / average_daily_expenditures_from_operation



"""
##### Efficiency ratios
- Asset Turnover ratio Formula +++++
- Equity Turnover Ratio Formula 
- Total asset turnover 
- Average collection period +++++
- Inventory turnover +++++
- Days' sales in inventories 
- Inventory Days Formula 
- Accounts Receivables Turnover +++++
- Accounts Receivables Days Formula 
- payables Turnover 
- payables Days 
- Net asset growth rate
- Days sales outstanding
- Inventory to total assets 
- Sales to total cash 
- Sales to total Inventory 
- Sales to total working capital or Working capital turnover 
- Sales to Fixed assets 
- Current asset turnover ratio 
- Growth rate of total assets
- Fixed asset turnover
"""


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




def cash_conversion_cycle(
        inventory_conversion_period,
        receivables_conversion_period,
        payables_conversion_period):
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


def receivables_conversion_period(receivables, net_sales):
    return (receivables / net_sales) * 365


def receivables_turnover_ratio(net_credit_sales, average_net_receivables):
    return net_credit_sales / average_net_receivables


"""
##### Profitability ratios

- Net profit margin ++++ 
- Return on assets (ROA) ++++
- Operating Profit Margin ++++
- ROE or Return on Equity Formula ++++
- Return on Capital Employed (ROCE) +++++
- Return on sales
- Dividends payout ratio ++++
- Plowback ratio 
- Growth in equity from plowback 
- Price- Earnings ratio ++++
- price to sales ratio (P/S) ++++
- Earnings per share (EPS)
- price to book ratio (P/B)
- Sales/Total Assest
- Net cash flow of investing activities per share 
- Research & Development Expense to Sales 
- Pre taxes income/Sales 
- EBITDA Margin Ratio
- Sales revenue growth rate 
- Gross profit margin ++++ 
- Shareholder equity growth rate
- Main business income growth
- Return on net assets ++++
"""

""" profitability """


def net_profit_margin(net_income, sales):
    return net_income / sales


def calc_gross_profit_margin(gross_profit, revenue):
    return gross_profit / revenue


def calc_operating_margin(operating_income, revenue):
    return operating_income / revenue


def calc_profit_margin(net_profit, revenue):
    return net_profit / revenue


def return_on_assets(net_income, interest, interest_tax_shields, average_total_assets):
    return (net_income + interest - interest_tax_shields) / average_total_assets


def calc_return_on_capital(ebit, tax_rate, invested_capital):
    return ebit * (1 - tax_rate) / invested_capital


def return_on_equity(net_income, average_shareholders_equity):
    return net_income / average_shareholders_equity


def calc_return_on_net_assets(net_income, fixed_assets, working_capital):
    return net_income / (fixed_assets + working_capital)


def calc_risk_adjusted_return_on_capital(expected_return, economic_capital):
    return expected_return / economic_capital


def calc_return_on_investment(gain, cost):
    return (gain - cost) / cost


""" market """


def calc_peg_ratio(price_per_earnings, annual_eps_growth):
    return price_per_earnings / annual_eps_growth


def calc_price_sales_ratio(price_per_share, revenue_per_share):
    return price_per_share / revenue_per_share
