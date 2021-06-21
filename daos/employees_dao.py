from abc import ABC, abstractmethod
from typing import List

from entities.employees import Employee


class EmployeeDao(ABC):

    # CRUD Functions
    # CREATE
    # @abstractmethod
    # def post_employee(self, employee: Employee) -> Employee:
    #     pass

    # READ
    @abstractmethod
    def get_all_employee(self) -> List[Employee]:
        pass

    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        pass

    # @abstractmethod
    # def stat_employee(self, employee_id: int):
    #     pass

    # UPDATE
    # @abstractmethod
    # def put_employee(self, employee: Employee, employee_id: int) -> Employee:
    #     pass

    # DELETE
    # @abstractmethod
    # def employee_account(self, employee_id: int) -> bool:
    #     pass
