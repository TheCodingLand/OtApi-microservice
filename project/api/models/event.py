
from flask_restplus import fields
from project.api.restplus import api

event = api.model('Event:', {
    'UCID': fields.Integer(description='call id'),
    'start': fields.DateTime,
})