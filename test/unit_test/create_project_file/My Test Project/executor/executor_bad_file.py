
# This example is primarily intended to remind users of the importance of verifying input.
from je_auto_control import execute_action, read_action_json
    
execute_action(
    read_action_json(
        r"C:\Users\JeffreyChen\Desktop\Code_Space\AutoControl\test\unit_test\create_project_file/My Test Project/keyword/bad_keyword_1.json"
    )
)
