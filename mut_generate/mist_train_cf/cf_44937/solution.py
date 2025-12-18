"""
QUESTION:
寫一個名為 `find_highest_avg_revenue` 的 Python 函數，該函數接受一個 JSON 物件作為參數，該物件包含一個名為 `companies` 的屬性。該屬性是一個包含多個公司信息的列表，每個公司信息是一個物件，包含 `name`、`revenue` 和 `years_in_business` 等屬性。函數應該返回平均營業額最高的公司名稱。注意：公司的營業額和年份可能為負數或非數值型態，函數應該能夠處理這些情況，確保年份不為零且平均營業額為正值。
"""

def find_highest_avg_revenue(data):
    companies = data.get('companies', [])
    highest_avg_revenue = float('-inf')
    highest_avg_revenue_company = ''

    for company in companies:
        revenue = company.get('revenue')
        years_in_business = company.get('years_in_business')

        # Ensure revenue and years_in_business are numbers and years_in_business is not zero
        if isinstance(revenue, (int, float)) and isinstance(years_in_business, (int, float)) and years_in_business != 0:
            avg_revenue = revenue / years_in_business

            # Ensure average revenue is positive
            if avg_revenue > 0 and avg_revenue > highest_avg_revenue:
                highest_avg_revenue = avg_revenue
                highest_avg_revenue_company = company.get('name')

    return highest_avg_revenue_company