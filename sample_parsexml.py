import xml.etree.cElementTree as et 

tree = et.parse("sample.xml")

root = tree.getroot()
job_title = []
Company_name = []
City = []
Category = []

for title in root.iter('job_title'):
    job_title.append(title.text)

for company in root.iter('company_name'):
    Company_name.append(company.text)

for category in root.iter('category'):
    Category.append(category.text)

for city in root.iter('city'):
    City.append(city.text)    

print("Job Title:", job_title)
print("Company Name:", Company_name)
print("Category:", Category)
print("City:", City)