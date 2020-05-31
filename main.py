import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_file", help="file to encode/decode using the provided key")
parser.add_argument("output_file", help="name under which the processed file should be saved")
parser.add_argument("key", help="cryptographic key to process file with")
args = parser.parse_args()

with open(args.input_file, 'rb') as in_file:
    with open(args.output_file, 'wb') as out_file:
        key = args.key.encode('utf-8')
        key_length = len(key)
        key_index = 0
        in_data = in_file.read()
        out_data = bytearray(b'')
        for byte in in_data:
            out_data.append(byte ^ key[key_index])
            if key_index == key_length - 1:
                key_index = 0
            else:
                key_index += 1
        out_file.write(out_data)

print("Operation completed successfully!")