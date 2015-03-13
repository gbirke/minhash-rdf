import os.path
import re
import collections
import sys

change_rates = [1, 5, 10, 25, 50]
#change_rates = [50]

class ObjectReplacer(object):
    def __init__(self):
        self.prev_objects = collections.deque(maxlen=20)

    def get_new_line(self, line, current_object):
        changed_line = line
        for o in self.prev_objects:
            if o != current_object:
                changed_line = line.replace(current_object, o)
                break
        if changed_line == line and linecount > 2:
            print "object {} (line {}) could not be changed.".format(current_object, linecount)
        self.prev_objects.append(current_object)
        return changed_line


if len(sys.argv) < 2:
    print "You must give a data source as argument!"
    sys.exit(1)

data_source = sys.argv[1]

ds_root, ds_ext = os.path.splitext(data_source)
target_files = {r:open("{}_{:02d}{}".format(ds_root, r, ds_ext), "w") for r in change_rates}
change_counters = {r:0 for r in change_rates}
source_file = open(data_source, "r")
linecount = 1
triple_pattern = re.compile(r"^\s*<[^>]+>\s+<[^>]+>\s+(<[^>]+>)\s+.$")
line_changer = ObjectReplacer()
for line in source_file:
    is_triple = triple_pattern.match(line)
    if is_triple:
        changed_line = line_changer.get_new_line(line, is_triple.group(1))
        
    for r in change_rates:
        if linecount % (100/r) or not is_triple:
            target_files[r].write(line)
        else:
            change_counters[r] += 1
            if not change_counters[r] % 2:
                target_files[r].write(changed_line)
    linecount += 1

