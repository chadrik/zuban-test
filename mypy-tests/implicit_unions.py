from __future__ import absolute_import, print_function


value = 5
value = None
reveal_type(value)


var = None
if "conditional":
    var = 22
reveal_type(var)  # Revealed type is "Union[builtins.int, None]"



if "conditional":
    var2 = None
else:
    var2 = 22
reveal_type(var2)  # Revealed type is "Union[builtins.int, None]"



result = None

for item in range(10):
    if item > 5:
        result = item

reveal_type(result)  # Revealed type is "Union[builtins.int, None]"
