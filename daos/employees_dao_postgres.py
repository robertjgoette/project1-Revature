from entities.stats import Stats
from daos.employees_dao import EmployeeDao, Employee
from typing import List
from utils.connection_util import connection
from exceptions.resource_not_found_error import ResourceNotFoundError


class EmployeeDaoPostgres(EmployeeDao):

    def get_all_employee(self) -> List[Employee]:
        try:
            sql = """select * from employee"""
            cursor = connection.cursor()
            cursor.execute(sql)
            employees = cursor.fetchall()
            employee_list = []
            for employee in employees:
                employee_list.append(Employee(*employee))
            return employee_list
        except Exception:
            raise ResourceNotFoundError(f"No employees found... Something really bad has happened")

    def get_employee(self, employee_id: int) -> Employee:
        try:
            sql = """select * from employee where employee_id = %s"""
            cursor = connection.cursor()
            cursor.execute(sql, [employee_id])
            record = cursor.fetchone()
            employee = Employee(*record)
            return employee
        except Exception:
            raise ResourceNotFoundError(f"No employee with ID {employee_id}")
