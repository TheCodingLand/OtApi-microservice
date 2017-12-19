


class otQuery():
    def __init__(self, requesttype, **kwargs):
        self.request_type = requesttype
        self.headers = initQuery()
        self.xml = ""
        self.xml_result = ""
        self.result = ""
    
        
        
    def initQuery(self):
        self.headers = {'Content-Type': 'text/xml', 'charset': 'iso-8859-1',
                        'SOAPAction': '"http://www.omninet.de/OtWebSvc/v1/%s"'
                        % (self.requesttype)}
        self.query = self.build()
        
    def build(self):
        self.xml = r'<?xml version="1.0" encoding="utf-8"?><soap:Envelope ' + \
            r'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ' + \
                   r'xmlns:xsd="http://www.w3.org/2001/XMLSchema" ' + \
                   r'xmlns:soap="http://www.w3.org/2003/05/soap-envelope"><soap:Body>' + \
                   r'<%s xmlns="http://www.omninet.de/OtWebSvc/v1">' % (self.command) + \
                   r'%s</%s></soap:Body></soap:Envelope>' \
                   % (self.body, self.command)
        
    def send(self):
        data = self.xml.replace(r'\r\n', r'&#x000d;&#x000a;').encode("ascii", "xmlcharrefreplace")
        result = requests.post(url, data=data, headers=self.headers)
        self.xml_result = result.content
        return self
                    
    def get(self, id):
        self.command = "GetObjectList"
        self.body = r'<Get folderPath="" recursive="true"><ObjectIDs objectIDs="%s"/></Get>' % (id)
        
        
        