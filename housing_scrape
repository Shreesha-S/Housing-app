import requests
import json

area_code = "134222"
resp = requests.get("https://rails.housing.com//api/v3/rent/filter?&est="\
                    +area_code+"&radius=500&details=true&sort_key=relevance&\
                    sort_order=ASC&personalisation_status=on&version=1442728800")
resp_parse = json.loads(resp.content)
"""
    resp_parse -> hits, _shards, took, aggregations, profile_used, timed_out
    
    resp_parse['hits'] -> hits, total, max_score 

    PATH -> resp_parse['hits']['hits'][1]['_source']
    
formatted_security_deposit      hide_building_name      updated_at
street_info                     canonical_url           lease_type
rent                            shortened_url           locality_url_name
date_added                      id                      negotiable
view_count                      freshness_index         building_polygon_name
bathroom_count                  seo_title               lifestyle_rating
security_deposit                city_url_name           latitude
client_uuid_id                  age_of_property         thumb_name
locality_polygon_uuid           description             thumb_id
brokerage                       thumb_url               sublocality_polygon_uuid
locality                        apartment_type          longitude
landmark                        image_count             seo_address_tags
date_added_in_seconds           property_type           building_name
area                            furnish_type            building_id
vailable_from                   city_name               formatted_rent
thumb_url_new
"""

for i in range(50):
    try:
        print resp_parse['hits']['hits'][i]['_source']['latitude'],
        print resp_parse['hits']['hits'][i]['_source']['longitude'],
        print resp_parse['hits']['hits'][i]['_source']['formatted_rent'],
        print resp_parse['hits']['hits'][i]['_source']['lifestyle_rating']
    except:
        break

