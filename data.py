import pandas as pd

# اسم الملف
file_name = "id1.xls"

# قراءة الملف
data = pd.read_excel(file_name)

# الرقم الوظيفي المطلوب البحث عنه
job_number = int(input("id: "))

# البحث عن السطر الذي يحتوي الرقم الوظيفي
row = data.loc[data['رقم الموظف'] == job_number]

# التحقق مما إذا كان هناك سطر مطابق
if len(row) > 0:
    # استخراج اسم الموظف
    employee_name = row['حالة العهدة'].values[0]
    print(f" {employee_name}")
else:
    print("Nothing.")
