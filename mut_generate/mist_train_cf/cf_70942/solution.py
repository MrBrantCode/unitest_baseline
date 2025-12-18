"""
QUESTION:
Create a function named `create_task_points_field` that adds a custom dropdown field named "Task Points" to a Task work item type in TFS 2008 with allowed values of 0, 1, 2, 3, 5, and 8. The function should modify the work item type's XML definition and make the field reportable.
"""

def create_task_points_field(xml_definition):
    """
    Adds a custom dropdown field named "Task Points" to a Task work item type in TFS 2008 
    with allowed values of 0, 1, 2, 3, 5, and 8. The function modifies the work item type's XML 
    definition and makes the field reportable.

    Args:
    xml_definition (str): The XML definition of the work item type.

    Returns:
    str: The updated XML definition with the new "Task Points" field.
    """

    new_field = """
    <FIELD name="Task Points" refname="MyCompany.TaskPoints" type="String" reportable="dimension">
      <ALLOWEDVALUES>
        <LISTITEM value="0" />
        <LISTITEM value="1" />
        <LISTITEM value="2" />
        <LISTITEM value="3" />
        <LISTITEM value="5" />
        <LISTITEM value="8" />
      </ALLOWEDVALUES>
    </FIELD>
    """

    form_group = """
    <Group Label="Status">
      <Column PercentWidth="100">
        <Control Type="FieldControl" FieldName="MyCompany.TaskPoints" Label="Task Points:" LabelPosition="Left" />
      </Column>
    </Group>
    """

    # Find the position to insert the new field
    field_insert_pos = xml_definition.find('</FIELDS>')
    form_insert_pos = xml_definition.find('</FORM>')

    # Insert the new field and form group
    updated_xml = xml_definition[:field_insert_pos] + new_field + xml_definition[field_insert_pos:]
    updated_xml = updated_xml[:form_insert_pos] + form_group + updated_xml[form_insert_pos:]

    return updated_xml