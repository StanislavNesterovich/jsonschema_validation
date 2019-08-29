from jsonschema import validate
import yaml





good_instance = """
testing: ['this1', 'is', 'a', 'test']
"""
validate(yaml.load(good_instance), yaml.load(open('schema.yaml'))) # passes

# Now let try a bad instance...


