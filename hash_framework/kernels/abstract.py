from hash_framework.config import config
import os.path
import json

class Kernel:
    def __init__(self, args):
        self.args = args

    def cache_dir(self):
        return config.cache_dir

    def pre_run(self):
        pass

    def out_path(self):
        return "problem.out"

    def run_cmd(self):
        return "echo 'Please override Kernel and supply a run_cmd method.'"

    def post_run(self, return_code):
        if return_code == 10:
            return self.run_sat()
        elif return_code == 20:
            return self.run_unsat()
        else:
            return self.run_error()

    def run_sat(self):
        return []

    def run_unsat(self):
        return []

    def run_error(self):
        print("[Error running model]: " + json.dumps(self.args))