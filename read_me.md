This script takes two arguments from the command line:

    1. The name of your HDL you want to test (i.e. "Mux")
    2. The number of inputs your HDL file has (i.e. 2)

This script assumes we're boring and only name our inputs as per the lower case alphabet.

An example invocation might look like this:
~$python3 generate_tst Xor 2

Which would generate a file Xor.tst that looks like this:

load Xor.hdl;

set a 0, set b 0, eval;
set a 0, set b 1, eval;
set a 1, set b 0, eval;
set a 1, set b 1, eval;

Just saves us time having to hard code these things as we go.

- Jack