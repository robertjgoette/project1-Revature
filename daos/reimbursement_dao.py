from abc import ABC, abstractmethod
from typing import List

from entities.reimbursements import Reimbursement


class ReimbursementDao(ABC):

    # CRUD Functions
    # CREATE
    @abstractmethod
    def post_reimbursement(self, reimbursement: Reimbursement, employee_id: int) -> Reimbursement:
        pass

    # READ
    @abstractmethod
    def get_all_reimbursement_employee(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_all_reimbursement(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        pass

    # UPDATE
    @abstractmethod
    def put_reimbursement(self, reimbursement: Reimbursement, reviewer_id: int) -> Reimbursement:
        pass

    # DELETE
    # @abstractmethod
    # def delete_reimbursement(self, reimbursement_id: int) -> bool:
    #     pass
    # Reimbursements will be denied but never DELETED]
