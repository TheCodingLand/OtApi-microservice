
class query_ot():
    
    
    
    
    def __init__(self):
        self.body=""
        self.command =""
        command = ""
        self.headers = ""
        self.xml = ""
        self.xml_result = ""
        self.result = ""
        
    def get(self, id):
        """Takes ID returns a formatted object"""
        self.body = r'<Get folderPath="" recursive="true"><ObjectIDs objectIDs="%s"/></Get>' % (id)
        self.command="GetObjectList"
    
    def getField(self, id, field):
        """Takes ID and a specific ot_field to query"""
        self.body = r'<Get folderPath="" recursive="true"><ObjectIDs objectIDs="%s"/><RequiredFields>%s</RequiredFields></Get>' % (id, field.name)
        self.command="GetObjectList"
        
    #def update(self, id, fields):
        
  
    def initQuery(self):
        """puts together hearders qnd command definition for the query"""
        self.headers = {'Content-Type': 'text/xml', 'charset': 'iso-8859-1',
                        'SOAPAction': '"http://www.omninet.de/OtWebSvc/v1/%s"'
                        % (self.command)}
        self.query = self.build()
        
    def build(self):
        """puts together hearders and command definition for the query"""
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
                    
   
        
        
        