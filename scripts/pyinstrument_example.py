# Instead of writing python script.py, type pyinstrument script.py.
# Your script will run as normal, and at the end (or when you press ^C)
# Pyinstrument will output a colored summary showing where most of the time was spent.


# Pyinstrument also has a Python API. Just surround your code with Pyinstrument, like this:

from pyinstrument import Profiler

profiler = Profiler()
profiler.start()

for i in range(10):
    print(i)

profiler.stop()

profiler.print()