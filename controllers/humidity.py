from aiohttp import web
from service.thingy_env_sensors import EnvironmentSensorDataService
from models.environment import EnvironmentSensorData


async def log_humidities(request):
    # data = await request.json()

    # if 'name' not in data:
    #     return web.json_response({'error': '"name" is a required field'})
    # name = data['name']
    # if not isinstance(name, str) or not len(name):
    #     return web.json_response({'error': '"name" must be a string with at least one character'})

    name = 'humidity_series'
    humidity_service = EnvironmentSensorDataService()
    humidity_service.run_humidity_service(name)

    return web.Response(status=204)

async def delete_humidty_log(request):
    pass


def delete_humidity_log(request):
    #todo test with json data post
    #data = await request.json()

    #if 'name' not in data:
    #    return web.json_response({'error': '"name" is a required field'})
    #name = data['name']
    #if not isinstance(name, str) or not len(name):
    #    return web.json_response({'error': '"name" must be a string with at least one character'})

    #temp
    name = 'humidity_series'
    temperature_log = EnvironmentSensorData()
    temperature_log.delete(name)

    return web.Response(status=204)