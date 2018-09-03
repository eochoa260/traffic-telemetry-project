import json
from google.cloud import pubsub
from sodapy import Socrata

publisher = pubsub.PublisherClient()
topic_path = publisher.topic_path('tutorial-182618', 'chi-traffic')

def get_traffic_data():
    APP_TOKEN = "6haMNOLuHLrz7Hz1OLv7USSnk"
    client = Socrata("data.cityofchicago.org",
                     APP_TOKEN,
                     username="eochoa260@gmail.com",
                     password="GoogleInterview1")
    
    results = client.get("8v9j-bter")
    return results

# sample_message = [{u'_lif_lat': u'41.8305024208', u'segmentid': u'146', u'start_lon': u'-87.6657517025', u'_lit_lat': u'41.8231529963', u'_strheading': u'S', u'_traffic': u'27', u'_lit_lon': u'-87.6654916893', u'_tost': u'Pershing', u'street': u'Ashland', u'_last_updt': u'2018-08-26 16:30:52.0', u'_length': u'0.5', u'_fromst': u'35th', u'_direction': u'SB'}, {u'_lif_lat': u'41.751121301', u'segmentid': u'705', u'start_lon': u'-87.6151773651', u'_lit_lat': u'41.7438113955', u'_strheading': u'S', u'_traffic': u'27', u'_lit_lon': u'-87.6149257801', u'_tost': u'83rd', u'street': u'Dr Martin L King Jr', u'_last_updt': u'2018-08-26 16:31:03.0', u'_length': u'0.5', u'_fromst': u'79th', u'_direction': u'SB'}, {u'_strheading': u'S', u'_lif_lat': u'41.7282286362', u'segmentid': u'332', u'start_lon': u'-87.6821164908', u'_lit_lat': u'41.7355262471', u'_comments': u'IDOT Signals Possible', u'_traffic': u'35', u'_lit_lon': u'-87.6823308541', u'_tost': u'87th', u'street': u'Western', u'_last_updt': u'2018-08-26 16:30:56.0', u'_length': u'0.5', u'_fromst': u'91st', u'_direction': u'NB'}] 
results = get_traffic_data()

for message in results:
    data = json.dumps(message)
    data = data.encode('utf-8')
    publisher.publish(topic_path, data=data)

print('Publised messages.')
