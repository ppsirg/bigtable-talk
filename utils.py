import argparse
import os
import subprocess

def convert_to_webp(input_folder, quality=75):
    # Ensure the output directory exists
    output_folder = os.path.join(input_folder, 'webp')
    os.makedirs(output_folder, exist_ok=True)

    # Supported image formats
    supported_formats = ('.jpg', '.jpeg', '.png')

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(supported_formats):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.webp')
            try:
                subprocess.run(['cwebp', '-q', str(quality), input_path, '-o', output_path], check=True)
                print(f'Successfully converted {input_path} to {output_path}')
            except subprocess.CalledProcessError as e:
                print(f'Error converting {input_path}: {e}')

def main():
    parser = argparse.ArgumentParser(description='Convert images to .webp format using cwebp.')
    parser.add_argument('input_folder', type=str, help='The input folder containing images to be converted.')

    args = parser.parse_args()
    convert_to_webp(args.input_folder)

if __name__ == '__main__':
    main()
