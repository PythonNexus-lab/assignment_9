import pandas as pd

# load the excel file
df = pd.read_excel("sample-case.xlsx")

# show original data
print("=== ORIGINAL dATA ===")
print(df)

# Example changes
# update Abu Bakr's score to 95
df.loc[df['Nama Mahasiswa'] == 'ABU BAKR E CEESAY', 'Score'] = 95

#add a new student
new_student = {
    'No': len(df) + 1,
    'NIM': 2024010001,
    'Nama Mahasiswa': 'Omar Jammeh',
    'Score': 88
}
df = pd.concat([df, pd.DataFrame([new_student])], ignore_index=True)

# Show updated data
print("\n=== UPDATED DATA ===")
print(df)

# Save to new Excel file
df.to_excel("updated_sample-case.xlsx", index=False)
