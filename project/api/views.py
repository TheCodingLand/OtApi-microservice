# project/api/views.py


from flask import Blueprint, jsonify, request
from project.api import swagger
from project.ot.query_ot import query_ot
from project.ot.ot_models import Event, Ticket, Category
from project.ot.serialize import serialize, test
#these hold our data model folder, fields list, required fields
import time
from project.ot.ot_field import *

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




def getFields(object_model, data):
    fields = []
    for key in data.keys():
        if key in object_model.fields.keys():
            cls = globals()[object_model.fields[key]] 
            f = cls(key)
            f.value = data[key]   
            fields.append(f)
        else:
            print ("field not in globals")
            raise ValueError('field not in globals')
    return fields    




event_model=Event()
events_blueprint = Blueprint('events', __name__)    
@events_blueprint.route('/events', methods=['POST'])
def add_event():
    time.sleep(1)
    post_data = request.get_json()
    
    #if not post_data:
    #    response_object = {
    #        'status': 'fail',
    #        'message': 'Invalid payload.'
    #    }
    #   return jsonify(response_object), 400
   
    try:
        fields=getFields(event_model,post_data)
    except:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload parsing fields.'
        }
        return jsonify(response_object), 400
    try:
        r = query_ot()
        print (event_model)
        print(fields)
        event = r.add(event_model,fields)
        if event:
            response_object = {
                'status': 'success',
                'message': 'event was added!',
                'event' : event
            }
            return jsonify(response_object), 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'Sorry. failed.'
            }
            return jsonify(response_object), 400
    except:
        response_object = {
            'status': 'fail',
            'message': 'Invalid payload.'
        }
        return jsonify(response_object), 400

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



ticket_model=Ticket()
tickets_blueprint = Blueprint('tickets', __name__)    
@tickets_blueprint.route('/tickets/<ticket_id>', methods=['GET'])
def get_single_ticket(ticket_id):
    """Get single ticket details"""
    response_object = {
        'status': 'fail',
        'message': 'Event does not exist'
    }
    try:
        t=query_ot()
        t.get(ticket_id)
        result=serialize(t.xml_result.decode("utf-8"))
        ticket=result.res
        #event = test()
        if not ticket:
            return jsonify(response_object), 404
        
        wrong_type=False
        unexpected_fields = []
        for f in ticket.keys():
            if f not in ticket_model.fields:
                unexpected_fields.append(f)
                wrong_type=True
        if wrong_type == True:
            response_object = {
            'status': 'fail',
            'message': 'wrong object returned'
            }
            return jsonify(response_object), 400
        else:
            response_object = {
                'status': 'success',
                'data': ticket
            }
            return jsonify(response_object), 200
    except ValueError:
        return jsonify(response_object), 404



