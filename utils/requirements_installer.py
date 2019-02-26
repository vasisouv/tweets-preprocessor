import os
import nltk


class RequirementsInstaller:
    def download_nltk_dependencies(self):
        nltk.download('stopwords')
        nltk.download('punkt')
        return self

    def download_spacy_dependencies(self):
        os.system('python -m spacy download en')
        return self


# Run this script to ensure that specific package requirements are installed
if __name__ == '__main__':
    requirements = RequirementsInstaller()
    try:
        requirements.download_nltk_dependencies().download_spacy_dependencies()
        print("All extra packages installed successfully.")
    except Exception as e:
        print("ERROR: " + str(e))
