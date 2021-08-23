from google.cloud import datastore
client = datastore.Client()
query = client.query(kind='OmsOpsUIFunctions')
result = query.add_filter('description', '=', 'Shipments').fetch()
list(result)
