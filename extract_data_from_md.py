import os

from paths import REPORT_FOLDER_PATH


def extract_data_from_md():
    file_path = ''
    result_dict = {'urls': []}

    # Get the file with the specified extension containing 'md' in its name
    matching_files = os.listdir(REPORT_FOLDER_PATH)

    for file_name in matching_files:
        if file_name.endswith('.md'):
            matching_file_path = os.path.join(REPORT_FOLDER_PATH, file_name)
            print("Matching file found:", matching_file_path)
            file_path = REPORT_FOLDER_PATH.joinpath(file_name)
            break
    else:
        print("No matching file found")

    if file_path:
        with open(file_path, 'r') as file:
            file_contents = file.read()

        lines = file_contents.strip().split('\n')

        # Find the index of the line containing "##"
        index_of_separator = next((i for i, line in enumerate(lines) if "##" in line), None)

        if index_of_separator is not None:
            # Keep only the lines starting from the line containing "##"
            lines = '\n'.join(lines[index_of_separator:])
        else:
            # If "##" is not found, keep the original contents
            lines = file_contents

        lines = lines.split('\n')
        for line in lines:
            parts = line.split(' ')

            if len(parts) >= 2 and 'Folder' not in line:
                status_code = parts[1]

                try:
                    int(status_code)
                except ValueError:
                    continue

                url = ''.join(parts[-1])
                info = ''
                if len(parts) > 2:
                    # info = ' '.join(parts[1:-1]).upper()
                    info = ' '.join(parts[2:-1]).upper()

                result_dict['urls'].append({
                    'status_code': status_code,
                    'url': url,
                    'info': info,
                })

            if len(parts) >= 2 and 'Folder' in line:
                if 'folders' not in result_dict:
                    result_dict['folders'] = []

                status_code = parts[1]
                url = ''.join(parts[-1])

                result_dict['folders'].append({
                    'status_code': status_code,
                    'url': url,
                })

    return result_dict
