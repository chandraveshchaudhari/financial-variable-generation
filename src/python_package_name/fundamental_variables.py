










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


""" liquidity """


def calc_cash_ratio(cash, marketable_securities, current_liabilities):
    return (cash + marketable_securities) / current_liabilities


def calc_current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities


def calc_operating_cash_flow_ratio(operating_cash_flow, total_debts):
    return operating_cash_flow / total_debts


def calc_quick_ratio(current_assets, inventories, current_liabilities):
    return (current_assets - inventories) / current_liabilities


""" market """


def calc_dividend_cover(earnings_per_share, dividends_per_share):
    return earnings_per_share / dividends_per_share


def calc_dividends_per_share(dividends_paid, number_of_shares):
    return dividends_paid / number_of_shares


def calc_dividend_yield(annual_dividend_per_share, price_per_share):
    return annual_dividend_per_share / price_per_share


def calc_earnings_per_share(net_earnings, number_of_shares):
    return net_earnings / number_of_shares


def calc_payout_ratio(dividends, earnings):
    return dividends / earnings


def calc_peg_ratio(price_per_earnings, annual_eps_growth):
    return price_per_earnings / annual_eps_growth


def calc_price_sales_ratio(price_per_share, revenue_per_share):
    return price_per_share / revenue_per_share


""" profitability """


def calc_efficiency_ratio(non_interest_expense, revenue):
    return non_interest_expense / revenue


def calc_gross_profit_margin(gross_profit, revenue):
    return gross_profit / revenue


def calc_operating_margin(operating_income, revenue):
    return operating_income / revenue


def calc_profit_margin(net_profit, revenue):
    return net_profit / revenue


def calc_return_on_assets(net_income, total_assets):
    return net_income / total_assets


def calc_return_on_capital(ebit, tax_rate, invested_capital):
    return ebit * (1 - tax_rate) / invested_capital


def calc_return_on_equity(net_income, average_shareholder_equity):
    return net_income / average_shareholder_equity


def calc_return_on_net_assets(net_income, fixed_assets, working_capital):
    return net_income / (fixed_assets + working_capital)


def calc_risk_adjusted_return_on_capital(expected_return, economic_capital):
    return expected_return / economic_capital


def calc_return_on_investment(gain, cost):
    return (gain - cost) / cost


def calc_ebitda(ebit, depreciation, amortization):
    return ebit + depreciation + amortization