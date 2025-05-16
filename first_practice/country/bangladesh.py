from fastapi import APIRouter

routers = APIRouter()

@routers.get('/bd')
def bangladesh():
    return {
        'status': 'success',
        'data':[
            {'country_name': 'BANGLADESH'},
            {'capital': 'Dhaka'},
            {'language': 'Bangla'},
            {'currency': 'Taka'},
            {'population': '170 million'},
            {'region': 'South Asia'}
        ]
    }

