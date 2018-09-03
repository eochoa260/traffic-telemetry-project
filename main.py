import json
from dateutil import parser
from google.cloud import bigquery

client = bigquery.Client()
dataset_id = 'chicago_traffic'
table_id = 'chi_traffic_segments'
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)

def form_row(data):
    row = [{
        "SEGMENTID": int(data['segmentid']),
        "STREET": data['street'],
        "DIRECTION": data['_direction'],
        "FROM_STREET": data['_fromst'],
        "TO_STREET": data['_tost'],
        "LENGTH": float(data['_length']),
        "STREET_HEADING": data['_strheading'],
        "COMMENTS": data.get('_comments'),
        "START_LONGITUDE": float(data['start_lon']),
        "START_LATITUDE": float(data['_lif_lat']),
        "END_LONGITUDE": float(data['_lit_lon']),
        "END_LATITUDE": float(data['_lit_lat']),
        "CURRENT_SPEED": float(data['_traffic']),
        "LAST_UPDATED": parser.parse(data['_last_updt'])
    }]
    return row

def handle_traffic_data(data, context):
    import base64

    if 'data' in data:
        message = base64.b64decode(data['data']).decode('utf-8')
        message = json.loads(message)
        row = form_row(message)

        errors = client.insert_rows(table, row)

        assert errors == []


