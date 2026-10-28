import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("employees.csv")

average=df.groupby("department")["salary"].mean()

bars=plt.bar(average.index,average.values)

plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")

plt.bar_label(bars)
plt.show()
plt.savefig("Average_Sal_Department.png")
plt.close()

plt.hist(df["salary"], bins=5, edgecolor="black")

plt.title("Distribution of Employee Salaries")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")

plt.savefig("salary_histogram.png")
plt.show()
plt.close()

for department,group in df.groupby("department"):
    plt.scatter(group["id"],group["salary"],label=department)

plt.title("Employee ID vs Salary by Department")
plt.xlabel("Employee ID")
plt.ylabel("Salary")
plt.legend(title="Department")
plt.savefig("employee_id_vs_salary.png")
plt.show()

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [12, 15, 14, 18, 22, 25]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.savefig("monthly_sales.png")
plt.show()
