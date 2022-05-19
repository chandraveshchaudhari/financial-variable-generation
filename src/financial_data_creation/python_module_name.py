"""
Remember to put distinct name of modules and they should not have same name functions and class inside
Try to use absolute import and reduce cyclic imports to avoid errors
if there are more than one modules then import like this:
from python_package_name import sample_func
"""
from python_package_name import second_python_module_name

run_this = second_python_module_name.sample_func("well anything")

if __name__ == '__main__':
    print(run_this)


def convert_to_average_stock_prices(BSE_stockprice, time_column_name='Bmonth_Month End'):
    # remove empty columns
    BSE_stockprice.dropna(how='all', axis=1, inplace=True)
    # find all unique years
    totalyears = len(BSE_stockprice[time_column_name].unique())//12
    yearlist = []
    number = 202103.0
    for i in range(totalyears):
        yearlist.append(number)
        number -= 100
    filtered_numeric_columns =  ['Bmonth_Open', 'Bmonth_High', 'Bmonth_Low', 'Bmonth_Close', "Bmonth_Volume ('000)", 'Bmonth_Value']
    averagestockpricecolumns = []
    for i in filtered_numeric_columns:
        averagestockpricecolumns.append("avg__"+i)

    averagestockpricecolumns = ['Accord Code','Company Name','Bmonth_Month End'] + averagestockpricecolumns
    company_names = list(BSE_stockprice["Company Name"].unique())
    data = []
    columns = averagestockpricecolumns
    for company in company_names:
        for index in range(totalyears-1):
            try:
                filtered = BSE_stockprice.loc[(BSE_stockprice['Company Name'] == company) &
                                  (BSE_stockprice['Bmonth_Month End'] < yearlist[index] )&
                                  (BSE_stockprice['Bmonth_Month End'] >= yearlist[index+1] )]

                values = [filtered['Accord Code'].values[0], company, yearlist[index]]
                for numeric_column in filtered_numeric_columns:
                    values.append(filtered[numeric_column].mean())
                zipped = zip(columns, values)
                a_dictionary = dict(zipped)
                #print(a_dictionary)
                data.append(a_dictionary)
            except:
                print(yearlist[index], yearlist[index+1],"is not there!")

    return pd.DataFrame(data)
