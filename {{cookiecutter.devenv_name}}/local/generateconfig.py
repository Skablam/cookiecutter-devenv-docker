#!/usr/bin/env python

# This file will generate a config.yml file using apps.yml,
# in the docker-compose.yml structure

import yaml

def generate_configuration():
    stream = file('/vagrant/apps.yml')
    apps = yaml.load(stream)

    config = {}

    # Loop through apps and create a yaml section for each app
    for app, conf in apps['applications'].iteritems():
        app_path = "/vagrant/apps/{0}".format(app)
        config[app] = {"container_name" : app,
                       "build" : app_path,
                       "ports" : ["{0}:{1}".format(conf["port"], conf["port"])],
                       "volumes" : ["".join([app_path, ":/code"])],
                       "environment" : {"PORT" : conf["port"]}
                      }

    with open('/vagrant/config.yml', 'w') as outfile:
        outfile.write( yaml.dump(config, default_flow_style=False) )

if __name__ == "__main__":
    generate_configuration()
