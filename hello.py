import os
import urllib.request

def download_github_file():
    # URL to the raw file on GitHub
    file_url = "https://raw.githubusercontent.com/Randunu01/OpenUniGit001/main/README.md"

    # Define the folder and file path to save the downloaded file
    folder_name = "fetch"
    file_name = "README.md"

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_path = os.path.join(folder_name, file_name)

    try:
        # Download the file from the URL
        urllib.request.urlretrieve(file_url, file_path)
        print(f"File downloaded successfully to: {file_path}")
    except Exception as e:
        print(f"Failed to download file: {e}")

if __name__ == "__main__":
    download_github_file()
