# Database table of Employee
# create table employee(
#     employee_id int primary key generated always as identity,
#     employee_first_name varchar(50),
#     employee_last_name varchar(50),
#     employee_email varchar(50),
#     employee_user_name varchar(50),
#     employee_password varchar(50),
#     employee_is_manager boolean default false
# );


class Employee:

    def __init__(self, employee_id: int, employee_first_name: str, employee_last_name: str, employee_email: str,
                 employee_user_name: str, employee_password: str, employee_is_manager: bool):
        self.employee_id = employee_id
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.employee_email = employee_email
        self.employee_user_name = employee_user_name
        self.employee_password = employee_password
        self.employee_is_manager = employee_is_manager

    def as_json_dict(self):
        return {"employeeId": self.employee_id,
                "employeeFirstName": self.employee_first_name,
                "employeeLastName": self.employee_last_name,
                "employeeEmail": self.employee_email,
                "employeeUserName": self.employee_user_name,
                "employeePassword": self.employee_password,
                "employeeIsManager": self.employee_is_manager
                }

    def __str__(self):
        return "employeeId: " + str(
            self.employee_id) + " employeeFirstName: " + self.employee_first_name + " employeeLastName: " + self.employee_last_name + " employeeEmail" + self.employee_email + " employeeUserName: " + self.employee_user_name + " employeePassword: " + self.employee_password + " employeeIsManager :" + str(
            self.employee_is_manager)
