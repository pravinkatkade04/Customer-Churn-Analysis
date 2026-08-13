import matplotlib.pyplot as plt
import pandas as pd
import Customer_RawData_Visualization as c

df = pd.read_csv("Customer_Churn_Cleaned.csv")
print(df.info())

#Overall Chur Data
type_counts = df["Churn"].value_counts()
plt.figure(figsize=(5,6))
plt.bar(type_counts.index , type_counts.values , color = [ "blue" , "red"])
plt.title("Customber Churns ")
plt.xlabel("Type")
plt.ylabel("number of Customer")
plt.tight_layout()
plt.savefig("ChurnColumn.png")
plt.show()



df["MonthlyCharges"] = df["MonthlyCharges"].astype(int)
mon = df["MonthlyCharges"].value_counts().sort_index()
plt.figure(figsize=(6,6))

plt.hist(df["MonthlyCharges"], bins=5 , color= "gray" , edgecolor = "red")
plt.grid(color = "Yellow")
plt.title("Monthly Charges vs Number of Customers")
plt.xlabel("Monthly Charges")
plt.ylabel("Number of Customers")
plt.legend()
plt.tight_layout()
plt.savefig("MonthlyCharges.png")
plt.show()


#Gender
gen= df["Gender"].value_counts()

plt.pie(gen ,labels=gen.index , autopct="%1.1f%%" , startangle=90)
plt.grid()
plt.title("Gender of Customers")
plt.legend()
plt.tight_layout()
plt.savefig("Gender_Chart.png")
plt.show()


age = df["Age"].value_counts()
plt.figure(figsize=(8,6))
plt.bar(age.index , age.values , color = "purple")
plt.grid()
plt.title("Age Of Employee")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.legend()
plt.savefig("Custmers_AGE.png")
plt.show()

payment = df["PaymentMethod"].value_counts()
plt.barh(payment.index , payment.values , color = "pink" )
plt.xlabel("Number Of Customers")
plt.ylabel("Payment Methods")
plt.tight_layout()
plt.legend("Payment Method")
plt.savefig("Payment_Method.png")
plt.show()


#Totalcharges 

plt.hist(df["TotalCharges"], bins=20, color="brown", edgecolor="black")
#plt.figure(figsize=(6,6))
plt.xlabel("Charges")
plt.ylabel("Numbers of Customers")
plt.tight_layout()
plt.savefig("Total_charges.png")
plt.show()


#contract
contract = df["Contract"].value_counts()
plt.pie(contract , labels= contract.index , autopct= "%1.1f%%" , startangle=90)
plt.title("Contract's Of Customers")

plt.tight_layout()
plt.savefig("Contract.png")
plt.show()

c.Relate_table_contract["Yes"].plot(kind="bar")
plt.title("Contract Relation With Churn ")
plt.xlabel("Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.savefig("Relation_Contract_Churn")
plt.show()



c.Relate_table["Yes"].plot(kind="bar",color="red")
plt.title("Gender Relation With Churn")
plt.xlabel("Type Of Gender")
plt.ylabel("Churn Rate(%)")
plt.xticks(rotation=0)
plt.grid(color="gray")
plt.tight_layout()
plt.savefig("Relation_Gender_Churn.png")
plt.show()
