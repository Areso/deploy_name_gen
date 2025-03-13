# deploy-name-gen
Generates names for deployments

## Invokation example
`python3 py_namegen.py` -> `sly-hare-83`

## Parameters for generation function
`max_obj_len` - how long object name could be, default 8 (doesn't count separator), so `brave-fox` is a valid output  
`digits` - how many digits in the end of the name (with leading zeroes, so `bla-blah-01` is totally valid)  
`separator` - default separator is hyphen `-`, but you could user underscore or anything you want  

## Invokation example
`-l` or `--max_obj_len`  
`-d` or `--digits`  
`-s` or `--separator`  
