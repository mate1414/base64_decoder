import base64
import yaml
import sys


def process_secret(input_file, output_file, decode_mode=True):
    with open(input_file) as f:
        secret = yaml.safe_load(f)

    if 'data' in secret:
        for key in secret['data']:
            if decode_mode:
                secret['data'][key] = base64.b64decode(secret['data'][key]).decode('utf-8')
            else:
                secret['data'][key] = base64.b64encode(secret['data'][key].encode('utf-8')).decode('utf-8')

    with open(output_file, 'w') as f:
        yaml.dump(secret, f)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python {__file__}.py [decode|encode] input.yaml output.yaml")
        sys.exit(1)

    mode = sys.argv[1]
    if mode not in ['decode', 'encode']:
        print("Invalid mode. Use 'decode' or 'encode'")
        sys.exit(1)

    process_secret(sys.argv[2], sys.argv[3], mode == 'decode')