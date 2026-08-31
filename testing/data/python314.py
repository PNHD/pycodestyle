#: Okay
try:
    raise AssertionError('hi')
except AssertionError, ValueError:
    pass

t'hello {world}'
t'{hello}:{world}'
t'in{x}'
t'hello{world=}'
#: Okay
# new nested f-strings
t'{
    thing
} {t'{other} {thing}'}'
#: E201:1:4 E202:1:17
t'{ an_error_now }'
#: Okay
t'{x:02x}'
#: Okay
# nested format specifiers
t'{x:0.{digits:d}f}'
t'{x:{width:d}.2f}'
t'{x:{y:{z:02}}}'
t'{x:{y!r:10}}'
t'{x:{y[1:2]}}'
t'{x:{({"a": "b"})}}'
#: E231
t"{x:{({'a':'b'})}}"
