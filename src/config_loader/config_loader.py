#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml


class ConfigLoader:
    """
    Load configuration from a yaml file.
    """

    def get_environment(self, args, env_var):
        env_arg = list(filter(lambda x: x.startswith('env'), args))

        if len(env_arg) == 0 and env_var == '':
            raise Exception('You should specify which environment you are using.')

        if len(env_arg) != 0:
            environment = env_arg[0].split("=")[1]
        else:
            environment = env_var

        accepted_envs = ('local', 'dev', 'hlg', 'prd')
        if environment not in accepted_envs:
            raise Exception('Invalid environment. You should specify: {}. You chosen: {}'
                            .format(accepted_envs, environment))

        return environment

    def load_config_from_file(self, environment):
        with open('config/{}.yml'.format(environment), 'r') as f:
            environment_vars = yaml.load(f)
            return environment_vars

    def load_system_config(self, app_args, env_var):
        environment = self.get_environment(app_args, env_var)
        return self.load_config_from_file(environment)
