# app.py
import streamlit as st
from employee import PartTimeEmployee, FullTimeEmployee

# Load the CSS style
st.markdown('<style>{}</style>'.format(open('style.css').read()), unsafe_allow_html=True)

# Function to handle employee creation
def create_employee():
    # Input fields for Employee Information
    firstname = st.text_input("First Name")
    secondname = st.text_input("Second Name")
    employee_type = st.selectbox("Select Employee Type", ["", "Part-Time", "Full-Time"])

    # Pay input field based on employee type
    pay = None
    if employee_type:
        if employee_type == "Part-Time":
            pay = st.number_input("Enter Weekly Pay", min_value=0)
        elif employee_type == "Full-Time":
            pay = st.number_input("Enter Monthly Pay", min_value=0)

    # Address input fields
    street_number = st.number_input("Street Number", min_value=1)
    street_name = st.text_input("Street Name")
    state_code = st.text_input("State Code")
    state_name = st.text_input("State Name")

    # Button to create employee
    if st.button("Create Employee"):
        if firstname and secondname and employee_type and pay and street_number and street_name and state_code and state_name:
            if employee_type == "Part-Time":
                employee = PartTimeEmployee(firstname, secondname, pay, street_number, street_name, state_code, state_name)
            else:
                employee = FullTimeEmployee(firstname, secondname, pay, street_number, street_name, state_code, state_name)
            
            employee_details = employee.get_employee_details()
            st.success("Employee Created Successfully!")
            st.write(employee_details)
        else:
            st.error("Please fill in all fields.")

def main():
    st.title("Employee Information Management System")
    create_employee()

if __name__ == "__main__":
    main()
