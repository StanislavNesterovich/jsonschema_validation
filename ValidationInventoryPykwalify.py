from pykwalify.core import Core
import yaml

inventory = yaml.load(open("manoci.yaml"), Loader=yaml.FullLoader)
#
print (inventory)
for i in inventory['localhost_fake'].keys():
    print(i)

inven_validation = Core(source_file="manoci.yaml", schema_files=["schema2.yaml"])
inven_validation.validate(raise_exception=True)

