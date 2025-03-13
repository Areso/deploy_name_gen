# deploy-name-gen
Generates names for deployments

## Invokation example
`python3 py_namegen.py` -> `sly-hare-83`

## Parameters for the generation function
`max_obj_len` - how long object name could be, default 8 (doesn't count separator), so `brave-fox` is a valid output  
`digits` - how many digits in the end of the name (with leading zeroes, so `bla-blah-01` is totally valid)  
`separator` - default separator is hyphen `-`, but you could user underscore or anything you want  

## Invokation params from OS
`-l` or `--max_obj_len`  
`-d` or `--digits`  
`-s` or `--separator`  

## How to use code  
to add this to your git project:  
```
git submodule add git@github.com:Areso/deploy_name_gen.git
git submodule update --init
```  

to update:  
```
git submodule update --remote
git commit -am "Upgraded dependency"
```
to downgrade:  
```
cd path/to/submodule_dir/within/the?repo
git reset --hard <commit_hash_or_tag>
cd ..
git commit -am "Downgraded dependency"
git push
```

on a remote:  
```
git submodule init
git submodule update --init
```

## To use inside your code
```
from deploy_name_gen.py_namegen import genname()
```

```
genname()
```
