import requests
import json


print ("Enter the locality frequently visited.")
inp_str = raw_input().strip()
area_resp = requests.get("https://regions.housing.com/api/v1/polygon/suggest?input="\
                        +inp_str+"&service_type=rent&cursor=8&source=web")
area_parse = json.loads(area_resp.content)

"""
Link to get area code: https://regions.housing.com/api/v1/polygon/suggest?
                        input=bangalore central, ksrtc layout, 2nd phase, j. p. nagar, 
                        bangalore&service_type=rent&cursor=8&source=web

Attributes: uuid, took, is_valid, city_id, super_type, type, name
"""

area_code = []
for index in range(10):
    try:
        print area_parse[index]['uuid']
        if len(area_parse[index]['uuid']) <= 7:
            area_code.append(str(area_parse[index]['uuid']))
        else:
            None
    except:
        break

for iterat in area_code:
    resp = requests.get("https://rails.housing.com//api/v3/rent/filter?&est="\
                    +iterat+"&radius=500&details=true&sort_key=relevance&\
                    sort_order=ASC&personalisation_status=on")
    resp_parse = json.loads(resp.content)

    """
        resp_parseh -> hits, _shards, took, aggregations, profile_used, timed_out
        
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
            print resp_parse['hits']['hits'][i]['_source']['locality'],
            print resp_parse['hits']['hits'][i]['_source']['latitude'],
            print resp_parse['hits']['hits'][i]['_source']['longitude'],
            print resp_parse['hits']['hits'][i]['_source']['formatted_rent'],
            print resp_parse['hits']['hits'][i]['_source']['lifestyle_rating']
        except:
            break

