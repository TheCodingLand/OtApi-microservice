
def swagger():
    js = {
  "swagger": "2.0",
  "info": {
    "version": "0.0.1",
    "title": "Users Service",
    "description": "Swagger spec for documenting the users service"
  },
  "host": "148.110.107.15:5001",
  "schemes": [
    "http"
  ],
  "securityDefinitions": {
    "Bearer": {
      "type": "apiKey",
      "name": "Authorization",
      "in": "header"
    }
  },
  "paths": {
    "/ping": {
      "get": {
        "description": "Returns a sanity check",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "Will return 'pong!'"
          }
        }
      }
    },
    "/events/{id}": {
      "get": {
        "description": "Returns an event based on a single event ID",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of Event to fetch",
            "required": True,
            "type": "integer",
            "format": "int64"
          }
        ],
        "responses": {
          "200": {
            "description": "event object"
          }
        }
      }
    },
    "/users": {
      "get": {
        "description": "Returns all users",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "user object"
          }
        }
      },
      "post": {
        "description": "Adds a new user",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "user",
            "in": "body",
            "description": "User to add",
            "required": True,
            "schema": {
              "$ref": "#/definitions/User"
            }
          }
        ],
        "security": [
          {
            "Bearer": []
          }
        ],
        "responses": {
          "200": {
            "description": "User added"
          }
        }
      }
    },
    "/users/{id}": {
      "get": {
        "description": "Returns a user based on a single user ID",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "description": "ID of user to fetch",
            "required": True,
            "type": "integer",
            "format": "int64"
          }
        ],
        "responses": {
          "200": {
            "description": "user object"
          }
        }
      }
    },
    "/auth/register": {
      "post": {
        "description": "Creates a new user",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "user",
            "in": "body",
            "description": "User to add",
            "required": True,
            "schema": {
              "$ref": "#/definitions/User"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "Successfully registered"
          }
        }
      }
    },
    "/auth/login": {
      "post": {
        "description": "Logs a user in",
        "produces": [
          "application/json"
        ],
        "parameters": [
          {
            "name": "user",
            "in": "body",
            "description": "User to log in",
            "required": True,
            "schema": {
              "$ref": "#/definitions/User"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully logged in"
          }
        }
      }
    },
    "/auth/status": {
      "get": {
        "description": "Returns the logged in user's status",
        "produces": [
          "application/json"
        ],
        "security": [
          {
            "Bearer": []
          }
        ],
        "responses": {
          "200": {
            "description": "user object"
          }
        }
      }
    },
    "/auth/logout": {
      "get": {
        "description": "Logs a user out",
        "produces": [
          "application/json"
        ],
        "security": [
          {
            "Bearer": []
          }
        ],
        "responses": {
          "200": {
            "description": "Successfully logged out"
          }
        }
      }
    }
  },
  "definitions": {
    "User": {
      "type": "object",
      "required": [
        "username",
        "email",
        "password"
      ],
      "properties": {
        "username": {
          "type": "string"
        },
        "email": {
          "type": "string"
        },
        "password": {
          "type": "string"
        }
      }
    }
  }
}
    return js