
#!/usr/bin/env python3
import sys


if __name__ == '__main__':
    depth_measures = (line.rstrip() for line in sys.stdin)

    increases = 0
    last_depth = None
    for current_depth in depth_measures:
        if last_depth is not None:
            if last_depth < current_depth:
                increases += 1
        last_depth = current_depth


    print(increases)
