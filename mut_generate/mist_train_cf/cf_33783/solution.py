"""
QUESTION:
Create a function `analyze_covid_data(covid_data)` that takes a list of dictionaries as input, where each dictionary contains COVID-19 data for a specific region and state on a given date. The function should calculate the total new cases and new deaths for each region and state, identify the region and state with the highest total new cases and new deaths, and return a dictionary with the total new cases and new deaths for each region and state, along with the region and state with the highest numbers. Each dictionary in the input list should have 'region', 'state', 'newcases', and 'newdeaths' keys. The output dictionary should have a specific structure with concatenated region and state as keys and the total new cases and new deaths as values, as well as separate keys for the region and state with the highest total new cases and new deaths.
"""

def analyze_covid_data(covid_data):
    region_state_cases_deaths = {}
    max_cases = 0
    max_deaths = 0
    region_with_highest_cases = ''
    state_with_highest_cases = ''
    region_with_highest_deaths = ''
    state_with_highest_deaths = ''

    for entry in covid_data:
        region = entry['region']
        state = entry['state']
        total_new_cases = entry['newcases']
        total_new_deaths = entry['newdeaths']

        key = f"{region}_{state}"
        if key in region_state_cases_deaths:
            region_state_cases_deaths[key]['total_new_cases'] += total_new_cases
            region_state_cases_deaths[key]['total_new_deaths'] += total_new_deaths
        else:
            region_state_cases_deaths[key] = {'total_new_cases': total_new_cases, 'total_new_deaths': total_new_deaths}

        if region_state_cases_deaths[key]['total_new_cases'] > max_cases:
            max_cases = region_state_cases_deaths[key]['total_new_cases']
            region_with_highest_cases = region
            state_with_highest_cases = state

        if region_state_cases_deaths[key]['total_new_deaths'] > max_deaths:
            max_deaths = region_state_cases_deaths[key]['total_new_deaths']
            region_with_highest_deaths = region
            state_with_highest_deaths = state

    result = {
        **region_state_cases_deaths,
        'region_with_highest_cases': region_with_highest_cases,
        'state_with_highest_cases': state_with_highest_cases,
        'region_with_highest_deaths': region_with_highest_deaths,
        'state_with_highest_deaths': state_with_highest_deaths
    }
    return result