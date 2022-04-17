"""
## List of variables
some code is borrowed from https://github.com/srbrettle/Financial-Formulas
### Financial Ratios
- Number of shares outstanding
"""
"""
##### Leverage ratios
- Long term debt ratio
- Debt-equity ratio 
- Total debt ratio 
- Interest Coverage Formula 
- Times interest earned 
- Cash coverage ratio 
- asset liability ratio
- Total debt to total assets
- Financial Leverage formula
- operating Leverage formula
- Cash debt coverage ratio
- Operating cash flow to liabilities ratio
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


"""
##### Liquidity ratios
- NWC to assets 
- Current ratio 
- Quick ratio
- Cash ratio 
"""

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


def asset_turnover_ratio_formula(net_sales, total_assets):
    return net_sales / total_assets


def average_collection_period(accounts_receivable, annual_credit_sales):
    return accounts_receivable / (annual_credit_sales / 365)


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


def inventory_turnover(sales, average_inventory):
    return sales / average_inventory


def payables_conversion_period(accounts_payable, purchases):
    return (accounts_payable / purchases) * 365


def receivables_conversion_period(receivables, net_sales):
    return (receivables / net_sales) * 365


def receivables_turnover_ratio(net_credit_sales, average_net_receivables):
    return net_credit_sales / average_net_receivables



"""
##### Profitability ratios
- Net profit margin
- Return on assets (ROA)
- Operating Profit Margin 
- ROE or Return on Equity Formula 
- Return on Capital Employed (ROCE) 
- Return on sales
- Dividends payout ratio 
- Plowback ratio 
- Growth in equity from plowback 
- Price- Earnings ratio 
- price to sales ratio (P/S)
- Earnings per share (EPS)
- price to book ratio (P/B)
- Sales/Total Assest
- Net cash flow of investing activities per share 
- Research & Development Expense to Sales 
- Pre taxes income/Sales 
- EBITDA Margin Ratio
- Sales revenue growth rate 
- Gross profit margin 
- Shareholder equity growth rate
- Main business income growth
- Return on net assets
"""