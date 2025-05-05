# Data Values
purchasing_price = 25000000 #IDR
residual_value = 2000000 #IDR 

annual_Depreciation = (purchasing_price - residual_value) / 5
depreciation_over_2_years = annual_Depreciation * 2
remaining_asset_value = purchasing_price - depreciation_over_2_years
print(remaining_asset_value)