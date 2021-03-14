## Спецификация OpenAPI 3
```JSON
{
  "openapi": "3.0.2",
  "info": {
    "title": "Server Monitoring API",
    "version": ""
  },
  "paths": {
    "/notes/": {
      "get": {
        "operationId": "listNotes",
        "description": "",
        "parameters": [
          {
            "name": "query",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "type": "array",
                  "items": {
                    "$ref": "#/components/schemas/Notes"
                  }
                }
              }
            },
            "description": ""
          }
        },
        "tags": [
          "notes"
        ]
      },
      "post": {
        "operationId": "createNotes",
        "description": "",
        "parameters": [],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            }
          }
        },
        "responses": {
          "201": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Notes"
                }
              }
            },
            "description": ""
          }
        },
        "tags": [
          "notes"
        ]
      }
    },
    "/notes/{id}/": {
      "get": {
        "operationId": "retrieveNotes",
        "description": "",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "A unique integer value identifying this notes.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "query",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Notes"
                }
              }
            },
            "description": ""
          }
        },
        "tags": [
          "notes"
        ]
      },
      "put": {
        "operationId": "updateNotes",
        "description": "",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "A unique integer value identifying this notes.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "query",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Notes"
                }
              }
            },
            "description": ""
          }
        },
        "tags": [
          "notes"
        ]
      },
      "patch": {
        "operationId": "partialUpdateNotes",
        "description": "",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "A unique integer value identifying this notes.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "query",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            },
            "application/x-www-form-urlencoded": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            },
            "multipart/form-data": {
              "schema": {
                "$ref": "#/components/schemas/Notes"
              }
            }
          }
        },
        "responses": {
          "200": {
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Notes"
                }
              }
            },
            "description": ""
          }
        },
        "tags": [
          "notes"
        ]
      },
      "delete": {
        "operationId": "destroyNotes",
        "description": "",
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "required": true,
            "description": "A unique integer value identifying this notes.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "query",
            "required": false,
            "in": "query",
            "description": "A search term.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "204": {
            "description": ""
          }
        },
        "tags": [
          "notes"
        ]
      }
    }
  },
  "components": {
    "schemas": {
      "Notes": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "readOnly": true
          },
          "title": {
            "type": "string"
          },
          "content": {
            "type": "string",
            "maxLength": 255
          }
        },
        "required": [
          "content"
        ]
      }
    }
  }
}
```