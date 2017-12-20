# project/api/views.py


from flask import Blueprint, jsonify, request
from project.api import swagger
from project.ot.query_ot import query_ot
from project.ot.ot_models import Event, Ticket, Category
from project.ot.serialize import serialize, test
#these hold our data model folder, fields list, required fields


swagger_blueprint = Blueprint('swagger', __name__)
@swagger_blueprint.route('/service.json', methods=['GET'])
def service():
    return jsonify(swagger.swagger())

base_blueprint = Blueprint('base', __name__)
@base_blueprint.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })



ot_objects_blueprint = Blueprint('ot_objects', __name__)
@ot_objects_blueprint.route('/ot_objects/metadata/<object_id>', methods=['GET'])
def get_ot_object_metadata(object_id):
    """Get single event details"""
    response_object = {
        'status': 'fail',
        'message': 'Event does not exist'
    }
    try:
        e=query_ot()
        e.get(object_id)
        print ("%s" % e.xml_result)
        result=serialize(e.xml_result.decode("utf-8"))
        ot_object=result.metadata
        if not ot_object:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': ot_object
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404

event_model=Event()
events_blueprint = Blueprint('events', __name__)    
@events_blueprint.route('/events/<event_id>', methods=['GET'])
def get_single_event(event_id):
    """Get single event details"""
    response_object = {
        'status': 'fail',
        'message': 'Event does not exist'
    }
    try:
        e=query_ot()
        e.get(event_id)
        result=serialize(e.xml_result.decode("utf-8"))
        event=result.res
        #event = test()
        if not event:
            return jsonify(response_object), 404
        
        wrong_type=False
        unexpected_fields = []
        for f in event.keys():
            if f not in event_model.fields:
                unexpected_fields.append(f)
                wrong_type=True
        if wrong_type == True:
            response_object = {
            'status': 'fail',
            #'message': 'unexpected fields : %s' % (unexpected_fields)
            'message': 'wrong object returned'
            }
            return jsonify(response_object), 400
        else:
            response_object = {
                'status': 'success',
                'data': event
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404


tickets_blueprint = Blueprint('tickets', __name__)    
@tickets_blueprint.route('/tickets/<ticket_id>', methods=['GET'])
def get_single_ticket(ticket_id):
    """Get single ticket details"""
    response_object = {
        'status': 'fail',
        'message': 'Event does not exist'
    }
    try:
        e=query_ot()
        e.get(ticket_id)
  
        result=serialize(e.xml_result.decode("utf-8"))
        #event = test()
        ticket = result.res
        if not ticket:
            return jsonify(response_object), 404
        else:
            response_object = {
                'status': 'success',
                'data': ticket
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404
        
        

