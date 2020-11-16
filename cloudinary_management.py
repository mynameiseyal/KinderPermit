import os
import sys
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url


class Cloudinary:
    # config
    os.chdir(os.path.join(os.path.dirname(sys.argv[0]), '.'))
    if os.path.exists('settings.py'):
        exec(open('settings.py').read())

    DEFAULT_TAG = "python_sample_basic"

    def dump_response(self, response):
        print("Upload response:")
        for key in sorted(response.keys()):
            print("  %s: %s" % (key, response[key]))

    def upload_files(self, file):
        print("--- Upload a local file")
        response = upload(file, tags=self.DEFAULT_TAG)
        self.dump_response(response)
        url, options = cloudinary_url(
            response['public_id'],
            format=response['format'],
            width=200,
            height=150,
            crop="fill"
        )
        return response['url']