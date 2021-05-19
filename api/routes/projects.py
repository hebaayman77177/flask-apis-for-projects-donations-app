#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.projects import Project, ProjectSchema
from api.utils.database import db
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt

jwt_refresh_token_required = jwt_required(refresh=True)

project_routes = Blueprint("project_routes", __name__)


@project_routes.route("/", methods=["POST"])
@jwt_required()
def create_project():
    try:
        data = request.get_json()
        data["user_id"] = get_jwt_identity()
        project_schema = ProjectSchema()
        project = project_schema.load(data)
        result = project_schema.dump(project.create())
        return response_with(resp.SUCCESS_201, value={"project": result})
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)


@project_routes.route("/", methods=["GET"])
def get_project_list():
    fetched = Project.query.all()
    project_schema = ProjectSchema(
        many=True, only=["id", "title", "details", "total_target", "user_id"]
    )
    print(fetched)
    projects = project_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"projects": projects})


@project_routes.route("/<int:id>", methods=["GET"])
def get_project_detail(id):
    fetched = Project.query.get_or_404(id)
    project_schema = ProjectSchema()
    projects = project_schema.dump(fetched)
    return response_with(resp.SUCCESS_200, value={"projects": projects})


# @project_routes.route("/<int:id>", methods=["PUT"])
# @jwt_required()
# def update_project_detail(id):
#     data = request.get_json()
#     get_project = Project.query.get_or_404(id)
#     get_project.title = data["title"]
#     get_project.details = data["details"]
#     get_project.total_target = data["total_target"]
#     get_project.user_id = data["user_id"]
#     db.session.add(get_project)
#     db.session.commit()
#     project_schema = ProjectSchema()
#     project = project_schema.dump(get_project)
#     return response_with(resp.SUCCESS_200, value={"project": project})


@project_routes.route("/<int:id>", methods=["PATCH"])
@jwt_required()
def modify_project_detail(id):
    current_user = get_jwt_identity()
    data = request.get_json()
    get_project = Project.query.get_or_404(id)
    if get_project.user_id != current_user:
        return response_with(resp.FORBIDDEN_403)
    if data.get("title"):
        get_project.title = data["title"]
    if data.get("details"):
        get_project.year = data["details"]
    if data.get("total_target"):
        get_project.year = data["total_target"]
    if data.get("user_id"):
        get_project.year = data["user_id"]
    db.session.add(get_project)
    db.session.commit()
    project_schema = ProjectSchema()
    project = project_schema.dump(get_project)
    return response_with(resp.SUCCESS_200, value={"project": project})


@project_routes.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_project(id):
    current_user = get_jwt_identity()
    get_project = Project.query.get_or_404(id)
    if get_project.user_id != current_user:
        return response_with(resp.FORBIDDEN_403)
    db.session.delete(get_project)
    db.session.commit()
    return response_with(resp.SUCCESS_204)
