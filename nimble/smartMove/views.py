from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Template, Context
from django.template import RequestContext

import json

@csrf_exempt
def showHouses(request):
    if request.method == 'GET':
        try:
            location1 = request.GET['1']
            location2 = request.GET['2']
            location3 = request.GET['3']
            totlat = 0
            totlng = 0
            for i in range(3):
                area = "location"+str(i+1)
                geocode = "https://maps.googleapis.com/maps/api/geocode/json?address=" + area
                gresp = requests.get(geocode)
                gresp = json.loads(gresp.content)
                """
                gresp -> results -> 0 -> geometry ->bounds, location ->lat, long
                """
                latlng = []
                totlat += gresp["results"][0]["geometry"]["location"]["lat"]
                totlng += gresp["results"][0]["geometry"]["location"]["lng"]

            avglat = totlat/3.0
            avglng = totlng/3.0

            revsgeo = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng="+str(avglat)+","+str(avglng))
            revsgeo = json.loads(revsgeo.content)
            inp_str = str(revsgeo["results"][-6]["address_components"][0]["long_name"])

            area_resph = requests.get("https://regions.housing.com/api/v1/polygon/suggest?input="\
                                    +inp_str+"&service_type=rent&cursor=8&source=web")
            area_parseh = json.loads(area_resph.content)

            area_respc = requests.get("https://www.commonfloor.com/autosuggest.php?c=Bangalore&\
                                    item=locationbuilderproject&str="+inp_str+"&res_type=json")
            area_respc = json.loads(area_respc.content)

            count = 0
            area = []
            for area_count in range(area_respc["count"]):
                if area_respc["data"][area_count]["type"] == "area":
                    area_codec = area_respc["data"][area_count]["id"]
                    area_codec = "area_"+str(area_codec)
                    area.append(area_codec)
            for area_codec in area:
                url = 'https://www.commonfloor.com/nitro/search/search-results'
                payload = {"search_intent":"rent","property_location_filter":[area_codec],"city":"Bangalore"}
                respc = requests.post(url, data=json.dumps(payload))
                resp_parsec = json.loads(respc.content)

                for houses in range(resp_parsec["result_count"]):
                    try:
                        print resp_parsec["data"][houses]["children"][0]["title"],
                        print resp_parsec["data"][houses]["children"][0]["lat"],
                        print resp_parsec["data"][houses]["children"][0]["lng"],
                        print resp_parsec["data"][houses]["children"][0]["price"]
                        count += 1
                    except:
                        break


            area_codeh = []
            for index in range(10):
                try:
                    #print area_parseh[index]['uuid']
                    if len(area_parseh[index]['uuid']) <= 7:
                        area_codeh.append(str(area_parseh[index]['uuid']))
                    else:
                        None
                except:
                    break

            for iterat in area_codeh:
                resph = requests.get("https://rails.housing.com//api/v3/rent/filter?&est="\
                                +iterat+"&radius=500&details=true&sort_key=relevance&\
                                sort_order=ASC&personalisation_status=on")
                resp_parseh = json.loads(resph.content)

                for i in range(50):
                    try:
                        print resp_parseh['hits']['hits'][i]['_source']['locality'],
                        print resp_parseh['hits']['hits'][i]['_source']['latitude'],
                        print resp_parseh['hits']['hits'][i]['_source']['longitude'],
                        print resp_parseh['hits']['hits'][i]['_source']['formatted_rent'],
                        print resp_parseh['hits']['hits'][i]['_source']['lifestyle_rating']
                    except:
                        break

                if request.method == 'POST':
                    latitude = request.POST['lat']
                    longitude = request.POST['lng']
                    geomatrix = requests.get("https://maps.googleapis.com/maps/api/distancematrix/json?origins="+latitude+","+longitude+"&destinations="+location1+"|"+location2+"|"+location3+"|"+"kempegowda+International+Airport+Bangalore")
                geomatrix = json.loads(geomatrix)
                for i in range(3):
                    loc = "location"+str(i+1)
                    print loc,
                    print geomatrix["rows"][0]["elements"][i]
                    
            response_message = {}
            response_message['message'] = 'Success'
            return HttpResponse(json.dumps(response_message))
        except:
            raise Http404

@csrf_exempt
def index(requests):
    return render_to_response('nimble/index.html')

