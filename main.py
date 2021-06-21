from typing import List

from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from daos.employees_dao_postgres import EmployeeDaoPostgres
from daos.reimbursement_dao_postgres import ReimbursementDaoPostgres
from exceptions.resource_not_found_error import ResourceNotFoundError
from services.employees_services_impl import EmployeesServicesImpl
from services.reimbursement_services_impl import ReimbursementServicesImpl, Reimbursement

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')
app: Flask = Flask(__name__)
CORS(app)

employees_dao = EmployeeDaoPostgres()
reimbursement_dao = ReimbursementDaoPostgres()
employees_service = EmployeesServicesImpl(employees_dao, reimbursement_dao)
reimbursement_service = ReimbursementServicesImpl(reimbursement_dao)


@app.route("/employee", methods=["get"])
def get_all_employee():
    username = request.args.get("username")
    password = request.args.get("password")
    try:
        if username is not None and password is not None:
            employee_dict = employees_service.login_employee(username, password)
            return employee_dict, 200
        else:
            employee = employees_service.get_all_employee()
            json_employee = [b.as_json_dict() for b in employee]
            return jsonify(json_employee), 200
    except Exception:
        return f"Unknown error has occurred."


@app.route("/employee/<employee_id>", methods=["get"])
def get_employee(employee_id: str):
    try:
        employee = employees_service.get_employee(int(employee_id))
        return jsonify(employee.as_json_dict()), 200
    except ResourceNotFoundError as e:
        return str(e), 404


# @app.route("/employee/<username>/<password>", methods=["get"])
# def login_employee(username: str, password: str):
#     employee_id = employees_service.login_employee(username, password)
#     if employee_id == 0:
#         return str(f"Incorrect username or password"), 404
#     else:
#         login = {"employeeId": employee_id}
#         return login


@app.route("/statistics", methods=["get"])
def stat_employee():
    statistics_list = employees_service.stat_employee()
    return jsonify(statistics_list), 200


@app.route("/reimbursement", methods=["post"])
def post_reimbursement():
    body = request.json
    print(body)
    reimbursement = Reimbursement(body["reimbursementId"], body["reimbursementAmount"], body["reimbursementState"],
                                  body["reimbursementLastDayModified"], body["reimbursementMessage"],
                                  body["reviewerId"], body["employeeId"], body["reimbursementResponse"],)
    print(reimbursement.employee_id)
    result = reimbursement_service.post_reimbursement(reimbursement, reimbursement.employee_id)
    return f"Created reimbursement", 201


@app.route("/reimbursement/all", methods=["get"])
def get_all_reimbursement():
    reimbursement = reimbursement_service.get_all_reimbursement()
    json_reimbursement = [b.as_json_dict() for b in reimbursement]
    return jsonify(json_reimbursement), 200


@app.route("/reimbursement/all/<employee_id>", methods=["get"])
def get_all_reimbursement_employee(employee_id: str):
    try:
        reimbursement: List[Reimbursement] = reimbursement_service.get_all_reimbursement_employee(int(employee_id))
        json_reimbursement = [b.as_json_dict() for b in reimbursement]
        return jsonify(json_reimbursement), 200
    except ResourceNotFoundError as e:
        return str(e), 404


@app.route("/reimbursement/<reimbursement_id>", methods=["get"])
def get_reimbursement(reimbursement_id: str):
    try:
        employee = reimbursement_service.get_reimbursement(int(reimbursement_id))
        return jsonify(employee.as_json_dict()), 200
    except ResourceNotFoundError as e:
        return str(e), 404


@app.route("/reimbursement/<reviewer_id>", methods=["put"])
def put_reimbursement(reviewer_id: str):
    try:
        body = request.json
        print(body)
        reimbursement = Reimbursement(body["reimbursementId"], body["reimbursementAmount"], body["reimbursementState"],
                                      body["reimbursementLastDayModified"], body["reimbursementMessage"],
                                      body["reviewerId"], body["employeeId"], body["reimbursementResponse"])
        reimbursement_service.put_reimbursement(reimbursement, int(reviewer_id))
        return f"Edited reimbursement {reimbursement.reimbursement_id}", 201
    except Exception:
        raise ResourceNotFoundError(f"No reimbursement found.")


if __name__ == '__main__':
    app.run()
