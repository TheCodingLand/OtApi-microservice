js= """{
	"Envelope": {
		"Body": {
			"GetObjectList": {
				"Get": {
					"Filter": {
						"StringVal": {
							"_name": "UCID",
							"__text": "1231244123"
						},
						"__text": "EventUCID"
					},
					"_folderPath": "01. ITSM - Service Operation\\01. Event Management",
					"_recursive": "true"
				},
				"_xmlns": "http://www.omninet.de/OtWebSvc/v1"
			},
			"__prefix": "soap"
		},
		"_xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
		"_xmlns:xsl": "http://www.w3.org/2001/XMLSchema",
		"_xmlns:soap": "http://www.w3.org/2003/05/soap-envelope",
		"__prefix": "soap"
	}
}"""

def data():
    return js
    