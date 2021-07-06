from abc import ABC, abstractmethod
from typing import List
from entities.employees import Employee


class EmployeesServices(ABC):
    # READ
    @abstractmethod
    def get_all_employee(self) -> List[Employee]:
        pass

    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def login_employee(self, username: str, password: str) -> int:
        pass

    @abstractmethod
    def stat_employee(self) -> dict[str, float]:
        pass
