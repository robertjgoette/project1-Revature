from typing import List, Dict
from daos.employees_dao import EmployeeDao, Employee
from daos.reimbursement_dao import ReimbursementDao
from entities.reimbursements import Reimbursement
from exceptions.resource_not_found_error import ResourceNotFoundError
from services.employees_services import EmployeesServices
from services.reimbursement_services import ReimbursementServices


class EmployeesServicesImpl(EmployeesServices, ReimbursementServices):

    def __init__(self, employee_dao: EmployeeDao, reimbursement_dao: ReimbursementDao):
        self.employee_dao = employee_dao
        self.reimbursement_dao = reimbursement_dao

    def get_all_employee(self) -> List[Employee]:
        return self.employee_dao.get_all_employee()

    def get_employee(self, employee_id: int) -> Employee:
        try:
            return self.employee_dao.get_employee(employee_id)
        except Exception:
            raise ResourceNotFoundError(f"Employee with ID {employee_id} not found")

    def login_employee(self, username: str, password: str) -> Dict:
        employees = self.employee_dao.get_all_employee()
        for employee in employees:
            if employee.employee_user_name == username and employee.employee_password == password:
                employee_dict = {"employeeID": employee.employee_id, "employeeIsManager": employee.employee_is_manager}
                return employee_dict
        return {"employeeID": 0, "employeeIsManager": False}

    # Should this also return ones with with no amount requested?
    def stat_employee(self) -> dict[str, float]:
        employee_list = self.employee_dao.get_all_employee()
        amount_spent = {}
        for s in employee_list:
            amount: float = 0.0
            current_id: int = 0
            reimbursement_list = self.reimbursement_dao.get_all_reimbursement_employee(s.employee_id)
            for a in reimbursement_list:
                if a.reimbursement_state == 'approved' and s.employee_id == a.employee_id:
                    amount += a.reimbursement_amount
                current_id = a.employee_id
                if s.employee_id == a.employee_id:
                    amount_spent.update({str(current_id): amount})
        return amount_spent

    def post_reimbursement(self, reimbursement: Reimbursement, employee_id: int) -> Reimbursement:
        return self.reimbursement_dao.post_reimbursement(reimbursement, employee_id)

    def get_all_reimbursement_employee(self, employee_id: int) -> List[Reimbursement]:
        # try:
        return self.get_all_reimbursement_employee(employee_id)

    # except Exception:
    #     raise ResourceNotFoundError(f"No reimbursements found.")

    def get_all_reimbursement(self) -> List[Reimbursement]:
        try:
            return self.get_all_reimbursement()
        except Exception:
            raise ResourceNotFoundError(f"No reimbursements found.")

    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        try:
            return self.get_reimbursement(reimbursement_id)
        except Exception:
            raise ResourceNotFoundError(f"No reimbursement found.")

    def put_reimbursement(self, reimbursement: Reimbursement, reviewer_id: int) -> Reimbursement:
        try:
            return self.put_reimbursement(reimbursement, reviewer_id)
        except Exception:
            raise ResourceNotFoundError(f"No reimbursement found.")