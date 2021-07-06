from unittest.mock import MagicMock
from daos.employees_dao_postgres import EmployeeDaoPostgres
from entities.employees import Employee
from entities.reimbursements import Reimbursement
from entities.stats import Stats
from services.employees_services import EmployeesServices
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres
from services.employees_services_impl import EmployeesServicesImpl

employees = [
    Employee(1, 'John', 'Smith', 'johnsmith@email.com', 'TheJohnGuy', 'MyPassword', False),
    Employee(2, 'John', 'Smith', 'johnsmith@email.com', 'TheJohnGuy2', 'MyPassword2', False),
    Employee(3, 'John', 'Smith', 'johnsmith@email.com', 'TheJohnGuy3', 'MyPassword3', False),
    Employee(4, 'John', 'Smith', 'johnsmith@email.com', 'TheJohnGuy4', 'MyPassword4', False),
    Employee(5, 'John', 'Smith', 'johnsmith@email.com', 'TheJohnGuy5', 'MyPassword5', False)
]
reimbursement = [
    Reimbursement(1, 200, 'approved', 1623195408, 'I need this.', 0, 1, "yes"),
    Reimbursement(2, 200, 'pending', 1623195408, 'I need this.',  0, 1, "yes"),
    Reimbursement(3, 200, 'approved', 1623195408, 'I need this.',  0, 1, "yes"),
    Reimbursement(4, 200, 'pending', 1623195408, 'I need this.', 0, 1, "yes"),
    Reimbursement(5, 200, 'approved', 1623195408, 'I need this.', 0, 2, "yes")
]

mock_dao_e = EmployeeDaoPostgres()
mock_dao_r = ReimbursementDaoPostgres()
mock_dao_e.get_all_employee = MagicMock(return_value=employees)
mock_dao_r.get_all_reimbursement_employee = MagicMock(return_value=reimbursement)
employees = mock_dao_e.get_all_employee(0)

employees_services: EmployeesServices = EmployeesServicesImpl(mock_dao_e, mock_dao_r)


def test_login_employee_0():
    result = employees_services.login_employee("TheJohnGuy", "MyPassword")
    assert result["employeeID"] == 1


def test_login_employee_1():
    result = employees_services.login_employee("TheJohnGuy2", "MyPassword2")
    assert result["employeeID"] == 2


def test_login_employee_2():
    result = employees_services.login_employee("TheJohnGuy6", "MyPassword6")
    assert result["employeeID"] == 0


def test_stat_employee_0():
    result = employees_services.stat_employee()
    print(result)
    assert len(result) == 2
