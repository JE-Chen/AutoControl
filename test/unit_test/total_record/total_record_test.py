import sys

print("t1")
from je_auto_control import keys_table
print("t1")
from je_auto_control import press_key
print("t1")
from je_auto_control import release_key
print("t1")
from je_auto_control import test_record_instance
print("t1")
from je_auto_control import write
print("t1")

try:
    test_record_instance.set_record_enable(True)
    print(keys_table.keys())
    press_key("shift")
    write("123456789")
    press_key("return")
    release_key("return")
    release_key("shift")
    press_key("return")
    release_key("return")
    print(write("abcdefghijklmnopqrstuvwxyz") == "abcdefghijklmnopqrstuvwxyz")
    press_key("return")
    release_key("return")
    """
    this write will print one error -> keyboard write error can't find key : Ѓ and write remain string
    """
    try:
        print(write("?123456789") == "123456789")
    except Exception as error:
        print(repr(error), file=sys.stderr)
    try:
        write("!#@L@#{@#PL#{!@#L{!#{|##PO}!@#O@!O#P!)KI#O_!K")
    except Exception as error:
        print(repr(error), file=sys.stderr)

    print(test_record_instance.test_record_list)

except Exception as error:
    print(repr(error), file=sys.stderr)
