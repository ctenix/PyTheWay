from wos import WosClient
import wos.utils

with WosClient(SID="6FNynd3mH2rVv8IzEB8",lite=True) as client:
    #print(wos.utils.query(client, 'SO=Synthetic Metals AND TI=nanotub*'))
    #print(client.retrieveById(uid="WOS:000302205300003")) 
    #print(client.citedReferences(uid="WOS:000302205300003"))#Primium API, not available in lite access
    print(client.search(query="petroleum"))