from jsonschema import validate
import yaml


inventory = yaml.load(open("manoci.yaml"), Loader=yaml.FullLoader)
schema = yaml.load(open('schema.yaml'), Loader=yaml.FullLoader)
print(schema)
print(inventory)
validate(inventory, schema)




