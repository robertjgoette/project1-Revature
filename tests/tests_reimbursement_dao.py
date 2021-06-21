from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao import Reimbursement
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres

reimbursementDao: ReimbursementDao = ReimbursementDaoPostgres()

test_reimbursement = Reimbursement(46, 800, 'pending', 1623295408, 'I want this.', 0, 1, '')


def test_post_reimbursement():
    reimbursementDao.post_reimbursement(test_reimbursement, test_reimbursement.employee_id)
    assert test_reimbursement.reimbursement_id != 0
    # Tests to see if item was saved to database by checking if it has a id


def test_get_all_reimbursement_employee():
    reimbursement = reimbursementDao.get_all_reimbursement_employee(1)
    assert len(reimbursement) >= 2
    # Tests to see how many items were returned to make sure a list was returned


def test_get_all_reimbursement():
    reimbursement = reimbursementDao.get_all_reimbursement()
    assert len(reimbursement) >= 2
    # Tests to see how many items were returned to make sure a list was returned


def test_get_reimbursement():
    reimbursement = reimbursementDao.get_reimbursement(1)
    assert reimbursement.reimbursement_id == 1
    # Checks to see if it gets back the right reimbursement_id


def test_put_reimbursement():
    test_reimbursement.reimbursement_state = "denied"
    test_reimbursement.reimbursement_id = 46
    reviewer_id = 2
    reimbursement = reimbursementDao.put_reimbursement(test_reimbursement, reviewer_id)
    assert reimbursement.reimbursement_state == "denied"
