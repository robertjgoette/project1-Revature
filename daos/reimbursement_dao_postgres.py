from daos.reimbursement_dao import ReimbursementDao, Reimbursement
from typing import List
from utils.connection_util import connection
from exceptions.resource_not_found_error import ResourceNotFoundError


class ReimbursementDaoPostgres(ReimbursementDao):
    def post_reimbursement(self, reimbursement: Reimbursement, employee_id: int) -> int:
        print(employee_id)
        sql = """insert into reimbursement values(default, %s, default, %s, %s, default, %s, default);"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.reimbursement_amount, reimbursement.reimbursement_last_day_modified,
                             reimbursement.reimbursement_message, employee_id))
        connection.commit()
        reimbursement_id = employee_id  # cursor.fetchone()
        reimbursement.reimbursement_id = reimbursement_id
        return reimbursement_id

    def get_all_reimbursement_employee(self, employee_id: int) -> List[Reimbursement]:
        # try:
        sql = """select * from reimbursement where employee_id = %s;"""
        cursor = connection.cursor()
        cursor.execute(sql % (employee_id))
        reimbursements = cursor.fetchall()
        reimbursement_list = []
        for reimbursement in reimbursements:
            reimbursement_list.append(Reimbursement(*reimbursement))
        return reimbursement_list

    # except Exception:
    #     raise ResourceNotFoundError(f"No reimbursement found.")

    def get_all_reimbursement(self) -> List[Reimbursement]:
        try:
            sql = """select * from reimbursement"""
            cursor = connection.cursor()
            cursor.execute(sql)
            reimbursements = cursor.fetchall()
            reimbursement_list = []
            for reimbursement in reimbursements:
                reimbursement_list.append(Reimbursement(*reimbursement))
            return reimbursement_list
        except Exception:
            raise ResourceNotFoundError(f"No reimbursement found... Something really bad has happened")

    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        try:
            sql = """select * from reimbursement where reimbursement_id = %s;"""
            cursor = connection.cursor()
            cursor.execute(sql % reimbursement_id)
            reimbursements = cursor.fetchone()
            reimbursement = Reimbursement(*reimbursements)
            return reimbursement
        except Exception:
            raise ResourceNotFoundError(f"No reimbursement found... Something really bad has happened")

    def put_reimbursement(self, reimbursement: Reimbursement, reviewer_id: int) -> Reimbursement:
        try:
            reviewer_id = reviewer_id
            sql = """update reimbursement set reimbursement_state = %s, reviewer_id = %s, reimbursement_last_day_modified= %s,  reimbursement_response = %s where reimbursement_id = %s;"""
            cursor = connection.cursor()
            cursor.execute(sql, (reimbursement.reimbursement_state, reviewer_id,
                                 reimbursement.reimbursement_last_day_modified, reimbursement.reimbursement_response,
                                 reimbursement.reimbursement_id))
            connection.commit()
            return reimbursement
        except Exception:
            raise ResourceNotFoundError(f"Reimbursement not found")
