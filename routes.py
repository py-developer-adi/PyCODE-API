'''PyCODE | @_py.code'''

# ? Importing Libraries
from flask import Blueprint, jsonify, request
from datetime import datetime
from models import *
from uuid import uuid4

# ! Api Router
api = Blueprint('api', __name__)
routes = {
    "/": ["GET", "gets all routes"],
    "/snippets": ["GET", "gets all snippets"],
    "/snippets/<id>": ["GET", "gets a specific snippet of given id"],
    "/snippets/add": ["POST", "adds a snippet"],
    "/snippets/update/<id>": {"PUT", "udates the snippet of given id"},
    "/snippets/delete/<id>": ["DELETE", "deletes the snippet of given id"]
}

# : Base Route
@api.route('/')
def home():
    return jsonify(routes)

# | Route for a snippet
@api.route('/snippets/')
def send_snippets():
    all_snippets = Snippet.query.all()
    return jsonify([
        {
            'id': d.id,
            'title': d.title,
            'code': d.code,
            'lang': d.lang,
            'created_at': d.created_at
        } for d in all_snippets
    ])
    
# | Route to get a specific snippet
@api.route('/snippets/<id>')
def send_spinnet(id):
    snippet = Snippet.query.filter_by(id=id).first()
    
    if not snippet:
        return jsonify({
            "error": "snippet not found"
        }), 404
        
    return jsonify({
        "id": snippet.id,
        "title": snippet.title,
        "code": snippet.code,
        "lang": snippet.lang,
        "created_at": snippet.created_at
    })
    
# | Route to Add New Snippet
@api.route('/snippets/add', methods=['POST'])
def add_snippet():
    snippet: dict = request.json
    id = str(uuid4())
    
    new_snippet = Snippet(
        id=id,
        title=snippet.get("title", "Untitled"),
        code=snippet.get("code"),
        lang=snippet.get("lang"),
    )
    db.session.add(new_snippet)
    db.session.commit()
    
    return jsonify({
        "status": 200,
        "msg": "New Snipet saved",
        "id": id
    })
    
# | Route to Update any Snippet
@api.route('/snippets/update/<id>', methods=['PUT'])
def update_snippet(id):
    snippet: dict = Snippet.query.filter_by(id=id).first()
    
    if not snippet:
        return jsonify({
            "error": "snippet not found!"
        })
        
    data = request.json
    
    snippet.title = data.get("title", snippet.title)
    snippet.code = data.get("code", snippet.code)
    snippet.lang = data.get("lang", snippet.lang)
    
    db.session.commit()
    return jsonify({
        "status": 200,
        "msg": "snippet updated!"
    })
    
# | Route to Delete any Snippet
@api.route('/snippets/delete/<id>', methods=['DELETE'])
def delete_snippet(id):
    snippet = Snippet.query.filter_by(id=id).first()
    
    if not snippet: return jsonify({
        "error": "snippet not found!"
    })
    
    db.session.delete(snippet)
    db.session.commit()
    
    return jsonify({
        "status": 200,
        "msg": "snippet deleted successfully!"
    })