from daos.employees_dao import EmployeeDao, Employee
from daos.employees_dao_postgres import EmployeeDaoPostgres

employeesDao: EmployeeDao = EmployeeDaoPostgres()

test_employee = Employee(0, 'John', 'Smith', 'johnsmith@email.com', 'TheJohnGuy', 'MyPassword', False)


# def test_stat_employee():
#     employees = employeesDao.stat_employee(1)
#     assert len(employees) >= 1


def test_get_all_employee():
    employees = employeesDao.get_all_employee()
    assert len(employees) >= 1


def test_get_employee():
    employees = employeesDao.get_employee(1)
    assert employees.employee_id == 1
