from typing import List
from daos.reimbursement_dao import ReimbursementDao
from services.reimbursement_services import ReimbursementServices, Reimbursement
from exceptions.resource_not_found_error import ResourceNotFoundError


class ReimbursementServicesImpl(ReimbursementServices):

    def __init__(self, reimbursement_dao: ReimbursementDao):
        self.reimbursement_dao = reimbursement_dao

    def post_reimbursement(self, reimbursement: Reimbursement, employee_id: int) -> Reimbursement:
        print(employee_id)
        return self.reimbursement_dao.post_reimbursement(reimbursement, employee_id)

    def get_all_reimbursement_employee(self, employee_id: int) -> List[Reimbursement]:
        try:
            return self.reimbursement_dao.get_all_reimbursement_employee(employee_id)
        except Exception:
            raise ResourceNotFoundError(f"No reimbursements found.")

    def get_all_reimbursement(self) -> List[Reimbursement]:
        try:
            return self.reimbursement_dao.get_all_reimbursement()
        except Exception:
            raise ResourceNotFoundError(f"No reimbursements found.")

    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        try:
            return self.reimbursement_dao.get_reimbursement(reimbursement_id)
        except Exception:
            raise ResourceNotFoundError(f"No reimbursement found.")

    def put_reimbursement(self, reimbursement: Reimbursement, reviewer_id: int) -> Reimbursement:
        try:
            return self.reimbursement_dao.put_reimbursement(reimbursement, reviewer_id)
        except Exception:
            raise ResourceNotFoundError(f"No reimbursement found.")
