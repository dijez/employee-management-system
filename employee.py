# employee.py

class Employee:
    def __init__(self, firstname, secondname, employee_type, pay, street_number, street_name, state_code, state_name):
        self.firstname = firstname
        self.secondname = secondname
        self.employee_type = employee_type
        self.pay = pay
        self.street_number = street_number
        self.street_name = street_name
        self.state_code = state_code
        self.state_name = state_name

    def get_employee_details(self):
        pay_type = "Weekly Pay" if self.employee_type == "Part-Time" else "Monthly Pay"
        return {
            "First Name": self.firstname,
            "Second Name": self.secondname,
            "Employee Type": self.employee_type,
            pay_type: f"${self.pay}",
            "Address": f"{self.street_number} {self.street_name}, {self.state_code} {self.state_name}"
        }

class PartTimeEmployee(Employee):
    def __init__(self, firstname, secondname, pay, street_number, street_name, state_code, state_name):
        super().__init__(firstname, secondname, "Part-Time", pay, street_number, street_name, state_code, state_name)

class FullTimeEmployee(Employee):
    def __init__(self, firstname, secondname, pay, street_number, street_name, state_code, state_name):
        super().__init__(firstname, secondname, "Full-Time", pay, street_number, street_name, state_code, state_name)
