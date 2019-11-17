from zato.server.service import Service
 
class GetOrganizations(Service):
    class SimpleIO:
        input_required = ()
        output_required = ('data')
    def handle(self):
         syst = self.outgoing.plain_http.get('dhis2.outgoing.getOUs')
         response = syst.conn.get(self.cid)
         self.response.payload['data'] = response.json()
