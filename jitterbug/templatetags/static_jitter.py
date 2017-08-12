import httpagentparser
import os
import subprocess
import jitterbug

from babeljs import transformer
from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

register = template.Library()


@register.simple_tag
def static_jitter(user_agent, filename):
    app_root = settings.PROJECT_ROOT
    browser = httpagentparser.detect(user_agent).get('browser', {})
    browser_name = browser.get('name', 'IE').lower()
    browser_version = int(browser.get('version', '0').split('.')[0])

    actual_name = filename.split('/')[-1]

    input_file_path = app_root + '/' + filename

    output_dir = os.path.dirname(input_file_path)
    output_file_path = output_dir + '/{}.{}.{}'.format(browser_name, browser_version, actual_name)

    if not os.path.isfile(output_file_path):
        with open(output_file_path, 'w+r+') as output_file:
            import pdb
            pdb.set_trace()

            presets = get_presets(browser_name, browser_version)
            babeledjs = transformer.transform(input_file_path, **presets)
            output_file.write(babeledjs)
            output_file.seek(0)

            js = output_file.read()
            output_file.seek(0)

            minifiedjs, err = minify(js)
            output_file.truncate()

            output_file.write(minifiedjs)

    return static(output_dir + actual_name)


def get_presets(browser_name, browser_version):
    presets = set()

    for preset, browser_name_map in jitterbug.preset_map.items():
        version_string = browser_name_map.get(browser_name, None)
        if version_string is not None:
            version_string = int(version_string)

        if version_string > browser_version:
            presets.add(preset)

    return {
        'plugins': list(presets)
    }


def minify(js_string):
    p = subprocess.Popen(['babili', '--no-babelrc'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.communicate(input=js_string)
