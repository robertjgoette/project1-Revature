class Stats:

    def __init__(self, employee_id1: int, employee_first_name: str, employee_last_name: str, employee_email: str,
                 employee_user_name: str, employee_password: str, employee_is_manager: bool, reimbursement_id: int,
                 reimbursement_amount: float, reimbursement_state: str,
                 reimbursement_last_day_modified: int, reimbursement_message: str, reviewer_id: int,
                 employee_id2: int):
        self.employee_id1 = employee_id1
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.employee_email = employee_email
        self.employee_user_name = employee_user_name
        self.employee_password = employee_password
        self.employee_is_manager = employee_is_manager
        self.reimbursement_id = reimbursement_id
        self.reimbursement_amount = reimbursement_amount
        self.reimbursement_state = reimbursement_state
        self.reimbursement_last_day_modified = reimbursement_last_day_modified
        self.reimbursement_message = reimbursement_message
        self.reviewer_id = reviewer_id
        self.employee_id2 = employee_id2

    def as_json_dict(self):
        return {"employeeId1": self.employee_id1,
                "employeeFirstName": self.employee_first_name,
                "employeeLastName": self.employee_last_name,
                "employeeEmail": self.employee_email,
                "employeeUserName": self.employee_user_name,
                "employeePassword": self.employee_password,
                "employeeIsManager": self.employee_is_manager,
                "reimbursementId": self.reimbursement_id,
                "reimbursementAmount": self.reimbursement_amount,
                "reimbursementState": self.reimbursement_state,
                "reimbursementLastDayModified": self.reimbursement_last_day_modified,
                "reimbursementMessage": self.reimbursement_message,
                "reviewerId": self.reviewer_id,
                "employeeId2": self.employee_id2
                }
