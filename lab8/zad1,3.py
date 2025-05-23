import json
import pandas as pd

with open('brzydki.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

features_properties = [feature['properties'] for feature in data['features']]

selected_attributes = [
    'featureGroup',
    'featureId',
    'toid',
    'changeEventType',
    'jobReference',
    'validFromTimestamp',
    'accessTopologyComponent',
    'administrativeUnitComponent',
    'baseFormComponent.componentId',
    'baseFormComponent.versionNumber'
]

df = pd.json_normalize(features_properties)

df_selected = df[selected_attributes]

print(df_selected.head())
