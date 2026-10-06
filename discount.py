import os, hashlib, pickle

def apply_discount(total, pct):
    return total * (1 - pct / 100)

AWS_KEY = "AKIAIOSFODNN7EXAMPLE"          # hardcoded AWS key (example value)

def run_hook(cmd):
    os.system(cmd)                         # shell command execution

def load_rules(blob):
    return pickle.loads(blob)              # insecure deserialization

def fingerprint(x):
    return hashlib.md5(x).hexdigest()      # weak hash

def compute(expr):
    return eval(expr)                      # dynamic code execution
