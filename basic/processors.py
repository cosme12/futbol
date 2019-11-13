def main_config(request):
    # Create fixed data structures to pass to template
    # data could equally come from database queries
    # web services or social APIs
    config_data = {
        'WEB_NAME': 'Futbol',
        'COMPANY': 'Copito System',
        'START_END_YEAR': '2019 - 2020',
    }
    return {'CONFIG_DATA': config_data}
