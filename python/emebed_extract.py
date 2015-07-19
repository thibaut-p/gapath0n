
import urllib3
import csv
import json
from pprint import pprint


class AvailableProgrammes:
    @property
    def programmes(self):
        txdata = None
        http = urllib3.PoolManager()
        txheaders = {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        url = 'http://www.getembed.com/4/programmes/'

        req = http.request('GET', url, txdata, txheaders)
        print(req.status)

        self._programmes = json.loads(req.data.decode("utf-8"))
        return self._programmes

class Programme:
    def __init__(self, metadata):
        self.metadata = metadata
        self.url = ''

    @property
    def projects(self):
        print(self.metadata['name'])
        self.url = 'http://www.getembed.com'+self.metadata['projects']
        print(self.url)
        txdata = None
        http = urllib3.PoolManager()
        txheaders = {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        req = http.request('GET', self.url, txdata, txheaders)
        print(req.status)
        self._projects = json.loads(req.data.decode("utf-8"))

        return self._projects

class Project:
    def __init__(self, metadata):
        self.metadata = metadata
        self.url = ''

    @property
    def entities(self):
        txdata = None
        http = urllib3.PoolManager()
        txheaders = {'User-agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        self.url = 'http://www.getembed.com/4/projects/'+self.metadata['project_id']+'/entities/'
        req = http.request('GET', self.url, txdata, txheaders)
        self._entities = json.loads(req.data.decode("utf-8"))
        return self._entities

class Entity:
    def __init__(self, metadata):
        self.metadata = metadata
        self._profiles = None

    def valid(self):
        keep = False
        if len(self.metadata['profiles']) > 0:
                for profile in self.metadata['profiles']:
                    if ('space_heating_requirement' in profile['profile_data'] and profile['profile_data']['space_heating_requirement'] is not None) or \
                        ('ber' in profile['profile_data'] and profile['profile_data']['ber'] is not None) or \
                        ('primary_energy_requirement' in profile['profile_data'] and profile['profile_data']['primary_energy_requirement'] is not None):

                        keep |= True
        return keep

    def fully_valid(self):
        keep = True
        measures_found = True

        if len(self.metadata['profiles']) > 0:
                for profile in self.metadata['profiles']:
                    if ('space_heating_requirement' in profile['profile_data'] and profile['profile_data']['space_heating_requirement'] is not None) and \
                        ('ber' in profile['profile_data'] and profile['profile_data']['ber'] is not None) and \
                        ('primary_energy_requirement' in profile['profile_data'] and profile['profile_data']['primary_energy_requirement'] is not None):

                        keep &= True

                        if len(self.metadata['devices']) > 0:
                            for device in self.metadata['devices']:
                                if len(device['readings']) > 0:
                                    for reading in device['readings']:
                                        if reading['upper_ts'] is not None:
                                            measures_found &= True
                                else:
                                    measures_found &= False
                        else:
                            measures_found &= False

                    else:
                        keep &= False
                        measures_found &= False
        else:
            keep = False
            measures_found = False

        if keep:
            keep = 1
        else:
            keep = 0
        if measures_found:
            measures_found = 1
        else:
            measures_found = 0
        return keep, measures_found

    def profiles_exists(self):
        return 'profiles' in self.metadata

    @property
    def profiles(self):
        if 'profiles' in self.metadata:
            self._profiles = self.metadata['profiles']
            return self._profiles
        else:
            return []


def main():
    programmes = AvailableProgrammes()
    programmes_data = programmes.programmes

    nb_programs = 0
    nb_projects = 0
    nb_entities = 0
    nb_valid_entities = 0

    file = open('all_buildings.csv', 'w',  newline='')
    csvFile = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csvFile.writerow(['programme_name', 'programme_id', 'project_name', 'project_id', 'project_url', 'property_code', 'entity_id', 'correct_profile', 'fully_correct_profile', 'fcorrect_measures', 'space_heating_requirement','ber', 'primary_energy_requirement', 'profile_event_type'])

    for program_data in programmes_data:
        nb_programs += 1
        programme = Programme(program_data)
        # pprint(programme.projects)

        if programme.metadata['name'] != 'Building Performance Evaluation':
            continue

        for project_data in programme.projects:
            nb_projects += 1
            project = Project(project_data)
            # pprint(project.entities)
            for entity_data in project.entities['entities']:
                nb_entities += 1
                entity = Entity(entity_data)
                if entity.valid():
                    nb_valid_entities += 1
                    pprint(entity.metadata['entity_id'])
                    pprint(entity.metadata['property_code'])

                    correct_profile = True
                else:
                    correct_profile = False

                fully_correct_profile, fcorrect_measures = entity.fully_valid()

                shr = None
                ber = None
                per = None
                profile_event_type = None

                if entity.profiles_exists() and correct_profile:
                    for profile in entity.profiles:
                        if 'space_heating_requirement' in profile['profile_data']:
                            shr = profile['profile_data']['space_heating_requirement']

                        if 'ber' in profile['profile_data']:
                            ber = profile['profile_data']['ber']

                        if 'primary_energy_requirement' in profile['profile_data']:
                            per = profile['profile_data']['primary_energy_requirement']


                        if 'event_type' in profile['profile_data']:
                            profile_event_type = profile['profile_data']['event_type']


                entity.metadata['property_code'] = entity.metadata['property_code'].replace('\t', '')

                csvFile.writerow([programme.metadata['name'],
                                          programme.metadata['programme_id'],
                                          project.metadata['name'],
                                          project.metadata['project_id'],
                                          project.url,
                                          entity.metadata['property_code'],
                                          entity.metadata['entity_id'],
                                          correct_profile,
                                          fully_correct_profile,
                                          fcorrect_measures,
                                          shr,
                                          ber,
                                          per,
                                          profile_event_type])

    print('nb_programs ' + str(nb_programs))
    print('nb_projects ' + str(nb_projects))
    print('nb_entities ' + str(nb_entities))
    print('nb_valid_entities ' + str(nb_valid_entities))
    file.close()

if __name__ == "__main__":
    main()