import requests
import json
def request(origin,dest,int1,int2,int3):
    data = {
        'origin':{
        'address': f'{origin}, Chennai'
    },
    'destination':{
        'address': f'{dest}, Chennai'
    },
    'intermediates': [
        {
        'address': f'{int1}, Chennai'
        },
        
        {
        'address': f'{int2}, Chennai'
        },

        {
        'address': f'{int3}, Chennai'
        },

    ],
    'travelMode': 'DRIVE',
    }

    header = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': '',
        'X-Goog-FieldMask': 'routes.optimizedIntermediateWaypointIndex',
        'X-Goog-FieldMask': 'routes.duration',


    }

    response = requests.post('https://routes.googleapis.com/directions/v2:computeRoutes', headers=header,json=data)
    response=response.json()
    #print("Status Code", response.status_code)
    #print("JSON Response ", (response.get('routes')[0]['duration'][:-1]))
    return ([(origin,dest,int1,int2,int3),(response.get('routes')[0]['duration'][:-1])])


if __name__ == "__main__":
    print(request(" Adyar","Alwarpet","Ambattur","Aminjikarai","Anna Nagar"))
