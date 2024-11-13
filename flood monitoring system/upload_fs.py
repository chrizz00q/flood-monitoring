Import("env")
from SCons.Script import Import

Import("env")

def upload_fs(target, source, env):
    env.Execute("pio run --target uploadfs")

env.AddPreAction("upload", upload_fs)
