import os

from PIL import Image, ImageEnhance


def edit_image(file_path: str, destination: str):
    img = Image.open(fp=file_path)
    saturation_filter = ImageEnhance.Color(img)
    saturated_image = saturation_filter.enhance(1.45)
    exposure_filter = ImageEnhance.Contrast(saturated_image)
    exposed_image = exposure_filter.enhance(1.2)

    exposed_image.save(destination)


def main():
    input_directory = os.environ.get('input_directory')
    output_directory = os.environ.get('output_directory')

    if input_directory is None or output_directory is None:
        print(f'''
Missing required environment variables.
$input_directory is "{input_directory}"
$output_directory is "{output_directory}"
''')
        exit(1)

    for filename in os.listdir(input_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            edit_image(os.path.join(input_directory, filename), os.path.join(output_directory, filename))


if __name__ == "__main__":
    main()
