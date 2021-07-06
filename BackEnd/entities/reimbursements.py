# Database table of Reimbursement
# create table reimbursement(
#     reimbursement_id int primary key generated always as identity,
#     reimbursement_amount int,
#     reimbursement_state varchar (50) default 'pending',
#     reimbursement_last_day_modified int,
#     reimbursement_message varchar (500),
#     reimbursement_response varchar (500) default null,
#     reviewer_id int default null,
#     employee_id int,
#     constraint fk_reimbursement_employee foreign key (employee_id) references employee(employee_id),
#     constraint fk_reimbursement_reviewer foreign key (reviewer_id) references employee(employee_id)
# );


class Reimbursement:

    def __init__(self, reimbursement_id: int, reimbursement_amount: float, reimbursement_state: str,
                 reimbursement_last_day_modified: int, reimbursement_message: str, reviewer_id: int, employee_id: int,
                 reimbursement_response: str):
        self.reimbursement_id = reimbursement_id
        self.reimbursement_amount = reimbursement_amount
        self.reimbursement_state = reimbursement_state
        self.reimbursement_last_day_modified = reimbursement_last_day_modified
        self.reimbursement_message = reimbursement_message
        self.reviewer_id = reviewer_id
        self.employee_id = employee_id
        self.reimbursement_response = reimbursement_response

    def as_json_dict(self):
        return {"reimbursementId": self.reimbursement_id,
                "reimbursementAmount": self.reimbursement_amount,
                "reimbursementState": self.reimbursement_state,
                "reimbursementLastDayModified": self.reimbursement_last_day_modified,
                "reimbursementMessage": self.reimbursement_message,
                "reimbursementResponse": self.reimbursement_response,
                "reviewerId": self.reviewer_id,
                "employeeId": self.employee_id
                }

    def __str__(self):
        return "reimbursementId(" + str(self.reimbursement_id) + ") reimbursementAmount(" + str(
            self.reimbursement_amount) + ") reimbursementState(" + self.reimbursement_state + ") reimbursementLastDayModified (" + str(
            self.reimbursement_last_day_modified) + ") reimbursementMessage(" + self.reimbursement_message + ") reviewerId(" + str(
            self.reviewer_id) + ") employeeId(" + str(self.employee_id) + ")"
