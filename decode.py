import base64
from os import system
import subprocess
import json


def decode(encoded_string):
    return base64.b64decode(encoded_string)


def copy_to_clipboard(output):
    process = subprocess.Popen(
        "pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=subprocess.PIPE
    )
    process.communicate(output)


def prettify_json_output(input):
    parsed = json.loads(input)
    return json.dumps(parsed, indent=4, sort_keys=True)


def main():
    while True:
        input_string = input("Paste base64 encoded string here and hit Enter:\n")

        if input_string == "q":
            print("Exiting...")
            exit()

        output_string = decode(input_string)
        try:
            output_string = prettify_json_output(output_string)
        except:
            pass

        print(f"{'-'*20}-----\nDecoded Data:\n")
        print(output_string.decode("utf-8"))

        copy_to_clipboard(output_string)
        print(f"\nDecoded Data copied to Clipboard\n{'-'*20}")


if __name__ == "__main__":
    main()
