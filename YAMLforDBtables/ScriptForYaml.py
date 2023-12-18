import yaml

# Your YAML content
yaml_content = '''
InstitutionsTable:
  TotalRecords: 
  attributes:
    Name:
      description: "Stores the details of the institution"
    Location:
      description: "Stores the location of the institution"
    AccreditationStatus:
      description: "Stores the accreditation status of the institution"
    EstablishmentYear:
      description: "Stores the year of establishment of the institution"
    InstitutionType:
      description: "Stores the type of the institution"
'''

# Parse YAML content
data = yaml.safe_load(yaml_content)

# Function to generate a single string of all descriptions
def combine_all_descriptions(data):
    table_data = data.get('InstitutionsTable', {})
    attributes = table_data.get('attributes', {})
    
    all_descriptions = ""
    for attribute, details in attributes.items():
        description = details.get('description', '')
        all_descriptions += description + '\n'

    return all_descriptions

# Generate single string of all descriptions
all_descriptions_string = combine_all_descriptions(data)
print(all_descriptions_string)
